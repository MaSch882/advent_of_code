from Utils import input_processing as ip


def read_input(filename: str) -> list[str]:
    list_of_strings = ip.read_input_list(filename)
    trimmed_strings = ip.trim_newlines(list_of_strings)
    return trimmed_strings


# Problem 1


def unzip_data_from_input(list_of_strings: list[str]) -> list[list[list[int]]]:
    cutted_data = cut_data_into_two_parts(list_of_strings)
    unpacked_all_numbers_encoded = unpack_encoded_numbers_in_cutted_date(cutted_data)
    return unpacked_all_numbers_encoded


def cut_data_into_two_parts(list_of_strings: list[str]) -> list[list[str]]:
    return [string.split(",") for string in list_of_strings]


def unpack_encoded_numbers_in_cutted_date(cutted_data: list[list[str]]) -> list[list[list[int]]]:
    unpacked_numbers = []
    for list_of_strings in cutted_data:
        first_data_entry = list_of_strings[0]
        second_data_entry = list_of_strings[1]

        numbers_in_first_data_entry = first_data_entry.split('-')
        numbers_in_second_data_entry = second_data_entry.split('-')

        range_of_numbers_in_first_entry = list(
            range(int(numbers_in_first_data_entry[0]), int(numbers_in_first_data_entry[1]) + 1))
        range_of_numbers_in_second_entry = list(
            range(int(numbers_in_second_data_entry[0]), int(numbers_in_second_data_entry[1]) + 1))

        unpacked_numbers.append([range_of_numbers_in_first_entry, range_of_numbers_in_second_entry])
    return unpacked_numbers


def are_lists_contained_in_each_other(lists: list[list[int]]) -> bool:
    first_list = lists[0]
    second_list = lists[1]

    first_contains_second = is_first_list_contained_in_second_list(first_list, second_list)
    second_contains_first = is_second_list_contained_in_first_list(first_list, second_list)

    return first_contains_second or second_contains_first


def is_first_list_contained_in_second_list(first_list: list[int], second_list: list[int]) -> bool:
    for number in first_list:
        if number not in second_list:
            return False
    return True


def is_second_list_contained_in_first_list(first_list: list[int], second_list: list[int]):
    return is_first_list_contained_in_second_list(second_list, first_list)


def count_pairs_of_list_containing_each_other(unpacked_numbers: list[list[list[int]]]) -> int:
    number_of_lists_containing_each_other = 0
    for pair in unpacked_numbers:
        if are_lists_contained_in_each_other(pair):
            number_of_lists_containing_each_other += 1
    return number_of_lists_containing_each_other


def count_pairs_of_jobs_contained_in_each_other_from_input_data(filename: str) -> int:
    list_of_strings = read_input(filename)
    unzipped_list_of_numbers = unzip_data_from_input(list_of_strings)
    number_of_pairs_containing_each_other = count_pairs_of_list_containing_each_other(unzipped_list_of_numbers)
    return number_of_pairs_containing_each_other


# Problem 2

def do_two_lists_overlap(lists: list[list[int]]) -> bool:
    first_list = lists[0]
    second_list = lists[1]

    for number in first_list:
        if number in second_list:
            return True
    return False


def count_pairs_of_list_overlapping(unpacked_numbers: list[list[list[int]]]) -> int:
    number_of_lists_overlapping = 0
    for pair in unpacked_numbers:
        if do_two_lists_overlap(pair):
            number_of_lists_overlapping += 1
    return number_of_lists_overlapping


def count_pairs_of_jobs_overlapping_from_input_data(filename: str) -> int:
    list_of_strings = read_input(filename)
    unzipped_list_of_numbers = unzip_data_from_input(list_of_strings)
    number_of_pairs_overlapping = count_pairs_of_list_overlapping(unzipped_list_of_numbers)
    return number_of_pairs_overlapping


def main():
    print("Solutions to problem 4: [https://adventofcode.com/2022/day/4]")

    pairs_of_jobs_containing_each_other = count_pairs_of_jobs_contained_in_each_other_from_input_data(
        "../input_data/04_12_problem_data.txt")
    print(f'The number of jobs where one job is contained in the other is {pairs_of_jobs_containing_each_other}.')

    pairs_of_jobs_overlapping = count_pairs_of_jobs_overlapping_from_input_data("../input_data/04_12_problem_data.txt")
    print(f'The number of jobs where the jobs are overlapping is {pairs_of_jobs_overlapping}.')

    print("")


if __name__ == "__main__":
    main()
