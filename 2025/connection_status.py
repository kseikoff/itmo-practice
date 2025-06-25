from enum import Enum, auto


class ConnectionStatus(Enum):
    SUCCESS = auto()
    NOT_CONNECTED = auto()
    CONNECTION_ERROR = auto()
    SEND_ERROR = auto()
    RECEIVE_ERROR = auto()
    NONE = auto()