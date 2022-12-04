import Utils.input_processing as ip

PRIORITIES = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
              "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
              "x": 24, "y": 25, "z": 26,
              "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37,
              "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48,
              "W": 49, "X": 50, "Y": 51, "Z": 52}


def read_input(filename: str) -> list[str]:
    input_strings = ip.read_input_list(filename)
    input_strings = ip.trim_newlines(input_strings)
    return input_strings


# Problem 1


def cut_all_strings_in_half(strings: list[str]) -> list[list[str]]:
    cutted_strings = []
    for string in strings:
        cutted_strings.append(cut_string_in_halfs(string))
    return cutted_strings


def cut_string_in_halfs(string: str) -> list[str]:
    half_length = int(len(string) / 2)
    first_half = string[0:half_length]
    second_half = string[half_length: len(string)]
    return [first_half, second_half]


def find_all_duplicated_characters(list_of_input_lists: list[list[str]]) -> list[str]:
    list_of_duplicated_characters = []
    for list_of_strings in list_of_input_lists:
        list_of_duplicated_characters.append(find_duplicate_character(list_of_strings))
    return list_of_duplicated_characters


def find_duplicate_character(input_strings: list[str]) -> str:
    # Precondition 1: input_strings contains by definition only exactly two strings.
    # Precondition 2: input_strings contains exactly on duplicated character.
    first_string = input_strings[0]
    second_string = input_strings[1]
    duplicated_character = None
    for char in first_string:
        if char in second_string:
            duplicated_character = char
            break
    if duplicated_character is None:
        print(first_string + ' ' + second_string)
    return duplicated_character


def find_sum_of_priorities_of_duplicated_characters(duplicated_characters: list[str]) -> int:
    sum_of_priorities = 0
    for character in duplicated_characters:
        sum_of_priorities += (PRIORITIES[character])
    return sum_of_priorities


def calculate_priorities_of_all_duplicated_characters_of_given_input(filename: str) -> int:
    input_strings = read_input(filename)
    cutted_strings = cut_all_strings_in_half(input_strings)
    duplicated_characters = find_all_duplicated_characters(cutted_strings)
    priority_sum = find_sum_of_priorities_of_duplicated_characters(duplicated_characters)
    return priority_sum


# Problem 2


def divide_input_data_into_groups_of_three(list_of_strings: list[str]) -> list[list[str]]:
    list_of_groups = []
    current_group = []
    for i, string in enumerate(list_of_strings):
        if (i + 1) % 3 == 0:
            current_group.append(list_of_strings[i])
            current_group.append(list_of_strings[i - 1])
            current_group.append(list_of_strings[i - 2])
            list_of_groups.append(current_group)
            current_group = []
    return list_of_groups


def find_only_duplicated_characters_in_all_groups_of_three(groups: list[list[str]]) -> list[str]:
    duplicated_characters = []
    for group in groups:
        duplicated_characters.append(find_only_duplicated_character_in_one_group_of_three(group))
    return duplicated_characters


def find_only_duplicated_character_in_one_group_of_three(group: list[str]) -> str:
    duplicated_character = None

    first_string = group[0]
    second_string = group[1]
    third_string = group[2]

    for char in first_string:
        if char in second_string and char in third_string:
            duplicated_character = char
            break
    return duplicated_character


def find_sum_of_priorities_of_all_badges(list_of_characters: list[str]) -> int:
    sum_of_priorities = 0
    for character in list_of_characters:
        sum_of_priorities += PRIORITIES[character]
    return sum_of_priorities


def calculate_sum_of_priorities_of_all_badges_from_input_data(filename: str) -> int:
    input_strings = read_input(filename)
    list_of_groups = divide_input_data_into_groups_of_three(input_strings)
    duplicated_characters = find_only_duplicated_characters_in_all_groups_of_three(list_of_groups)
    return find_sum_of_priorities_of_all_badges(duplicated_characters)


def main():
    print("Solutions to problem 3: [https://adventofcode.com/2022/day/3]")

    sum_of_priorities = calculate_priorities_of_all_duplicated_characters_of_given_input(
        "../input_data/03_12_problem_data.txt")
    print(f'The sum of the priorities of the duplicated items is {sum_of_priorities}.')
    sum_of_priorities_of_badges = calculate_sum_of_priorities_of_all_badges_from_input_data(
        "../input_data/03_12_problem_data.txt")
    print(f'The sum of the priorities of all badges is {sum_of_priorities_of_badges}.')

    print("")


if __name__ == "__main__":
    main()
