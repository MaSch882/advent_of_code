from Utils import input_processing
from structure_day_05_2015 import FirstNiceWordCounter, SecondNiceWordCounter

filename = r"..\..\input_data/input_day_05_2015.txt"


def main():
    list_of_words = read_input()

    print_solution_part_1(list_of_words)
    print_solution_part_2(list_of_words)


def print_solution_part_1(list_of_words: list[str]):
    number_of_nice_words = FirstNiceWordCounter.count_nice_words(list_of_words)
    print(f'The number of nice words is {number_of_nice_words}.')


def print_solution_part_2(list_of_words: list[str]):
    number_of_nice_words = SecondNiceWordCounter.count_nice_words(list_of_words)
    print(f'The number of new nice words is now {number_of_nice_words}.')


def read_input() -> list[str]:
    return input_processing.read_input(filename)


if __name__ == "__main__":
    main()
