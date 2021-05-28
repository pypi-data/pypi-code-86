import concurrent.futures
import json
import logging
import random
import ssl
import threading
import time
from abc import abstractmethod
from enum import Enum
from time import sleep
from typing import Optional, Tuple

from websocket import WebSocketApp, ABNF, WebSocketException, setdefaulttimeout, WebSocketConnectionClosedException

from hiro_graph_client.clientlib import AbstractTokenApiHandler

logger = logging.getLogger(__name__)
""" The logger for this module """


class ErrorMessage:
    """
    The structure of an incoming error message
    """
    code: int
    message: str

    def __init__(self,
                 code,
                 message):
        """
        Constructor

        :param code: Numerical error code of the error
        :param message: Error message
        """
        self.code = int(code)
        self.message = str(message)

    @classmethod
    def parse(cls, message: str):
        """
        :param message: The message received from the websocket. Will be decoded here.
        :return: The new error message or None if this is not an error message.
        """
        json_message: dict = json.loads(message)
        error_message = json_message.get('error')
        if isinstance(error_message, dict):
            return cls(error_message.get('code'),
                       error_message.get('message'))
        else:
            return None

    def __str__(self):
        return json.dumps(vars(self))

    def to_dict(self) -> dict:
        return {
            "error": {
                "code": self.code,
                "message": self.message
            }
        }


class ReaderStatus(str, Enum):
    """
    The states the reader thread can be in.
    """
    NONE = 'Not started',
    STARTING = 'Starting',
    RUNNING_PRELIMINARY = 'Running preliminary (status of token unknown)',
    RUNNING = 'Running'
    RESTARTING = 'Restarting',
    DONE = 'Finished normally',
    FAILED = 'Finished because of error'


