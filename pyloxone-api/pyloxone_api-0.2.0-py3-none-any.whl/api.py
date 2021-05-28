"""
Loxone Api

For more details about this component, please refer to the documentation at
https://github.com/JoDehli/pyloxone-api
"""
import asyncio
import binascii
import hashlib
import json
import logging
import queue
import time
import traceback
import urllib.request as req
import uuid
from base64 import b64encode
from math import floor  # pylint: disable=no-name-in-module
from struct import unpack  # pylint: disable=no-name-in-module

import httpx
import websockets as wslib
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Hash import HMAC, SHA1, SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util import Padding

from .const import (
    AES_KEY_SIZE,
    CMD_AUTH_WITH_TOKEN,
    CMD_ENABLE_UPDATES,
    CMD_ENCRYPT_CMD,
    CMD_GET_KEY,
    CMD_GET_KEY_AND_SALT,
    CMD_GET_PUBLIC_KEY,
    CMD_GET_VISUAL_PASSWD,
    CMD_KEY_EXCHANGE,
    CMD_REFRESH_TOKEN,
    CMD_REFRESH_TOKEN_JSON_WEB,
    CMD_REQUEST_TOKEN,
    CMD_REQUEST_TOKEN_JSON_WEB,
    DEFAULT_TOKEN_PERSIST_NAME,
    ERROR_VALUE,
    IV_BYTES,
    KEEP_ALIVE_PERIOD,
    LOXAPPPATH,
    SALT_BYTES,
    SALT_MAX_AGE_SECONDS,
    SALT_MAX_USE_COUNT,
    TIMEOUT,
    TOKEN_PERMISSION,
)

from .lxtoken import LxToken

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)
_LOGGER.addHandler(logging.StreamHandler())


