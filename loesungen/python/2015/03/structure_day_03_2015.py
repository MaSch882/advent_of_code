from dataclasses import dataclass


@dataclass()
class Santa:
    pos_x: int
    pos_y: int
    houses_visited: list[(int, int)]

    def move_north(self):
        self.pos_y += 1

    def move_south(self):
        self.pos_y -= 1

    def move_east(self):
        self.pos_x += 1

    def move_west(self):
        self.pos_x -= 1

    def performing_one_elf_instruction(self, direction: str) -> None:
        if direction == '^':
            self.move_north()
        if direction == 'v':
            self.move_south()
        if direction == '>':
            self.move_east()
        if direction == '<':
            self.move_west()

    def update_houses_visited(self):
        coordinates = (self.pos_x, self.pos_y)
        if coordinates not in self.houses_visited:
            self.houses_visited.append(coordinates)
