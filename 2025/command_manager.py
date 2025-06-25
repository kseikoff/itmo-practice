from typing import List
import re


class CommandMessageManager:
    @staticmethod
    def build_position_request(pos: List[float]) -> str:
        if len(pos) != 6:
            raise ValueError('List of pos must contain 6 values')

        return f"({','.join(map(str, pos))})"


    @staticmethod
    def parse_position_response(response: list):
        try:
            matches = re.findall(r'\((.*?)\)', response[0])
            lists = [list(map(float, group.split(','))) for group in matches[:2]]
            lists.append(list(map(int, matches[2].split(','))))

            return tuple(lists)
        except ValueError:
            return None
