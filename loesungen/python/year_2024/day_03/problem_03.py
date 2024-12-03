import re

from advent_of_code.loesungen.python.utils import input_processing as ip

filename = "C:/_Python/advent_of_code/advent_of_code/input/2024_03_real.txt"
test_command = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

find_mul_regex = "mul\([1-9]\d{0,2},[1-9]\d{0,2}\)"
regex_find_all_mul_do_donts = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

def read_input() -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(filename)

def find_all_multiplications(commands: list[str]) -> list[str]:
    multiplications = []
    for command in commands:
        matches = re.findall(find_mul_regex, command)
        for m in matches:
            multiplications.append(m)
    return multiplications

def sum_all_valid_multiplications(multiplications: list[str]) -> int:
    sum_of_products = 0
    for multiplication in multiplications:
        multiplication = multiplication.removeprefix("mul(")
        multiplication = multiplication.removesuffix(")")
        factors = multiplication.split(",")
        sum_of_products += int(factors[0]) * int(factors[1])
    return sum_of_products

def solve_part_1(commands: list[str]) -> int:
    multiplications = find_all_multiplications(commands)
    sum_of_products = sum_all_valid_multiplications(multiplications)

    return sum_of_products


def solve_part_2(commands: list[str]) -> int:
    multiplication_enabled = True
    multiplications: list[str] = []

    for command in commands:
        all_matches: list[str] = re.findall(regex_find_all_mul_do_donts, command)

        for m in all_matches:
            if m.startswith("do"):
                if m.startswith("don't"):
                    multiplication_enabled = False
                else:
                    multiplication_enabled = True
            if m.startswith("mul") and multiplication_enabled:
                multiplications.append(m)

    sum_of_multiplications = sum_all_valid_multiplications(multiplications)

    return sum_of_multiplications


def main():
    commands = read_input()

    solution_part_1 = solve_part_1(commands)
    print(f"Part 1: Sum of all multiplications is {solution_part_1}.")

    solution_part_2 = solve_part_2(commands)
    print(f"Part 2: Sum of all valid multiplications is {solution_part_2}.")

if __name__ == "__main__":
    main()
