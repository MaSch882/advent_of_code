import math

from advent_of_code.loesungen.python.utils import input_processing as ip

# INPUT

def read_input(filename: str) -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(filename)

def build_orderings(filename_orderings: str) -> list[list[int]]:
    inputs = read_input(filename_orderings)
    orderings = []
    for i in inputs:
        splitted = i.split("|")
        orderings.append([int(splitted[0]), int(splitted[1])])
    return orderings

def build_pagelists(filename_pagelists: str) -> list[list[int]]:
    inputs = read_input(filename_pagelists)
    pagelists = []
    for i in inputs:
        splitted = i.split(",")
        pagelists.append([int(s) for s in splitted])
    return pagelists

# PART 1

def is_ordered_page_list(pagelist: list[int], orderings: list[list[int]]):
    for ordering in orderings:
        x = ordering[0]
        y = ordering[1]
        try:
            index_x = pagelist.index(x)
            index_y = pagelist.index(y)
            if index_x > index_y:
                return False
        except ValueError:
            continue
    return True

def solve_part_1(orderings: list[list[int]], pagelists: list[list[int]]):
    ordered_pagelists = list(filter(lambda p: is_ordered_page_list(p, orderings), pagelists))
    sum = 0
    for p in ordered_pagelists:
        sum += p[math.floor(len(p) / 2)]
    return sum


def main():
    filename_orderings = "C:/_Python/advent_of_code/advent_of_code/input/2024_05_real_orderings.txt"
    filename_pagelists = "C:/_Python/advent_of_code/advent_of_code/input/2024_05_real_pagelists.txt"
    orderings: list[list[int]] = build_orderings(filename_orderings)
    pagelists: list[list[int]] = build_pagelists(filename_pagelists)

    solution_part_1 = solve_part_1(orderings, pagelists)
    print(f"Part 1: Sum of middle pages of sorted pagelists is {solution_part_1}.")

    # solution_part_2 = solve_part_2(lattice)
    # print(f"Part 2: There are {solution_part_2} X-MAS-crosses.")

if __name__ == "__main__":
    main()
