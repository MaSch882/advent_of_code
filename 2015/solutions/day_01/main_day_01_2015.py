from Utils import input_processing
from structure_day_01_2015 import FloorCalculator

filename = r"..\..\input_data/input_day_01_2015.txt"


def main():
    instruction = read_input()

    print_solution_part_1(instruction)  # 232
    print_solution_part_2(instruction)  # 1783


def print_solution_part_1(instruction: str):
    floor_at_the_end = FloorCalculator.calculate_floor(instruction)
    print(f'At the end of the instruction, Santa stands in floor {floor_at_the_end}.')


def print_solution_part_2(instruction: str):
    first_basement_floor = FloorCalculator.calculate_first_basement_floor(instruction)
    print(f'The first time, Santa enters the basement is after {first_basement_floor} steps.')


def read_input() -> str:
    return input_processing.read_input(filename)[0]


if __name__ == '__main__':
    main()
