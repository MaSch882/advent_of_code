from framework.input_processing import InputReader
from structure_day_06_2016 import MostFrequentErrorCorrector, LeastFrequentErrorCorrector

filename = r"..\..\input_data\input_day_06_2016.txt"


def main():
    words_with_error = get_words_with_error()
    print_solution_part_1(words_with_error)  # xhnqpqql
    print_solution_part_2(words_with_error)  # brhailro


def print_solution_part_1(words: list[str]):
    error_corrector = MostFrequentErrorCorrector(list_of_strings=words)
    corrected_message = error_corrector.correct_error_of_message()
    print(f"The corrected message using most frequent characters is {corrected_message}.")


def print_solution_part_2(words: list[str]):
    error_corrector = LeastFrequentErrorCorrector(list_of_strings=words)
    corrected_message = error_corrector.correct_error_of_message()
    print(f"The corrected message using least frequent characters is {corrected_message}.")


def get_words_with_error():
    return InputReader.read_input(filename=filename)


if __name__ == "__main__":
    main()
