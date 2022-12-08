from Utils import input_processing as ip


# Problem 1


def count_nice_words(filename: str) -> int:
    list_of_input_words = ip.read_input(filename)
    number_of_nice_words = 0

    for word in list_of_input_words:
        if is_nice(word):
            number_of_nice_words += 1
    return number_of_nice_words


def is_nice(s: str) -> bool:
    condition_1 = contains_at_least_three_vowels(s)
    condition_2 = contains_double_letter(s)
    condition_3 = contains_no_forbidden_strings(s)
    return condition_1 and condition_2 and condition_3


def contains_at_least_three_vowels(s: str) -> bool:
    number_of_vowels = 0
    number_of_vowels += s.count("a")
    number_of_vowels += s.count("e")
    number_of_vowels += s.count("i")
    number_of_vowels += s.count("o")
    number_of_vowels += s.count("u")
    return number_of_vowels >= 3


def contains_double_letter(s):
    for i in range(0, len(s) - 1):
        if s[i] is s[i + 1]:
            return True
    return False


def contains_no_forbidden_strings(s):
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    for string in forbidden_strings:
        if string in s:
            return False
    return True


def main():
    problem_filename = "../input_data/05_12_problem_data.txt"
    number_of_nice_words = count_nice_words(problem_filename)

    print(f'The number of nice words is {number_of_nice_words}.')


if __name__ == "__main__":
    main()
