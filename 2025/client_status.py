from enum import Enum, auto


class ClientStatus(Enum):
    SUCCESS = auto()
    NOT_CONNECTED = auto()
    CONNECTION_ERROR = auto()
    SEND_ERROR = auto()
    RECEIVE_ERROR = auto()