from loesungen.python.utils.input_processing import InputReader
from structure_day_01_2016 import Walker

filename = r"..\..\..\..\input_data/2016/2016_01.txt"


def main():
    commands = extract_commands_from_input()

    print_solution_part_1(commands)  # 291
    print_solution_part_2(commands)  # 159


def extract_commands_from_input() -> list[str]:
    raw_command = InputReader.read_input(filename)
    raw_commands = raw_command[0].split()
    return [x.replace(",", "") for x in raw_commands]


def print_solution_part_1(commands: list[str]):
    walker = Walker(0, 0)

    for command in commands:
        walker.process_walk_command(command)

    distance = walker.calculate_manhattan_distance_to_origin(walker.x_position, walker.y_position)

    print(f"Easter Bunny HQ is {distance} blocks away.")


def print_solution_part_2(commands: list[str]):
    walker = Walker(0, 0)

    for command in commands:
        walker.process_walk_command(command)

    first_visited_twice = walker.first_visited_twice
    distance = walker.calculate_manhattan_distance_to_origin(first_visited_twice[0], first_visited_twice[1])

    print(f"The first block visited twice is {distance} blocks away.")


if __name__ == "__main__":
    main()
