from framework.input_processing import InputReader
from structure_day_03_2015 import Santa

filename = r"..\..\input_data/input_day_03_2015.txt"


def main():
    elves_instructions = InputReader.read_input(filename)[0]

    print_solution_part_1(elves_instructions)  # 2565
    print_solution_part_2(elves_instructions)  # 2639


def print_solution_part_1(elves_instructions: str):
    santa = Santa(0, 0, [(0, 0)])

    execute_delivery_route(santa, elves_instructions)
    number_of_houses_visited = count_visited_houses(santa)
    print(f'The number of houses which receive at least one present from Santa is {number_of_houses_visited}.')


def execute_delivery_route(santa: Santa, route: str) -> None:
    for instruction in route:
        santa.performing_one_elf_instruction(instruction)
        santa.update_houses_visited()


def count_visited_houses(santa: Santa) -> int:
    return len(santa.houses_visited)


def print_solution_part_2(elves_instructions: str):
    santa = Santa(0, 0, [(0, 0)])
    robot_santa = Santa(0, 0, [(0, 0)])

    execute_alternating_delivery_route(santa, robot_santa, elves_instructions)
    number_of_unique_houses_visited = count_combined_visited_houses(santa, robot_santa)
    print(
        f'The number of houses which receive at least one present from Santa or Robot Santa is '
        f'{number_of_unique_houses_visited}.')


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


def read_input() -> str:
    return input_processing.read_input(filename)[0]


if __name__ == '__main__':
    main()
