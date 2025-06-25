from typing import Tuple, Literal

from virtual_robot import VirtualRobot
from command_manager import CommandMessageManager
from robot_command import RobotCommand, MODE_TO_COMMAND
from client import Client
from connection_status import ConnectionStatus


class BackendController:
    def __init__(self):
        self.robot = VirtualRobot()
        self.client = Client()
        self.last_connection_status = ConnectionStatus.NONE
        self.last_cmd_send_status = ConnectionStatus.NONE
        self.last_params_send_status = ConnectionStatus.NONE
        self.last_receive_status = ConnectionStatus.NONE


    def connect(self, ip: str, port: int):
        self.last_connection_status = self.client.connect(ip, port)
        return self.client.connected


    def disconnect(self):
        cmd = str(RobotCommand.EXIT.value)
        self.last_cmd_send_status = self.client.send(cmd)
        
        self.last_connection_status = self.client.disconnect()
        
        return not self.client.connected


    def is_connected(self):
        return self.client.connected


    def get_pos(self):
        cmd = str(RobotCommand.GET_POSITION.value)
        self.last_cmd_send_status = self.client.send(cmd)

        ans = []
        self.last_receive_status = self.client.receive(ans)

        return ans


    def move_axis(self,
                  move_info: Tuple[Literal["cartesian_linear", "cartesian_rotation", "joint_rotation"], int, Literal['+', '-']],
                  step: float):
        mode, axis_index, direction = move_info

        signed_step = step if direction == '+' else -step
        pos = self.robot.calculate_next_move(mode, axis_index, signed_step)

        cmd = str(MODE_TO_COMMAND[mode].value)

        params = CommandMessageManager.build_position_request(pos)
        if "cartesian" in mode:
            params = f"{params}({','.join(map(str, self.robot.kinematic_sol))})"

        self.last_cmd_send_status = self.client.send(cmd)
        self.last_params_send_status = self.client.send(params)

        ans = []
        self.last_receive_status = self.client.receive(ans)

        return ans
