def read_instruction(filename: str) -> str:
    with open(filename) as file:
        for line in file:
            return str(line)


def calculate_floor(instruction: str):
    floor = 0
    for command in instruction:
        if command == '(':
            floor += 1
        if command == ')':
            floor -= 1
    return floor


def calculate_first_basement_floor(instruction: str):
    floor = 0
    for index, command in enumerate(instruction):
        if command == '(':
            floor += 1
        if command == ')':
            floor -= 1
        if floor < 0:
            return index + 1
    return -1


def main():
    instruction = read_instruction("../input_data/01_12_problem_data.txt")
    floor_at_the_end = calculate_floor(instruction)
    first_basement_floor = calculate_first_basement_floor(instruction)
    print(f'At the end of the instruction, Santa stands in floor {floor_at_the_end}.')
    print(f'The first time, Santa enters the basement is after {first_basement_floor} steps.')


if __name__ == '__main__':
    main()
