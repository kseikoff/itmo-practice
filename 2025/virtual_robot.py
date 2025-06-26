from typing import List, Literal, Tuple


class VirtualRobot:
    def __init__(self,
                 cartesian: List[float] = None,
                 joint: List[float] = None):
        self.cartesian = cartesian if cartesian is not None else [0.0] * 6
        self.joint = joint if joint is not None else [0.0] * 6
        self.kinematic_sol = (0, 0)


    def update_cartesian(self, new_values: List[float], kinematic_sol: Tuple[int, int]):
        if len(new_values) != 6:
            raise ValueError("Cartesian must have 6 values")
        self.cartesian = new_values.copy()
        self.kinematic_sol = kinematic_sol


    def update_joint(self, new_values: List[float]):
        if len(new_values) != 6:
            raise ValueError("Joint must have 6 values")
        self.joint = new_values.copy()


    def calculate_next_move(
        self,
        mode: Literal["cartesian_linear", "cartesian_rotation", "joint_rotation"],
        axis_index: int,
        step: float
    ) -> List[float]:
        if not (0 <= axis_index < 6):
            raise ValueError("Value of axis_index must be in range from 0 to 5")

        if "cartesian" in mode:
            new_pos = self.cartesian.copy()
        elif "joint" in mode:
            new_pos = self.joint.copy()
        else:
            raise ValueError("Expected 'cartesian' or 'joint' mode")

        new_pos[axis_index] += step
        return new_pos
