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


    def connect(self, ip: str, port: int):
        try:
            self.sock.connect((ip, port))
            self.connected = True

            return ClientStatus.SUCCESS
        except socket.error as e:
            self.connected = False

            return ClientStatus.CONNECTION_ERROR

    
    def disconnect(self):
        if self.connected:
            try:
                self.sock.close()
                self.connected = False

                return ClientStatus.SUCCESS
            except socket.error:
                return ClientStatus.CONNECTION_ERROR
        
        return ClientStatus.NOT_CONNECTED


    def send(self, data: str):
        if not self.connected:
            return ClientStatus.NOT_CONNECTED
        try:
            self.sock.sendall(data.encode('utf-8'))

            return ClientStatus.SUCCESS
        except socket.error as e:
             return ClientStatus.SEND_ERROR

    
    def receive(self, buffer_size: int = 1024) -> str:
        if not self.connected:
            return ClientStatus.NOT_CONNECTED, ''
        try:
            received = self.sock.recv(buffer_size)
            data = received.decode('utf-8')
            
            return ClientStatus.SUCCESS, data
        except socket.error as e:
            return ClientStatus.RECEIVE_ERROR, ''