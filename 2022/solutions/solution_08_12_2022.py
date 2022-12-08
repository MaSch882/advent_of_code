from Utils import input_processing as ip


def read_input(filename: str) -> list[str]:
    list_of_inputs = ip.read_input_list(filename)
    trimmed_list = ip.trim_newlines(list_of_inputs)
    return trimmed_list


def main():
    print("Solutions to problem 8: [https://adventofcode.com/2022/day/8]")

    print("")


if __name__ == "__main__":
    main()
