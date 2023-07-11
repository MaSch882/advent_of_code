from Utils.input_processing import InputReader
from structure_day_09_2016 import FormatDecrompessor

filename = r"..\..\input_data\input_day_09_2016.txt"

test_data = ["(27x12)(20x12)(13x14)(7x10)(1x12)A"]


def main():
    compressed_file = InputReader.read_input(filename)[0]

    # log_teststrings()

    print_solution_part_1(compressed_file)
    print_solution_part_2(compressed_file)


def print_solution_part_1(compressed_file: str):
    decompressed_file = FormatDecrompessor.decrompress(compressed_file)
    decompressed_length = len(decompressed_file)

    print(f"The decompressed length of the file is {decompressed_length}.")


def print_solution_part_2(compressed_file: str):
    decompressed_length = FormatDecrompessor.compute_decompressed_length_without_decompression(compressed_file)
    print(f"The decompressed length of the file using the recursive compression algorithm is {decompressed_length}.")


def log_teststrings():
    data = {"(3x3)XYZ": 9,
            "X(8x2)(3x3)ABCY": 20,
            "(27x12)(20x12)(13x14)(7x10)(1x12)A": 241920,
            "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN": 445,
            "(8x2)AB(1x2)C": 8,
            "(15x2)AB(2x3)CD(1x2)A": 20
            }

    successes = 0

    for string in data.keys():
        expected = data[string]
        calculated = FormatDecrompessor.compute_decompressed_length_without_decompression(string)

        equal = expected == calculated
        message = "OK." if equal else "Error!"

        if equal:
            successes += 1

        print(f"Current string: \t {string}")
        print(f"Expected length: \t {expected}")
        print(f"Calculated length: \t {calculated}")
        print(f"{message}")
        print("-----------------------------------------")

    print(f"{successes} of {len(data)} tests successful.")


if __name__ == "__main__":
    main()
