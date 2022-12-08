def read_input_list(filename: str) -> list[str]:
    result = []
    with open(filename) as file:
        for line in file:
            result.append(line)
    return result


def trim_newlines(list_of_strings: list[str]) -> list[str]:
    return [string.strip() for string in list_of_strings]


def read_input(filename: str) -> list[str]:
    return trim_newlines(read_input_list(filename))
