from loesungen.python.utils import input_processing as ip
from loesungen.python.year_2024.day_07.calibration_equation import CalibrationEquation

filename = "H:/git_repos/advent_of_code/2024/07_real.txt"


# INPUT

def read_input(f: str) -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(f)


def build_calibration_equations(raw_input: list[str]) -> list[CalibrationEquation]:
    return [CalibrationEquation(s) for s in raw_input]


# PART 1

def solve_part_1(calibration_equations: list[CalibrationEquation]) -> int:
    sum_of_valid_target_values = 0
    for equation in calibration_equations:
        if equation.is_solvable(equation.operands):
            sum_of_valid_target_values += equation.target_value
    return sum_of_valid_target_values


def main():
    calibration_equations: list[CalibrationEquation] = build_calibration_equations(read_input(filename))

    solution_part_1 = solve_part_1(calibration_equations)
    print(f"Part 1: Number of visited fields is {solution_part_1}.")


if __name__ == "__main__":
    main()
