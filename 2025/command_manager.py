from typing import List, Optional

import robot_command as rc


class CommandMessageManager:
    @staticmethod
    def build_command(cmd: rc.RobotCommand, params: Optional[List[float]] = None) -> str:
        if params is None:
            params = []

        param_str = ' '.join(f"{p:.4f}" for p in params)
        return f"{cmd.value} {param_str}".strip()


    @staticmethod
    def parse_position_response(response: str) -> Optional[List[float]]:
        try:
            return [float(x) for x in response.strip().split()]
        except ValueError:
            return None
