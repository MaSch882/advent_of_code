from dataclasses import dataclass

import Utils.input_processing as ip


def read_input(filename: str) -> str:
    list_of_strings = ip.read_input_list(filename)
    list_of_strings = ip.trim_newlines(list_of_strings)
    return list_of_strings[0]


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


# Problem 1


def execute_delivery_route(santa: Santa, route: str) -> None:
    for instruction in route:
        santa.performing_one_elf_instruction(instruction)
        santa.update_houses_visited()


def count_visited_houses(santa: Santa) -> int:
    return len(santa.houses_visited)


# Problem 2


def execute_alternating_delivery_route(santa: Santa, robot_santa: Santa, route: str) -> None:
    for i, instruction in enumerate(route):
        if i % 2 == 0:
            santa.performing_one_elf_instruction(instruction)
            santa.update_houses_visited()
        else:
            robot_santa.performing_one_elf_instruction(instruction)
            robot_santa.update_houses_visited()


def count_combined_visited_houses(santa: Santa, robot_santa: Santa) -> int:
    houses_visited_by_santa = santa.houses_visited
    houses_visited_by_robot_santa = robot_santa.houses_visited
    houses_visited = houses_visited_by_santa + houses_visited_by_robot_santa
    unique_houses_visited = set(houses_visited)
    return len(unique_houses_visited)


def main():
    santa = Santa(0, 0, [(0, 0)])
    elves_instructions = read_input("../input_data/03_12_problem_data.txt")

    execute_delivery_route(santa, elves_instructions)
    number_of_houses_visited = count_visited_houses(santa)
    print(f'The number of houses which receive at least one present from Santa is {number_of_houses_visited}.')

    santa = Santa(0, 0, [(0, 0)])
    robot_santa = Santa(0, 0, [(0, 0)])
    execute_alternating_delivery_route(santa, robot_santa, elves_instructions)
    number_of_unique_houses_visited = count_combined_visited_houses(santa, robot_santa)
    print(
        f'The number of houses which receive at least one present from Santa or Robot Santa is {number_of_unique_houses_visited}.')

    pass


if __name__ == "__main__":
    main()
