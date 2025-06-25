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
        self.last_send_status = ConnectionStatus.NONE
        self.last_receive_status = ConnectionStatus.NONE


    def connect(self, ip: str, port: int):
        self.last_connection_status = self.client.connect(ip, port)
        return self.client.connected


    def disconnect(self):
        cmd = CommandMessageManager.build_command(RobotCommand.EXIT)
        self.last_send_status = self.client.send(cmd)
        
        self.last_connection_status = self.client.disconnect()
        
        return not self.client.connected


    def get_pos(self):
        cmd = CommandMessageManager.build_command(RobotCommand.GET_POSITION)
        self.last_send_status = self.client.send(cmd)

        ans = []
        self.last_receive_status = self.client.receive(ans)

        return ans


    def move_axis(self,
                  move_info: Tuple[Literal["cartesian", "joint"], int, str],
                  step: float):
        mode, axis_index, direction = move_info

        signed_step = step if direction == '+' else -step
        pos = self.robot.calculate_next_move(mode, axis_index, signed_step)

        cmd = CommandMessageManager.build_command(MODE_TO_COMMAND[mode], pos)
        self.last_send_status = self.client.send(cmd)

        ans = []
        self.last_receive_status = self.client.receive(ans)

        return ans
