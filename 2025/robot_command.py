from enum import Enum


class RobotCommand(Enum):
    EXIT = 0
    GET_POSITION = 1
    MOVE_LINE = 2
    MOVE_JOINTS = 3