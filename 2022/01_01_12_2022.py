def calculate_maximum_calories_in_list(filename: str) -> int:
    list_of_strings = read_input_list(filename)
    trimmed_list_of_strings = trim_newlines(list_of_strings)
    list_of_summed_blocks = sum_blocks(trimmed_list_of_strings)
    return calculate_maximum(list_of_summed_blocks)


def calculate_sum_of_three_highest_calories(filename: str) -> int:
    list_of_strings = read_input_list(filename)
    trimmed_list_of_strings = trim_newlines(list_of_strings)
    list_of_summed_blocks = sum_blocks(trimmed_list_of_strings)
    sort_list_of_integers(list_of_summed_blocks)
    return sum_three_highest_calories(list_of_summed_blocks)


def read_input_list(filename: str) -> list[str]:
    result = []
    with open(filename) as file:
        for line in file:
            result.append(line)
    return result


def trim_newlines(list_of_strings: list[str]) -> list[str]:
    return [string.strip() for string in list_of_strings]


def sum_blocks(list_of_strings: list[str]) -> list[int]:
    result = []
    subtotal = 0
    for string in list_of_strings:
        if string != '':
            subtotal += int(string)
        if string == '':
            result.append(subtotal)
            subtotal = 0
    result.append(subtotal)
    return result


def calculate_maximum(list_of_integers: list[int]) -> int:
    return max(list_of_integers)


def sort_list_of_integers(list_of_integers: list[int]) -> None:
    return list_of_integers.sort(reverse=True)


def sum_three_highest_calories(list_of_sorted_integers: list[int]) -> int:
    return sum(list_of_sorted_integers[0:3])


def main():
    max_calories = calculate_maximum_calories_in_list("input_data//1_01_12_problem_1_problem_data.txt")
    print(f'The elf with the maximum amount of calories carries {max_calories} calories.')

    max_three_calories = calculate_sum_of_three_highest_calories("input_data/1_01_12_problem_1_problem_data.txt")
    print(f'The three elves carrying the most calories carry {max_three_calories} in total.')


if __name__ == '__main__':
    main()
