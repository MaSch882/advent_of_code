class Walker:
    x_position: int
    y_position: int
    orientation: str
    visited_locations: list[(int, int)]
    first_visited_twice: (int, int)

    def __init__(self, x: int, y: int):
        self.x_position = x
        self.y_position = y
        self.orientation = "N"
        self.visited_locations = [(0, 0)]
        self.first_visited_twice = None

    def turn_right(self):
        if self.orientation == "N":
            self.orientation = "O"
            return
        if self.orientation == "O":
            self.orientation = "S"
            return
        if self.orientation == "S":
            self.orientation = "W"
            return
        if self.orientation == "W":
            self.orientation = "N"

    def turn_left(self):
        if self.orientation == "N":
            self.orientation = "W"
            return
        if self.orientation == "W":
            self.orientation = "S"
            return
        if self.orientation == "S":
            self.orientation = "O"
            return
        if self.orientation == "O":
            self.orientation = "N"

    def walk(self, steps: int):
        if self.orientation == "N":
            for i in range(1, steps + 1):
                self.y_position += 1
                self.update_visited_positions()
        if self.orientation == "W":
            for i in range(1, steps + 1):
                self.x_position -= 1
                self.update_visited_positions()
        if self.orientation == "S":
            for i in range(1, steps + 1):
                self.y_position -= 1
                self.update_visited_positions()
        if self.orientation == "O":
            for i in range(1, steps + 1):
                self.x_position += 1
                self.update_visited_positions()

    def update_visited_positions(self):
        new_position = (self.x_position, self.y_position)
        self.visited_locations.append(new_position)
        if self.first_visited_twice is None and self.visited_locations.count(new_position) > 1:
            self.first_visited_twice = new_position

    def process_walk_command(self, command: str):
        direction = command[0]
        steps = int(command[1:])

        if direction == "L":
            self.turn_left()
        if direction == "R":
            self.turn_right()

        self.walk(steps)

    def is_last_visited_location_visited_more_than_once(self):
        return self.visited_locations.count(self.visited_locations[-1]) > 1

    @staticmethod
    def calculate_manhattan_distance_to_origin(x_pos: int, y_pos: int) -> int:
        return abs(x_pos) + abs(y_pos)
