import socket

import connection_status as cs


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False


    def connect(self, ip: str, port: int) -> cs.ConnectionStatus:
        try:
            self.sock.connect((ip, port))
            self.connected = True

            return cs.ConnectionStatus.SUCCESS
        except socket.error:
            self.connected = False

            return cs.ConnectionStatus.CONNECTION_ERROR

    
    def disconnect(self) -> cs.ConnectionStatus:
        if self.connected:
            try:
                self.sock.close()
                self.connected = False

                return cs.ConnectionStatus.SUCCESS
            except socket.error:
                return cs.ConnectionStatus.CONNECTION_ERROR
        
        return cs.ConnectionStatus.NOT_CONNECTED


    def send(self, data: str) -> cs.ConnectionStatus:
        if not self.connected:
            return cs.ConnectionStatus.NOT_CONNECTED
        try:
            self.sock.sendall(data.encode('utf-8'))

            return cs.ConnectionStatus.SUCCESS
        except socket.error:
             return cs.ConnectionStatus.SEND_ERROR


    def receive(self, out_data: list, buffer_size: int = 1024) -> cs.ConnectionStatus:
        if not self.connected:
            return cs.ConnectionStatus.NOT_CONNECTED
        try:
            received = self.sock.recv(buffer_size)
            out_data.clear()
            out_data.append(received.decode('utf-8'))

            return cs.ConnectionStatus.SUCCESS
        except socket.error:
            return cs.ConnectionStatus.RECEIVE_ERROR
