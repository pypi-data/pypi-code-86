from typing import Optional, Union, List, Dict, Iterable

import select
import socket
import time
import pickle as pkl

import torch.jit

from .configs import Config
from ..utils import logger

from .socket_connection import SocketConnection


class ServerSocket(SocketConnection):
    def read_buffer(self) -> Optional[bytes]:
        response = bytes()
        while True:
            buffer = self.connection.recv(self.message_size)
            if not buffer:
                raise ConnectionError('No response, other side probably died')
            response += buffer
            if response.startswith(Config.request_cancelled):
                return None
            if response.endswith(self.delimiter):
                return response.split(self.delimiter)[-2]

    def receive_message(self):
        try:
            response = self.connection.recv(self.message_size)
            if not response:
                raise ConnectionError('No response, other side probably died')
        except ConnectionError:
            self.alive = False
            raise
        active_request = response.endswith(Config.request_signal)
        if active_request:
            self.connection.send(Config.request_signal)
            response = self.read_buffer()
            if response is None:
                return None
            return response[:Config.message_id_len], pkl.loads(response[Config.message_id_len:])


class SessionState:
    def __init__(self, connection: SocketConnection, message_id: bytes, inputs: dict):
        self.connection = connection
        self.message_id = message_id
        self.inputs = inputs

    def send_output(self, output):
        try:
            self.connection.send_message(self.message_id, output)
        except ConnectionError:
            pass

    def send_error(self, e: Exception):
        try:
            self.connection.send_error(self.message_id, str(e))
        except ConnectionError:
            pass


class ModelServer:
    def __init__(self, port: int, model: torch.nn.Module, model_name: str):
        logger.info('Server starting')
        self.model = model
        self.device = next(self.model.parameters()).device
        self.server_socket = self.create_server_socket(port)
        logger.info(f'{model_name} model server started on port {port}')

    @staticmethod
    def create_server_socket(port: int) -> socket.socket:
        server_socket = socket.socket()
        while True:
            try:
                server_socket.bind((Config.host, port))
                break
            except OSError:
                time.sleep(5)
        server_socket.listen(10)
        return server_socket

    def close(self):
        self.server_socket.close()

    @staticmethod
    def pad_and_concat(tensors: List[torch.Tensor], pad: int = 0) -> torch.Tensor:
        sample_tensor = tensors[0]
        if len(tensors) == 1:
            return sample_tensor

        max_len = max([tensor.shape[1] for tensor in tensors])

        total_batch_size = 0
        for tensor in tensors:
            total_batch_size += tensor.shape[0]
        output_tensor = torch.empty((total_batch_size, max_len) + sample_tensor.shape[2:],
                                    dtype=sample_tensor.dtype, device=sample_tensor.device).fill_(pad)
        cur_ind = 0
        for tensor in tensors:
            new_ind = cur_ind + tensor.shape[0]
            output_tensor[cur_ind: new_ind, :tensor.shape[1]] = tensor
            cur_ind = new_ind

        return output_tensor

    @staticmethod
    def split_tensor_output(outputs: torch.Tensor, sizes: List[int]) -> Iterable[torch.Tensor]:
        outputs = outputs.detach().to('cpu')
        last_ind = 0
        for size in sizes:
            new_ind = last_ind + size
            yield outputs[last_ind: new_ind]
            last_ind = new_ind

    @staticmethod
    def split_dict_output(
            outputs: Dict[str, Union[list, torch.Tensor]], sizes: List[int]
    ) -> Iterable[Dict[str, Union[list, torch.Tensor]]]:
        outputs = {
            key: value.detach().to('cpu') if isinstance(value, torch.Tensor) else value
            for key, value in outputs.items()
        }
        last_ind = 0
        for size in sizes:
            new_ind = last_ind + size
            yield {key: value[last_ind: new_ind] for key, value in outputs.items()}
            last_ind = new_ind

    def split_output(self, outputs, sizes: List[int]) -> Iterable:
        return (self.split_tensor_output(outputs, sizes) if isinstance(outputs, torch.Tensor)
                else self.split_dict_output(outputs, sizes))

    def run(self):
        connections: List[Union[SocketConnection, socket.socket]] = []

        while True:
            connections = [connection for connection in connections if connection.alive]

            logger.info('Waiting for connections')
            new_connections = select.select(connections + [self.server_socket], [], [], None)[0]
            logger.info('Connection received')

            if self.server_socket in new_connections:
                connection, address = self.server_socket.accept()
                connection = ServerSocket(connection, Config.server_message_size)
                logger.debug(f'Added connection, fileno: {connection.fileno()}')
                connections.append(connection)
                continue

            session_states: List[SessionState] = []
            for connection in new_connections:
                try:
                    inputs = connection.receive_message()
                except ConnectionError:
                    logger.debug('ConnectionError')
                    continue
                if not inputs:
                    logger.debug('Empty')
                    continue
                message_id, input_dict = inputs
                session_states.append(SessionState(connection, message_id, input_dict))
                logger.debug('Processed new inputs')

            if not session_states:
                continue

            inputs = [session_state.inputs for session_state in session_states]
            pad_map: Dict[str, int] = getattr(self.model, 'pad_map', {})

            try:
                keys = list(inputs[0].keys())
                sizes = [sample_inputs[keys[0]].shape[0] for sample_inputs in inputs]
                inputs = {
                    key: self.pad_and_concat(
                        [sample_inputs[key].to(self.device) for sample_inputs in inputs], pad_map.get(key, 0))
                    for key in keys
                }
                with torch.no_grad():
                    outputs = self.model.forward(**inputs)
                logger.debug('Sending outputs')
                for session_state, output in zip(session_states, self.split_output(outputs, sizes)):
                    session_state.send_output(output)
            except Exception as e:
                logger.exception(e)
                for session_state in session_states:
                    session_state.send_error(e)
