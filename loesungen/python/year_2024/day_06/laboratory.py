from dataclasses import dataclass

import directions
from guard import Guard


@dataclass
class Laboratory:
    fields: list[str]
    guard: Guard
    guard_symbol: str
    obstruction_symbol: str
    guard_is_inside: bool

    def __init__(self, fields: list[str]):
        self.fields = fields
        self.guard_symbol = "^"
        self.obstruction_symbol = "#"
        self.guard = self.initialize_guard()
        self.guard_is_inside = True

    def initialize_guard(self) -> (int, int):
        for y in range(len(self.fields)):
            for x in range(len(self.fields[0])):
                if self.fields[y][x] == self.guard_symbol:
                    return Guard(x, y)
        raise ValueError("No guard found!")

    def simulate_next_step(self) -> None:
        if self.is_guard_facing_an_obstruction():
            self.update_guard_view_direction()
        else:
            self.update_guard_position()

    def is_guard_facing_an_obstruction(self) -> bool:
        pos_x = self.guard.pos_x
        pos_y = self.guard.pos_y

        next_x = pos_x
        next_y = pos_y

        match self.guard.view_direction:
            case directions.UPWARDS:
                next_y = pos_y - 1
            case directions.DOWNWARDS:
                next_y = pos_y + 1
            case directions.LEFT:
                next_x = pos_x - 1
            case directions.RIGHT:
                next_x = pos_x + 1

        if next_x < 0 or next_y < 0:
            # In this case, we left the field on the top or left.
            self.guard_is_inside = False
            return False

        if next_x >= len(self.fields[0]) or next_y >= len(self.fields):
            # In this case, we left the field on the bottom or right.
            self.guard_is_inside = False
            return False

        if self.fields[next_y][next_x] == self.obstruction_symbol:
            return True
        else:
            return False

    def update_guard_view_direction(self) -> None:
        match self.guard.view_direction:
            case directions.UPWARDS:
                self.guard.view_direction = directions.RIGHT
            case directions.RIGHT:
                self.guard.view_direction = directions.DOWNWARDS
            case directions.DOWNWARDS:
                self.guard.view_direction = directions.LEFT
            case directions.LEFT:
                self.guard.view_direction = directions.UPWARDS

    def update_guard_position(self):
        guard_position = self.guard.pos_x, self.guard.pos_y
        if guard_position not in self.guard.visited_fields:
            self.guard.visited_fields.append(guard_position)

        next_x = self.guard.pos_x
        next_y = self.guard.pos_y
        match self.guard.view_direction:
            case directions.UPWARDS:
                next_y -= 1
            case directions.DOWNWARDS:
                next_y += 1
            case directions.RIGHT:
                next_x += 1
            case directions.LEFT:
                next_x -= 1

        if next_x < 0 or next_y < 0:
            # In this case, we left the field on the top or left.
            self.guard_is_inside = False
            return

        if next_x >= len(self.fields[0]) or next_y >= len(self.fields):
            # In this case, we left the field on the bottom or right.
            self.guard_is_inside = False
            return

        self.guard.pos_x = next_x
        self.guard.pos_y = next_y
