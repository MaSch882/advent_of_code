from advent_of_code.loesungen.python.utils import input_processing as ip

# INPUT

def read_input(filename: str) -> list[str]:
    input_reader = ip.InputReader()
    return input_reader.read_input(filename)

# PART 1

def solve_part_1(lattice: list[str], word_to_search: str) -> int:
    number_of_occurences: int = 0
    # The number of occurences of the word to search in the lattice
    # is the number of it ocurring forwards PLUS the number of it
    # occuring backwards.
    number_of_occurences += count_all_occurences(lattice, word_to_search)
    number_of_occurences += count_all_occurences(lattice, word_to_search[::-1])

    return number_of_occurences


def count_all_occurences(lattice: list[str], word_to_search: str):
    number_of_occurences: int = 0

    number_of_occurences += count_all_horizontal_occurences(lattice, word_to_search)
    number_of_occurences += count_all_vertical_occurences(lattice, word_to_search)
    number_of_occurences += count_all_diagonal_downwards_occurences(lattice, word_to_search)
    number_of_occurences += count_all_diagonal_upwards_occurences(lattice, word_to_search)

    return number_of_occurences

def count_all_horizontal_occurences(lattice: list[str], word_to_search: str) -> int:
    if not lattice:
        return 0

    return sum([row.count(word_to_search) for row in lattice])

def count_all_vertical_occurences(lattice: list[str], word_to_search: str) -> int:
    if not lattice:
        return 0

    number_of_rows = len(lattice)
    number_of_columns = len(lattice[0])

    word_length = len(word_to_search)
    if word_length > number_of_rows:
        return 0

    vertical_occurences = 0

    # For each row...
    for row_offset in range(number_of_rows):
        # ...look through each column...
        for column_number in range(number_of_columns):
            word_found = ""
            # ...exactly so far as we have length.
            for row_number in range(word_length):
                try:
                    word_found += lattice[row_offset + row_number][column_number]
                except IndexError:
                    break
            if word_found == word_to_search:
                vertical_occurences += 1

    return vertical_occurences

def count_all_diagonal_downwards_occurences(lattice: list[str], word_to_search: str) -> int:
    if not lattice:
        return 0

    number_of_rows = len(lattice)
    number_of_columns = len(lattice[0])

    word_length = len(word_to_search)
    if word_length > number_of_rows:
        return 0

    diagonal_downwards_occurences = 0

    # For each row...
    for row_number in range(number_of_rows):
        # ...and for each column...
        for column_number in range(number_of_columns):
            word_found = ""
            # ...exactly so far as we have length.
            for offset in range(word_length):
                try:
                    word_found += lattice[row_number + offset][column_number + offset]
                except IndexError:
                    break
            if word_found == word_to_search:
                diagonal_downwards_occurences += 1

    return diagonal_downwards_occurences

def count_all_diagonal_upwards_occurences(lattice: list[str], word_to_search: str) -> int:
    if not lattice:
        return 0

    number_of_rows = len(lattice)
    number_of_columns = len(lattice[0])

    word_length = len(word_to_search)
    if word_length > number_of_rows:
        return 0

    diagonal_upwards_occurences = 0

    # For each row...
    for row_number in range(number_of_rows):
        # ...and for each column...
        for column_number in range(number_of_columns):
            word_found = ""
            # ...exactly so far as we have length.
            for offset in range(word_length):
                try:
                    # If index gets negative, we don't want to continue!
                    if row_number - offset < 0:
                        break
                    word_found += lattice[row_number - offset][column_number + offset]
                except IndexError:
                    break
            if word_found == word_to_search:
                diagonal_upwards_occurences += 1

    return diagonal_upwards_occurences

# PART 2
def is_cross(lattice: list[str], row_number: int, column_number: int) -> bool:
    valid_words = ["MAS", "SAM"]

    main_diagonal = ""
    non_diagonal = ""

    for i in range(3):
        try:
            main_diagonal += lattice[row_number + i][column_number + i]
            non_diagonal += lattice[row_number + 2 - i][column_number + i]
        except IndexError:
            break

    return main_diagonal in valid_words and non_diagonal in valid_words

def solve_part_2(lattice: list[str]) -> int:
    number_of_crosses = 0

    for row_number in range(len(lattice)):
        for column_number in range(len(lattice[0])):
            if is_cross(lattice, row_number, column_number):
                number_of_crosses += 1

    return number_of_crosses


def main():
    filename = "C:/_Python/advent_of_code/advent_of_code/input/2024_04_real.txt"
    lattice: list[str] = read_input(filename)

    solution_part_1 = solve_part_1(lattice, "XMAS")
    print(f"Part 1: There is {solution_part_1} times the word XMAS.")

    solution_part_2 = solve_part_2(lattice)
    print(f"Part 2: There are {solution_part_2} X-MAS-crosses.")

if __name__ == "__main__":
    main()
