from enum import Enum


class RobotCommand(Enum):
    EXIT = 0
    GET_POSITION = 1
    MOVE_LINEAR = 2
    MOVE_JOINTS = 3


MODE_TO_COMMAND = {
    "cartesian": RobotCommand.MOVE_LINEAR,
    "joint": RobotCommand.MOVE_JOINTS,
}