class AbstractAuthenticatedWebSocketHandler:
    """
    The basic class for all WebSockets.
    """
    _api_handler: AbstractTokenApiHandler
    _proxy_hostname: str
    _proxy_port: str
    _proxy_auth: dict

    _reconnect_delay: int

    _protocol: str
    _url: str

    _timeout: int
    _auto_reconnect: bool

    _ws: Optional[WebSocketApp]
    _ws_lock: threading.RLock

    _reader_executor: concurrent.futures.ThreadPoolExecutor
    """
    Executor for the reader thread *self._run()*.
    """
    _reader_future: Optional[concurrent.futures.Future]
    """
    Carries the result of the reader thread *self._run()* via the *self._reader_executor*.
    """
    _reader_status: ReaderStatus
    """
    Tracks the status of the internal reader thread.  
    """
    _reader_guard: threading.Condition
    """
    Meant to protect the startup sequence. *self.start()* will return only after the startup sequence has been finished.
    When start is handled, it gets notified in *self.on_open()* on success or *self.on_error()* on error.
    Se also *self._reader_starting*.
    """
    _inner_exception: Optional[Exception]
    """
    The WebSocketApp catches all exceptions that are thrown in the *on_[...]* methods, so we have to store the exceptions
    here.
    """

    _sender_thread_lock: threading.RLock

    MAX_RETRIES = 3

    def __init__(self,
                 api_handler: AbstractTokenApiHandler,
                 api_name: str,
                 timeout: int = 5,
                 auto_reconnect: bool = True):
        """
        Create the websocket

        :param api_handler: Required: The api handler for authentication.
        :param api_name: The name of the ws api.
        :param timeout: The timeout for websocket messages. Default is 5sec.
        :param auto_reconnect: Try to create a new websocket automatically when *self.send()* fails. If this is set
                               to False, a WebSocketException will be raised instead. The default is True.
        """
        if not api_handler:
            raise ValueError('Parameter api_handler= cannot be empty.')

        if not api_name:
            raise ValueError('Parameter api_name= cannot be empty.')

        self._url, self._protocol, self._proxy_hostname, self._proxy_port, self._proxy_auth = \
            api_handler.get_websocket_config(api_name)

        self._api_handler = api_handler

        self._timeout = timeout
        self._auto_reconnect = auto_reconnect

        self._reader_guard = threading.Condition()
        self._reader_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self._reader_status = ReaderStatus.NONE
        self._reader_future = None
        self._ws = None
        self._ws_lock = threading.RLock()
        self._inner_exception = None

        self._sender_thread_lock = threading.RLock()

        setdefaulttimeout(timeout)

        random.seed(time.time_ns())

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.stop(self._timeout)

    def _set_error(self, error: Exception) -> None:
        """
        Log the Exception, store it and set the status to FAILED.

        :param error: The Exception to store.
        """
        self._reader_status = ReaderStatus.FAILED
        self._inner_exception = error
        logger.error("Reader thread encountered error: %s", str(error))

    def _check_message(self, ws: WebSocketApp, message: str) -> None:
        """
        Look for error 401. Try to reconnect with a new token when this is encountered.
        Set status to *ReaderStatus.RESTART* when a token is no longer valid on error code 401.
        Set status to *ReaderStatus.FAILED* when error 401 is received and the token was never valid.

        :param ws: WebSocketApp
        :param message: Incoming message as string
        """
        with self._reader_guard:
            try:
                error_message = ErrorMessage.parse(message)
                if error_message:
                    if error_message.code == 401:
                        if self._reader_status == ReaderStatus.RUNNING_PRELIMINARY:
                            raise WebSocketException(
                                "Received error message while token was never valid: " + str(error_message))
                        else:
                            self._api_handler.refresh_token()

                            # If we get here, the token has been refreshed successfully.
                            self._reconnect_delay = 0
                            self._reader_status = ReaderStatus.RESTARTING

                            logger.info("Refreshing token because of error: %s", str(error_message))
                            self._close()
                            return
                else:
                    if logger.isEnabledFor(logging.DEBUG):
                        logger.debug("Received message: %s", message)
                    else:
                        logger.info("Received message of length %d", len(message))

                # If we get here, the token is valid
                if self._reader_status != ReaderStatus.RUNNING:
                    self._reader_status = ReaderStatus.RUNNING
                    self._reconnect_delay = 0

                self.on_message(ws, message)
            except Exception as err:
                self._set_error(err)
                self._close()

    def _check_open(self, ws: WebSocketApp) -> None:
        """
        First signal, that the connection has been opened successfully. Then
        call *self.on_open* and set *self._reader_status* to CHECKING_TOKEN if opening succeeded.

        :param ws: WebSocketApp
        """
        logger.debug("Connection to %s open.", self._url)

        with self._reader_guard:
            try:
                if self._reader_status == ReaderStatus.STARTING:
                    self._reader_guard.notify()
                self._reader_status = ReaderStatus.RUNNING_PRELIMINARY

                self.on_open(ws)
            except Exception as err:
                self._set_error(err)
                self._close()

    def _check_close(self, ws: WebSocketApp, code: int, reason: str):
        """
        Call *self.on_close*. When *code* and *reason* are None, the stop has been issued locally and not by the
        remote side.

        :param ws: WebSocketApp
        :param code: Code of stop message
        :param reason: Reason str of stop message
        """
        with self._reader_guard:
            try:
                if code or reason:
                    logger.debug("Received close from remote: %s %s. Restarting...", code, reason)
                    self._reader_status = ReaderStatus.RESTARTING
                else:
                    logger.debug("Received local close. Exiting...")

                self.on_close(ws, code, reason)
            except Exception as err:
                self._set_error(err)

    def _check_error(self, ws: WebSocketApp, error: Exception) -> None:
        """
        Just log the error and propagate it to *self.on_error*.

        :param ws: WebSocketApp
        :param error: Exception
        """
        # logger.error("Received error: %s", str(error))
        # logger.exception(error)

        with self._reader_guard:
            try:
                if self._reader_status == ReaderStatus.STARTING:
                    self._reader_guard.notify()

                self._set_error(error)
                self.on_error(ws, error)
            except Exception as err:
                self._set_error(err)

    def _run(self) -> Tuple[ReaderStatus, Exception]:
        """
        The _run loop of the reader thread. Exits only when *self._reader_status* is ReaderStatus.DONE or
        ReaderStatus.FAILED.

        :return: Tuple of (ReaderStatus - either DONE or ERROR, the Exception on ERROR or None)
        """
        with self._reader_guard:
            try:
                self._reconnect_delay = 0

                while self._reader_status not in [ReaderStatus.DONE, ReaderStatus.FAILED]:
                    self._reconnect_delay = self._backoff(self._reconnect_delay)

                    self._reader_status = ReaderStatus.STARTING
                    self._inner_exception = None

                    header: dict = {
                        "Sec-WebSocket-Protocol": "{}, token-{}".format(self._protocol, self._api_handler.token)
                    }

                    with self._ws_lock:
                        self._ws = WebSocketApp(self._url,
                                                header=header,
                                                on_open=lambda ws: self._check_open(ws),
                                                on_close=lambda ws, code, reason: self._check_close(ws, code, reason),
                                                on_message=lambda ws, msg: self._check_message(ws, msg),
                                                on_error=lambda ws, err: self._check_error(ws, err),
                                                on_ping=lambda ws, data: ws.send(data, opcode=ABNF.OPCODE_PONG))

                    # BUG: While this is initializing, the self._reader_status_condition should remain locked until the
                    # dispatcher listens at the socket. Since we cannot securely release it within, we have to release
                    # it beforehand and expect errors when the websocket gets closed before it was completely
                    # initialized.
                    try:
                        self._reader_guard.release()
                        self._ws.run_forever(http_proxy_host=self._proxy_hostname,
                                             http_proxy_port=self._proxy_port,
                                             http_proxy_auth=self._proxy_auth,
                                             sslopt={
                                                 "cert_reqs": ssl.CERT_NONE
                                             } if AbstractTokenApiHandler.accept_all_certs else None)
                    finally:
                        self._reader_guard.acquire()

            except Exception as error:
                self._check_error(self._ws, error)

            self.on_close(self._ws)

            with self._ws_lock:
                self._ws = None

            return self._reader_status, self._inner_exception

    @staticmethod
    def _backoff(reconnect_delay: int) -> int:
        """
        Sleeps for *reconnect_delay* seconds, then returns the delay in seconds for the next try.

        :param reconnect_delay: Delay in seconds to wait.
        :return: Next value for the delay.
        """
        if reconnect_delay:
            sleep(reconnect_delay)

        return (reconnect_delay + 1) if reconnect_delay < 10 \
            else (reconnect_delay + 10) if reconnect_delay < 60 \
            else random.randint(60, 600)

    def _close(self):
        """
        Internal stop that does not join the reader thread. Intended to be called on unrecoverable errors within the
        reader thread, i.e. invalid tokens.
        """
        with self._ws_lock:
            if self._ws:
                self._ws.close(status=ABNF.OPCODE_CLOSE,
                               reason="{} closing".format(self._api_handler.get_user_agent()))

    ###############################################################################################################
    # Public API Reader thread
    ###############################################################################################################

    @abstractmethod
    def on_open(self, ws: WebSocketApp):
        pass

    @abstractmethod
    def on_close(self, ws: WebSocketApp, code: int = None, reason: str = None):
        pass

    @abstractmethod
    def on_message(self, ws: WebSocketApp, message: str):
        pass

    @abstractmethod
    def on_error(self, ws: WebSocketApp, error: Exception):
        pass

    ###############################################################################################################
    # Public API Main Writer thread
    ###############################################################################################################

    def start(self) -> None:
        """
        Start the background thread for receiving messages from the websocket. Returns when the websocket has been
        created.

        :raise WebSocketException: When the startup of the reader thread fails.
        """

        try:
            with self._reader_guard:
                if self._reader_future:
                    return
                self._reader_future = self._reader_executor.submit(AbstractAuthenticatedWebSocketHandler._run, self)
                self._reader_guard.wait()
                start_ok = (self._reader_status != ReaderStatus.FAILED)

            if not start_ok:
                self.join()
        except Exception as err:
            raise WebSocketException("Cannot start reader thread.") from err

    def join(self, timeout: int = None) -> None:
        """
        Joins the reader thread and deletes it thereafter.

        :param timeout: Optional timeout in seconds for joining the reader thread.
        :raise WebSocketException: When the reader thread finished with an exception.
        """
        if not self._reader_future:
            return

        try:
            status, exception = self._reader_future.result(timeout)

            if status == ReaderStatus.FAILED:
                if exception:
                    raise exception
                else:
                    raise WebSocketException("Unspecified error")
        except Exception as err:
            raise WebSocketException("Reader thread finished with error.") from err
        finally:
            self._reader_future = None

    def stop(self, timeout: int = None) -> None:
        """
        Intentionally closes this websocket. Joins on the reader before returning.

        :param timeout: Optional timeout in seconds for joining the reader thread.
        """
        with self._reader_guard:
            self._reader_status = ReaderStatus.DONE
        self._close()
        self.join(timeout)

    def restart(self, timeout: int = None) -> None:
        """
        Closes the websocket and starts a new one.

        :param timeout: Optional timeout in seconds for joining the old reader thread.
        """
        self.stop(timeout)
        self.start()

    def send(self, message: str) -> None:
        """
        Send message across the websocket. Make sure, that this is thread-safe.

        :param message: Message as string
        :raise WebSocketException: When *self._auto_reconnect* is False: If a message cannot be sent and all retries
                                   have been exhausted.
        :raise WebSocketConnectionClosedException: When the websocket is not available at all.
        """
        with self._sender_thread_lock:
            retries = 0
            retry_delay = 0

            while True:
                retry_delay = self._backoff(retry_delay)

                try:
                    with self._reader_guard:
                        if self._reader_status in [ReaderStatus.NONE]:
                            raise WebSocketConnectionClosedException('Websocket not started.')
                        elif self._reader_status in [ReaderStatus.DONE, ReaderStatus.FAILED]:
                            raise WebSocketConnectionClosedException('Websocket has exited.')
                        elif self._reader_status not in [ReaderStatus.RUNNING, ReaderStatus.RUNNING_PRELIMINARY]:
                            raise WebSocketException('Websocket not ready.')

                    with self._ws_lock:
                        if not self._ws:
                            raise WebSocketConnectionClosedException('Websocket is gone.')

                        if logger.isEnabledFor(logging.DEBUG):
                            logger.debug("Sending message: %s", message)
                        else:
                            logger.info("Sending message of length %d", len(message))

                        self._ws.send(message)

                    return

                except WebSocketConnectionClosedException:
                    raise

                except Exception as err:
                    if retries < self.MAX_RETRIES:
                        if self._auto_reconnect:
                            retries = 0
                            logger.warning('Restarting because of error: %s', str(err))
                            self.restart(self._timeout)
                        else:
                            raise WebSocketException("Could not send and all retries have been exhausted.")
                    else:
                        logger.warning('Retrying to send message because of error: %s', str(err))
                        retries += 1
