from loesungen.python.utils import input_processing as ip
from loesungen.python.year_2024.day_06.laboratory import Laboratory

filename = "H:/git_repos/advent_of_code/2024/06_real.txt"


# INPUT

def read_input(f: str) -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(f)


# PART 1


def solve_part_1(laboratory: Laboratory) -> int:
    # Idea:
    # As long as the guard is inside the labs fields, simulate his next step and update the lab fields.
    # As soon as he leaves the lab fields, return the number of visited fields of the guard.
    while laboratory.guard_is_inside:
        laboratory.simulate_next_step()
    return len(laboratory.guard.visited_fields)


def main():
    laboratory: Laboratory = Laboratory(read_input(filename))

    solution_part_1 = solve_part_1(laboratory)
    print(f"Part 1: Number of visited fields is {solution_part_1}.")


if __name__ == "__main__":
    main()
