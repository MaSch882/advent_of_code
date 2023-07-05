from Utils.input_processing import InputReader
from structure_day_09_2016 import FormatDecrompessor

filename = r"..\..\input_data\input_day_09_2016.txt"


def main():
    compressed_file = InputReader.read_input(filename)[0]

    print_solution_part_1(compressed_file)


def print_solution_part_1(compressed_file: str):
    decompressed_file = FormatDecrompessor.decrompress(compressed_file)
    decompressed_length = len(decompressed_file)

    print(f"The decompressed length of the file is {decompressed_length}.")


if __name__ == "__main__":
    main()
