from loesungen.python.utils import input_processing as ip

filename = "H:/git_repos/advent_of_code/2024/01_real.txt"
filename_test = "H:/git_repos/advent_of_code/2024/01_test.txt"


# INPUT

def read_input() -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(filename)


def build_lists(raw_input: list[str]) -> list[list[int]]:
    if not raw_input:
        return [[], []]

    list1 = []
    list2 = []

    for entry in raw_input:
        entries = entry.split(" ")
        list1.append(int(entries[0].strip()))
        list2.append(int(entries[-1].strip()))

    return [list1, list2]


# PART 1

def sort_lists(input_lists: list[list[int]]) -> list[list[int]]:
    input_lists[0].sort()
    input_lists[1].sort()
    return [input_lists[0], input_lists[1]]


def calculate_total_distance(sorted_lists: list[list[int]]) -> int:
    total_distance = 0

    left_list = sorted_lists[0]
    right_list = sorted_lists[1]

    for i, _ in enumerate(sorted_lists[0]):
        number_left = left_list[i]
        number_right = right_list[i]
        total_distance += abs(number_left - number_right)

    return total_distance


def solve_part_1() -> int:
    raw_data = read_input()
    input_lists = build_lists(raw_data)
    sorted_lists = sort_lists(input_lists)
    return calculate_total_distance(sorted_lists)


# PART 2

def calculate_similarity(input_lists: list[list[int]]):
    similarity = 0

    left_list = input_lists[0]
    right_list = input_lists[1]

    for number in left_list:
        number_of_matches = right_list.count(number)
        similarity += number * number_of_matches

    return similarity


def solve_part_2() -> int:
    raw_data = read_input()
    input_lists = build_lists(raw_data)
    return calculate_similarity(input_lists)


def main():
    solution_part_1 = solve_part_1()
    print(f"Part 1: Total distance is {solution_part_1}.")

    solution_part_2 = solve_part_2()
    print(f"Part 1: Total distance is {solution_part_2}.")


if __name__ == "__main__":
    main()
