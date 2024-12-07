from dataclasses import dataclass

import directions


@dataclass
class Guard:
    pos_x: int
    pos_y: int
    visited_fields: list[(int, int)]
    view_direction: str

    def __init__(self, x: int, y: int):
        self.pos_x = x
        self.pos_y = y
        self.visited_fields = [(self.pos_x, self.pos_y)]
        self.view_direction = directions.UPWARDS
