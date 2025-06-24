from typing import List, Literal


class VirtualRobot:
    def __init__(self,
                 cartesian: List[float] = None,
                 joint: List[float] = None):
        self.cartesian = cartesian if cartesian is not None else [0.0] * 6
        self.joint = joint if joint is not None else [0.0] * 6


    def update_cartesian(self, new_values: List[float]):
        if len(new_values) != 6:
            raise ValueError("Cartesian must have 6 values")
        self.cartesian = new_values.copy()


    def update_joint(self, new_values: List[float]):
        if len(new_values) != 6:
            raise ValueError("Joint must have 6 values")
        self.joint = new_values.copy()


    def calculate_next_move(
        self,
        mode: Literal["cartesian", "joint"],
        axis_index: int,
        step: float
    ) -> List[float]:
        if not (0 <= axis_index < 6):
            raise ValueError("Value of axis_index must be in range from 0 to 5")

        if mode == "cartesian":
            new_pos = self.cartesian.copy()
        elif mode == "joint":
            new_pos = self.joint.copy()
        else:
            raise ValueError("Expected 'cartesian' or 'joint' mode")

        new_pos[axis_index] += step
        return new_pos


    def calculate_composite_move(
            self,
            mode: Literal["cartesian", "joint"],
            deltas: List[float]
    ) -> List[float]:
        if len(deltas) != 6:
            raise ValueError("Value of deltas must contain 6 values")

        if mode == "cartesian":
            base = self.cartesian
        elif mode == "joint":
            base = self.joint
        else:
            raise ValueError("Expected 'cartesian' or 'joint' mode")

        return [base[i] + deltas[i] for i in range(6)]

