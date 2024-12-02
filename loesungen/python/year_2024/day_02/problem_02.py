from advent_of_code.loesungen.python.utils import input_processing as ip

filename = "C:/_Python/advent_of_code/advent_of_code/input/2024_02_real.txt"

# INPUT

def read_input() -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(filename)


def build_lists(raw_data: list[str]) -> list[list[int]]:
    lists = []

    for date in raw_data:
        numbers = date.split(" ")
        lists.append([int(x) for x in numbers])

    return lists

# PART 1

def is_increasing(report: list[int]):
    indicator = True

    for i in range(0, len(report) - 1):
        if report[i] >= report[i+1]:
            indicator = False
            break

    return indicator


def is_decreasing(report: list[int]):
    indicator = True

    for i in range(0, len(report) - 1):
        if report[i] <= report[i + 1]:
            indicator = False
            break

    return indicator


def has_correct_difference(report: list[int]):
    indicator = True

    for i in range(0, len(report) - 1):
        if abs(report[i] - report[i+1]) > 3:
            indicator = False
            break

    return indicator


def is_safe(report: list[int]):
    all_increasing: bool = is_increasing(report)
    all_decreasing: bool = is_decreasing(report)
    correct_difference: bool = has_correct_difference(report)

    return (all_increasing or all_decreasing) and correct_difference



def solve_part_1(reports: list[list[int]]) -> int:
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
    return safe_reports

# PART 2

def solve_part_2():
    pass


def main():
    reports = build_lists(read_input())

    solution_part_1 = solve_part_1(reports)
    print(f"Part 1: Number of safe reports is {solution_part_1}.")

    # solution_part_2 = solve_part_2()
    # print(f"Part 1: Total distance is {solution_part_2}.")


if __name__ == "__main__":
    main()