class LoxAPI:
    def __init__(
        self,
        host=None,
        port=None,
        user=None,
        password=None,
        token_persist_filename=DEFAULT_TOKEN_PERSIST_NAME,
    ):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._token_persist_filename = token_persist_filename

        self._iv = get_random_bytes(IV_BYTES)
        self._key = get_random_bytes(AES_KEY_SIZE)
        self._salt = ""
        self._salt_used_count = 0
        self._salt_time_stamp = 0
        self._public_key = None
        self._rsa_cipher = None
        self._session_key = None
        self._ws = None
        self._current_message_typ = None
        self._encryption_ready = False
        self._visual_hash = None

        self.message_call_back = None
        self._url = None
        self.connect_retries = 20
        self.connect_delay = 10
        self._state = "CLOSED"
        self._secured_queue = queue.Queue(maxsize=1)
        self.config_dir = "."
        self.json = None
        self.version = None
        self._https_status = None
        self._token = LxToken(
            token_dir=self.config_dir,
            token_filename=self._token_persist_filename,
        )

    async def getJson(self):
        if self._port == 80:
            url_api = f"http://{self._host}/jdev/cfg/apiKey"
        else:
            url_api = f"http://{self._host}:{self._port}/jdev/cfg/apiKey"
        async with httpx.AsyncClient(
            auth=(self._user, self._password), verify=False, timeout=TIMEOUT
        ) as client:
            api_resp = await client.get(url_api)
        if api_resp.status_code != 200:
            _LOGGER.error(
                f"Could not connect to Loxone! Status code {api_resp.status_code}."
            )
            return False

        req_data = api_resp.json()
        if "LL" in req_data:
            if "Code" in req_data["LL"] and "value" in req_data["LL"]:
                _ = req_data["LL"]["value"]
                if isinstance(_, str):
                    try:
                        _ = eval(_)
                    except ValueError:
                        pass
                if isinstance(_, dict):
                    if "httpsStatus" in _:
                        self._https_status = _["httpsStatus"]

        self._url = api_resp.url.copy_with(path="")

        url_version = f"{self._url}/jdev/cfg/version"
        async with httpx.AsyncClient(
            auth=(self._user, self._password), verify=False, timeout=TIMEOUT
        ) as client:
            version_resp = await client.get(url_version)
        if version_resp.status_code == 200:
            vjson = version_resp.json()
            if "LL" in vjson:
                if "Code" in vjson["LL"] and "value" in vjson["LL"]:
                    self.version = [int(x) for x in vjson["LL"]["value"].split(".")]

        async with httpx.AsyncClient(
            auth=(self._user, self._password), verify=False, timeout=TIMEOUT
        ) as client:
            my_response = await client.get(f"{self._url}{LOXAPPPATH}")
        status = my_response.status_code
        if status == 200:
            self.json = my_response.json()
            if self.version is not None:
                self.json["softwareVersion"] = self.version
        else:
            self.json = None

        if self.json is not None:
            if "softwareVersion" in self.json:
                vers = self.json["softwareVersion"]
                if isinstance(vers, list) and len(vers) >= 2:
                    try:
                        self._version = float(f"{vers[0]}.{vers[1]}")
                    except ValueError:
                        self._version = 0

        return status

    async def _refresh_token(self):
        while True:
            seconds_to_refresh = self._token.seconds_to_expire()
            await asyncio.sleep(seconds_to_refresh)
            command = f"{CMD_GET_KEY}"
            enc_command = self._encrypt(command)
            await self._ws.send(enc_command)
            message = await self._ws.recv()
            resp_json = json.loads(message)
            token_hash = None
            if "LL" in resp_json:
                if "value" in resp_json["LL"]:
                    key = resp_json["LL"]["value"]
                    if key == "":
                        if self._version < 12.0:
                            digester = HMAC.new(
                                binascii.unhexlify(key),
                                self._token.token.encode("utf-8"),
                                SHA1,
                            )
                        else:
                            digester = HMAC.new(
                                binascii.unhexlify(key),
                                self._token.token.encode("utf-8"),
                                SHA256,
                            )
                        token_hash = digester.hexdigest()

            if token_hash is not None:
                if self._version < 10.2:
                    command = f"{CMD_REFRESH_TOKEN}{token_hash}/{self._user}"
                else:
                    command = f"{CMD_REFRESH_TOKEN_JSON_WEB}{token_hash}/{self._user}"

                enc_command = self._encrypt(command)
                await self._ws.send(enc_command)
                message = await self._ws.recv()
                resp_json = json.loads(message)

                _LOGGER.debug(
                    f"Seconds before refresh: {self._token.seconds_to_expire()}"
                )

                if "LL" in resp_json:
                    if "value" in resp_json["LL"]:
                        if "validUntil" in resp_json["LL"]["value"]:
                            self._token.valid_until = resp_json["LL"]["value"][
                                "validUntil"
                            ]

                self._token.save()

    async def start(self):
        consumer_task = self._ws_listen()
        keep_alive_task = self._keep_alive(KEEP_ALIVE_PERIOD)
        refresh_token_task = self._refresh_token()

        _, pending = await asyncio.wait(
            [consumer_task, keep_alive_task, refresh_token_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        # The first task has completed. Cancel the others
        for task in pending:
            task.cancel()
        # Wait until they have cancelled properly
        await asyncio.wait(pending)

        if self._state != "STOPPING" and self._state != "CONNECTED":
            await self._reconnect()

    async def _reconnect(self):
        for i in range(self.connect_retries):
            _LOGGER.debug(f"reconnect: {i + 1} from {self.connect_retries}")
            await self.stop()
            self._state = "CONNECTING"
            _LOGGER.debug(f"wait for {self.connect_delay} seconds...")
            await asyncio.sleep(self.connect_delay)
            res = await self.async_init()
            if res is True:
                await self.start()
                break

    # https://github.com/aio-libs/aiohttp/issues/754
    async def stop(self):
        try:
            self._state = "STOPPING"
            if not self._ws.closed:
                await self._ws.close()
            return 1
        except:
            return -1

    async def _keep_alive(self, second):
        while True:
            await asyncio.sleep(second)
            if self._encryption_ready:
                await self._ws.send("keepalive")

    async def _send_secured(self, device_uuid, value, code):
        pwd_hash_str = f"{code}:{self._visual_hash.salt}"
        if self._visual_hash.hash_alg == "SHA1":
            m = hashlib.sha1()
        elif self._visual_hash.hash_alg == "SHA256":
            m = hashlib.sha256()
        else:
            _LOGGER.error(
                "Unrecognised hash algorithm: {}".format(self._visual_hash.hash_alg)
            )
            return -1

        m.update(pwd_hash_str.encode("utf-8"))
        pwd_hash = m.hexdigest().upper()
        if self._visual_hash.hash_alg == "SHA1":
            digester = HMAC.new(
                binascii.unhexlify(self._visual_hash.key),
                pwd_hash.encode("utf-8"),
                SHA1,
            )
        elif self._visual_hash.hash_alg == "SHA256":
            digester = HMAC.new(
                binascii.unhexlify(self._visual_hash.key),
                pwd_hash.encode("utf-8"),
                SHA256,
            )

        command = f"jdev/sps/ios/{digester.hexdigest()}/{device_uuid}/{value}"
        await self._ws.send(command)

    async def send_secured__websocket_command(self, device_uuid, value, code):
        self._secured_queue.put((device_uuid, value, code))
        # Get visual hash
        command = f"{CMD_GET_VISUAL_PASSWD}{self._user}"
        enc_command = self._encrypt(command)
        await self._ws.send(enc_command)

    async def send_websocket_command(self, device_uuid, value):
        """Send a websocket command to the Miniserver."""
        command = f"jdev/sps/io/{device_uuid}/{value}"
        _LOGGER.debug(f"send command: {command}")
        await self._ws.send(command)

    async def async_init(self):
        # Read token from file

        _LOGGER.debug("try to get_token_from_file")
        try:
            if self._token.load():
                _LOGGER.debug("token successfully loaded from file")
        except OSError:
            _LOGGER.debug("error token read")

        # Get public key from Loxone
        resp = await self._get_public_key()

        if not resp:
            return ERROR_VALUE

        # Init resa cipher
        try:
            self._public_key = self._public_key.replace(
                "-----BEGIN CERTIFICATE-----", "-----BEGIN PUBLIC KEY-----\n"
            )
            public_key = self._public_key.replace(
                "-----END CERTIFICATE-----", "\n-----END PUBLIC KEY-----\n"
            )
            self._rsa_cipher = PKCS1_v1_5.new(RSA.importKey(public_key))
            _LOGGER.debug("init_rsa_cipher successfully...")
            result = True
        except KeyError:
            _LOGGER.debug("init_rsa_cipher error...")
            _LOGGER.debug(f"{traceback.print_exc()}")
            result = False
        rsa_gen = result
        if not rsa_gen:
            return ERROR_VALUE

        # Generate session key
        try:
            aes_key = binascii.hexlify(self._key).decode("utf-8")
            iv = binascii.hexlify(self._iv).decode("utf-8")
            sess = f"{aes_key}:{iv}"
            sess = self._rsa_cipher.encrypt(bytes(sess, "utf-8"))
            self._session_key = b64encode(sess).decode("utf-8")
            _LOGGER.debug("generate_session_key successfully...")
            result1 = True
        except KeyError:
            _LOGGER.debug("error generate_session_key...")
            result1 = False
        session_gen = result1
        if not session_gen:
            return ERROR_VALUE

        # Exchange keys
        try:
            if self._url.scheme == "https":
                new_url = self._url.copy_with(scheme="wss", path="/ws/rfc6455")
            else:
                new_url = self._url.copy_with(scheme="ws", path="/ws/rfc6455")
            # pylint: disable=no-member
            self._ws = await wslib.connect(str(new_url), timeout=TIMEOUT)

            await self._ws.send(f"{CMD_KEY_EXCHANGE}{self._session_key}")

            message = await self._ws.recv()
            self._unpack_loxone_message(message)
            if self._current_message_typ != 0:
                _LOGGER.debug("error by getting the session key response...")
                return ERROR_VALUE

            message = await self._ws.recv()
            resp_json = json.loads(message)
            if "LL" in resp_json:
                if "Code" in resp_json["LL"]:
                    if resp_json["LL"]["Code"] != "200":
                        return ERROR_VALUE
            else:
                return ERROR_VALUE

        except ConnectionError:
            _LOGGER.debug("connection error...")
            return ERROR_VALUE

        self._encryption_ready = True

        if (
            self._token is None
            or self._token.token == ""
            or self._token.seconds_to_expire() < 300
        ):
            res = await self._acquire_token()
        else:
            res = await self._use_token()
            # Delete old token
            if res is ERROR_VALUE:
                self._token.delete()
                _LOGGER.debug(
                    "Old Token found and deleted. Please restart Homeassistant to acquire new token."
                )
                return ERROR_VALUE

        if res is ERROR_VALUE:
            return ERROR_VALUE

        if self._ws.closed:
            _LOGGER.debug(f"Connection closed. Reason {self._ws.close_code}")
            return False

        command = f"{CMD_ENABLE_UPDATES}"
        enc_command = self._encrypt(command)
        await self._ws.send(enc_command)
        if self._ws.closed:
            _LOGGER.debug(f"Connection closed. Reason {self._ws.close_code}")
            return False
        _ = await self._ws.recv()
        _ = await self._ws.recv()

        self._state = "CONNECTED"
        return True

    async def _ws_listen(self):
        """Listen to all commands from the Miniserver."""
        try:
            while True:
                message = await self._ws.recv()
                await self._async_process_message(message)
                await asyncio.sleep(0)
        except:
            await asyncio.sleep(5)
            if self._ws.closed and self._ws.close_code in [4004, 4005]:
                self._token.delete()

            elif self._ws.closed and self._ws.close_code:
                await self._reconnect()

    async def _async_process_message(self, message):
        """Process the messages."""
        if len(message) == 8:
            unpacked_data = unpack("ccccI", message)
            self._current_message_typ = int.from_bytes(
                unpacked_data[1], byteorder="big"
            )
            if self._current_message_typ == 6:
                _LOGGER.debug("Keep alive response received...")
        else:
            parsed_data = self._parse_loxone_message(message)
            _LOGGER.debug(
                "message [type:{}]):{}".format(
                    self._current_message_typ, json.dumps(parsed_data, indent=2)
                )
            )

            try:
                resp_json = json.loads(parsed_data)
            except TypeError:
                resp_json = None

            # Visual hash and key response
            if resp_json is not None and "LL" in resp_json:
                if (
                    "control" in resp_json["LL"]
                    and "code" in resp_json["LL"]
                    and resp_json["LL"]["code"] in [200, "200"]
                ):
                    if "value" in resp_json["LL"]:
                        if (
                            "key" in resp_json["LL"]["value"]
                            and "salt" in resp_json["LL"]["value"]
                        ):
                            key_and_salt = LxJsonKeySalt()
                            key_and_salt.read_user_salt_response(parsed_data)
                            key_and_salt.time_elapsed_in_seconds = (
                                time_elapsed_in_seconds()
                            )
                            self._visual_hash = key_and_salt

                            while not self._secured_queue.empty():
                                secured_message = self._secured_queue.get()
                                await self._send_secured(
                                    secured_message[0],
                                    secured_message[1],
                                    secured_message[2],
                                )

            if self.message_call_back is not None:
                if "LL" not in parsed_data and parsed_data != {}:
                    # pylint: disable=not-callable
                    await self.message_call_back(parsed_data)
            self._current_message_typ = None
            await asyncio.sleep(0)

    def _parse_loxone_message(self, message):
        """Parser of the Loxone message."""
        event_dict = {}
        if self._current_message_typ == 0:
            event_dict = message
        elif self._current_message_typ == 1:
            pass
        elif self._current_message_typ == 2:
            length = len(message)
            num = length / 24
            start = 0
            end = 24
            for _ in range(int(num)):
                packet = message[start:end]
                event_uuid = uuid.UUID(bytes_le=packet[0:16])
                fields = event_uuid.urn.replace("urn:uuid:", "").split("-")
                uuidstr = f"{fields[0]}-{fields[1]}-{fields[2]}-{fields[3]}{fields[4]}"
                value = unpack("d", packet[16:24])[0]
                event_dict[uuidstr] = value
                start += 24
                end += 24
        elif self._current_message_typ == 3:
            start = 0

            def get_text(message, start, offset):
                first = start
                second = start + offset
                event_uuid = uuid.UUID(bytes_le=message[first:second])
                first += offset
                second += offset

                icon_uuid_fields = event_uuid.urn.replace("urn:uuid:", "").split("-")
                uuidstr = "{}-{}-{}-{}{}".format(
                    icon_uuid_fields[0],
                    icon_uuid_fields[1],
                    icon_uuid_fields[2],
                    icon_uuid_fields[3],
                    icon_uuid_fields[4],
                )

                icon_uuid = uuid.UUID(bytes_le=message[first:second])
                icon_uuid_fields = icon_uuid.urn.replace("urn:uuid:", "").split("-")

                first = second
                second += 4

                text_length = unpack("<I", message[first:second])[0]

                first = second
                second = first + text_length
                message_str = unpack(f"{text_length}s", message[first:second])[0]
                start += (floor((4 + text_length + 16 + 16 - 1) / 4) + 1) * 4
                event_dict[uuidstr] = message_str.decode("utf-8")
                return start

            while start < len(message):
                start = get_text(message, start, 16)

        elif self._current_message_typ == 6:
            event_dict["keep_alive"] = "received"
        else:
            self._current_message_typ = 7
        return event_dict

    async def _use_token(self):
        token_hash = await self._hash_token()
        if token_hash is ERROR_VALUE:
            return ERROR_VALUE
        command = f"{CMD_AUTH_WITH_TOKEN}{token_hash}/{self._user}"
        enc_command = self._encrypt(command)
        await self._ws.send(enc_command)
        message = await self._ws.recv()
        self._unpack_loxone_message(message)
        message = await self._ws.recv()
        resp_json = json.loads(message)
        if "LL" in resp_json:
            if "code" in resp_json["LL"]:
                if resp_json["LL"]["code"] == "200":
                    if "value" in resp_json["LL"]:
                        self._token.valid_until = resp_json["LL"]["value"]["validUntil"]
                    return True
        return ERROR_VALUE

    async def _hash_token(self):
        try:
            command = f"{CMD_GET_KEY}"
            enc_command = self._encrypt(command)
            await self._ws.send(enc_command)
            message = await self._ws.recv()
            self._unpack_loxone_message(message)
            message = await self._ws.recv()
            resp_json = json.loads(message)
            if "LL" in resp_json:
                if "value" in resp_json["LL"]:
                    key = resp_json["LL"]["value"]
                    if key != "":
                        if self._token.hash_alg == "SHA1":
                            digester = HMAC.new(
                                binascii.unhexlify(key),
                                self._token.token.encode("utf-8"),
                                SHA1,
                            )
                        elif self._token.hash_alg == "SHA256":
                            digester = HMAC.new(
                                binascii.unhexlify(key),
                                self._token.token.encode("utf-8"),
                                SHA256,
                            )
                        else:
                            _LOGGER.error(
                                "Unrecognised hash algorithm: {}".format(
                                    self._token.hash_alg
                                )
                            )
                            return ERROR_VALUE

                        return digester.hexdigest()
            return ERROR_VALUE
        except:
            return ERROR_VALUE

    async def _acquire_token(self):
        _LOGGER.debug("acquire_token")
        command = f"{CMD_GET_KEY_AND_SALT}{self._user}"
        enc_command = self._encrypt(command)

        if not self._encryption_ready or self._ws is None:
            return ERROR_VALUE

        await self._ws.send(enc_command)
        message = await self._ws.recv()
        self._unpack_loxone_message(message)

        message = await self._ws.recv()

        key_and_salt = LxJsonKeySalt()
        key_and_salt.read_user_salt_response(message)

        new_hash = self._hash_credentials(key_and_salt)

        if self._version < 10.2:
            command = (
                "{}{}/{}/{}/edfc5f9a-df3f-4cad-9dddcdc42c732be2"
                "/pyloxone_api".format(
                    CMD_REQUEST_TOKEN, new_hash, self._user, TOKEN_PERMISSION
                )
            )
        else:
            command = (
                "{}{}/{}/{}/edfc5f9a-df3f-4cad-9dddcdc42c732be2"
                "/pyloxone_api".format(
                    CMD_REQUEST_TOKEN_JSON_WEB,
                    new_hash,
                    self._user,
                    TOKEN_PERMISSION,
                )
            )

        enc_command = self._encrypt(command)
        await self._ws.send(enc_command)
        message = await self._ws.recv()
        self._unpack_loxone_message(message)
        message = await self._ws.recv()

        resp_json = json.loads(message)
        if "LL" in resp_json:
            if "value" in resp_json["LL"]:
                if (
                    "token" in resp_json["LL"]["value"]
                    and "validUntil" in resp_json["LL"]["value"]
                ):
                    self._token.token = resp_json["LL"]["value"]["token"]
                    self._token.valid_until = resp_json["LL"]["value"]["validUntil"]
                    self._token.hash_alg = key_and_salt.hash_alg

        if self._token.save() == ERROR_VALUE:
            return ERROR_VALUE
        return True

    def _encrypt(self, command):
        if not self._encryption_ready:
            return command
        if self._salt != "" and self._new_salt_needed():
            prev_salt = self._salt
            self._salt = self._generate_salt()
            s = f"nextSalt/{prev_salt}/{self._salt}/{command}\x00"
        else:
            if self._salt == "":
                self._salt = self._generate_salt()
            s = f"salt/{self._salt}/{command}\x00"
        s = Padding.pad(bytes(s, "utf-8"), 16)
        try:
            _new_aes = AES.new(self._key, AES.MODE_CBC, self._iv)
            _LOGGER.debug("get_new_aes_cipher successfully...")
            result = _new_aes
        except ValueError:
            _LOGGER.debug("error get_new_aes_cipher...")
            result = None
        aes_cipher = result
        encrypted = aes_cipher.encrypt(s)
        encoded = b64encode(encrypted)
        encoded_url = req.pathname2url(encoded.decode("utf-8"))
        return CMD_ENCRYPT_CMD + encoded_url

    def _hash_credentials(self, key_salt):
        try:
            pwd_hash_str = f"{self._password}:{key_salt.salt}"
            if key_salt.hash_alg == "SHA1":
                m = hashlib.sha1()
            elif key_salt.hash_alg == "SHA256":
                m = hashlib.sha256()
            else:
                _LOGGER.error(
                    "Unrecognised hash algorithm: {}".format(key_salt.hash_alg)
                )
                return None

            m.update(pwd_hash_str.encode("utf-8"))
            pwd_hash = m.hexdigest().upper()
            pwd_hash = f"{self._user}:{pwd_hash}"

            if key_salt.hash_alg == "SHA1":
                digester = HMAC.new(
                    binascii.unhexlify(key_salt.key), pwd_hash.encode("utf-8"), SHA1
                )
            elif key_salt.hash_alg == "SHA256":
                digester = HMAC.new(
                    binascii.unhexlify(key_salt.key), pwd_hash.encode("utf-8"), SHA256
                )
            _LOGGER.debug("hash_credentials successfully...")
            return digester.hexdigest()
        except ValueError:
            _LOGGER.debug("error hash_credentials...")
            return None

    def _generate_salt(self):
        salt = get_random_bytes(SALT_BYTES)
        salt = binascii.hexlify(salt).decode("utf-8")
        salt = req.pathname2url(salt)
        self._salt_time_stamp = time_elapsed_in_seconds()
        self._salt_used_count = 0
        return salt

    def _new_salt_needed(self):
        self._salt_used_count += 1
        if (
            self._salt_used_count > SALT_MAX_USE_COUNT
            or time_elapsed_in_seconds() - self._salt_time_stamp > SALT_MAX_AGE_SECONDS
        ):
            return True
        return False

    def _unpack_loxone_message(self, message):
        if len(message) == 8:
            try:
                unpacked_data = unpack("ccccI", message)
                self._current_message_typ = int.from_bytes(
                    unpacked_data[1], byteorder="big"
                )
                _LOGGER.debug("unpack_message successfully...")
            except ValueError:
                _LOGGER.debug("error unpack_message...")

    async def _get_public_key(self):
        command = f"{self._url}/{CMD_GET_PUBLIC_KEY}"
        _LOGGER.debug(f"try to get public key: {command}")

        try:
            async with httpx.AsyncClient(
                auth=(self._user, self._password), timeout=TIMEOUT
            ) as client:
                response = await client.get(command)
        except:
            return False

        if response.status_code != 200:
            _LOGGER.debug(f"error get_public_key: {response.status_code}")
            return False
        try:
            resp_json = json.loads(response.text)
            if "LL" in resp_json and "value" in resp_json["LL"]:
                self._public_key = resp_json["LL"]["value"]
                _LOGGER.debug("get_public_key successfully...")
            else:
                _LOGGER.debug("public key load error")
                return False
        except ValueError:
            _LOGGER.debug("public key load error")
            return False
        return True


# Loxone Stuff


def time_elapsed_in_seconds():
    return int(round(time.time()))


class LxJsonKeySalt:
    def __init__(self):
        self.key = None
        self.salt = None
        self.response = None
        self.time_elapsed_in_seconds = None
        self.hash_alg = None

    def read_user_salt_response(self, response):
        js = json.loads(response, strict=False)
        value = js["LL"]["value"]
        self.key = value["key"]
        self.salt = value["salt"]
        self.hash_alg = value.get("hashAlg", "SHA1")
