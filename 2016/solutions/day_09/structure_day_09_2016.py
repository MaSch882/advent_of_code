from dataclasses import dataclass

from Utils.lists import ListUtils


class FormatDecrompessor:

    @staticmethod
    def decompress_all(list_of_strings: list[str]) -> list[str]:
        decompressed = []
        for string in list_of_strings:
            decompressed.append(FormatDecrompessor.decrompress(string))
        return decompressed

    @staticmethod
    def decrompress(string: str) -> str:
        string_as_list = [x for x in string]
        decompressed_string = ""

        while len(string_as_list) != 0:
            current_character = ListUtils.get_first(string_as_list)
            if current_character != "(":
                decompressed_string += ListUtils.get_and_delete_first(string_as_list)
            else:
                marker = MarkerExtractor.extract_next_marker(string_as_list)
                decompressed_string += MarkerProcessor.process_marker(marker, string_as_list)

        return decompressed_string


@dataclass()
class Marker:
    substring_length: int
    times_to_repeat: int


class MarkerExtractor:

    @staticmethod
    def extract_next_marker(string_as_list: list[str]) -> Marker:
        ListUtils.get_and_delete_first(string_as_list)
        marker_list = []
        while ListUtils.get_first(string_as_list) != ")":
            marker_list += string_as_list.pop(0)

        marker_string = ""
        for string in marker_list:
            marker_string += string

        splitted_marker_string = marker_string.split("x")

        ListUtils.get_and_delete_first(string_as_list)
        marker = Marker(int(splitted_marker_string[0]), int(splitted_marker_string[1]))
        return marker


class MarkerProcessor:

    @staticmethod
    def process_marker(marker: Marker, list_to_process: list[str]) -> str:
        sequence_to_repeat = ""
        for i in range(0, marker.substring_length):
            sequence_to_repeat += ListUtils.get_and_delete_first(list_to_process)

        repeated_sequence = ""
        for i in range(0, marker.times_to_repeat):
            repeated_sequence += sequence_to_repeat

        return repeated_sequence
