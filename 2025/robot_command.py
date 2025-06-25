from enum import Enum


class RobotCommand(Enum):
    EXIT = 0
    GET_POSITION = 1
    MOVE_LINEAR = 2
    MOVE_JOINTS = 3


MODE_TO_COMMAND = {
    "cartesian_linear": RobotCommand.MOVE_LINEAR,
    "cartesian_rotation": RobotCommand.MOVE_LINEAR,
    "joint_rotation": RobotCommand.MOVE_JOINTS,
}