from dataclasses import dataclass

import Utils.input_processing as ip


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

    def execute_delivery_route(self, route: str):
        for instruction in route:
            self.performing_one_elf_instruction(instruction)
            self.update_houses_visited()

    def count_visited_houses(self):
        return len(self.houses_visited)


def read_input(filename: str) -> str:
    list_of_strings = ip.read_input_list(filename)
    list_of_strings = ip.trim_newlines(list_of_strings)
    return list_of_strings[0]


def main():
    santa = Santa(0, 0, [(0, 0)])
    elves_instructions = read_input("../input_data/03_12_problem_data.txt")

    santa.execute_delivery_route(elves_instructions)
    number_of_houses_visited = santa.count_visited_houses()
    print(f'The number of houses which receive at least one present is {number_of_houses_visited}.')
    
    pass


if __name__ == "__main__":
    main()
