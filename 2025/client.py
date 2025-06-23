import socket
from enum import Enum, auto


class ClientStatus(Enum):
    SUCCESS = auto()
    NOT_CONNECTED = auto()
    CONNECTION_ERROR = auto()
    SEND_ERROR = auto()
    RECEIVE_ERROR = auto()


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False


    def connect(self, ip: str, port: int) -> ClientStatus:
        try:
            self.sock.connect((ip, port))
            self.connected = True

            return ClientStatus.SUCCESS
        except socket.error:
            self.connected = False

            return ClientStatus.CONNECTION_ERROR

    
    def disconnect(self) -> ClientStatus:
        if self.connected:
            try:
                self.sock.close()
                self.connected = False

                return ClientStatus.SUCCESS
            except socket.error:
                return ClientStatus.CONNECTION_ERROR
        
        return ClientStatus.NOT_CONNECTED


    def send(self, data: str) -> ClientStatus:
        if not self.connected:
            return ClientStatus.NOT_CONNECTED
        try:
            self.sock.sendall(data.encode('utf-8'))

            return ClientStatus.SUCCESS
        except socket.error:
             return ClientStatus.SEND_ERROR


    def receive(self, out_data: list, buffer_size: int = 1024) -> ClientStatus:
        if not self.connected:
            return ClientStatus.NOT_CONNECTED
        try:
            received = self.sock.recv(buffer_size)
            out_data.clear()
            out_data.append(received.decode('utf-8'))

            return ClientStatus.SUCCESS
        except socket.error:
            return ClientStatus.RECEIVE_ERROR
