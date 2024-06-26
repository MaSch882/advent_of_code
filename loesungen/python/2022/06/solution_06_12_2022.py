from loesungen.python.utils.input_processing import InputReader as ip


def read_input(filename: str) -> str:
    list_of_strings = ip.read_input_list(filename)
    list_of_strings = ip.trim_newlines(list_of_strings)
    return list_of_strings[0]


# Problem 1 and 2


def find_number_of_processed_characters_before_first_event(input_stream: str, event: int) -> int:
    current_characters = [input_stream[i] for i in range(0, event)]
    input_stream = input_stream[event:]
    current_marker_position = event
    for character in input_stream:
        if is_start_of_packet(current_characters):
            return current_marker_position
        current_characters = current_characters[1:]
        current_characters.append(character)
        current_marker_position += 1


def is_start_of_packet(input_characters: list[str]) -> bool:
    for character in input_characters:
        if input_characters.count(character) > 1:
            return False
    return True


def main():
    print("Solutions to problem 6: [https://adventofcode.com/2022/day/6]")

    filename = r"..\..\..\..\input_data/2022/2022_06.txt"
    input_stream = read_input(filename)

    START_OF_PACKET = 4
    MESSAGE = 14

    index_of_first_start_of_packet = find_number_of_processed_characters_before_first_event(input_stream,
                                                                                            START_OF_PACKET)
    print(
        f'There are {index_of_first_start_of_packet} characters processed before the first start-of-packet is found.')

    index_of_first_start_of_message = find_number_of_processed_characters_before_first_event(input_stream, MESSAGE)
    print(f'There are {index_of_first_start_of_message} characters processed before the first message is found.')

    print("")


if __name__ == "__main__":
    main()
