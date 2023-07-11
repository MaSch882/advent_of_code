from dataclasses import dataclass

from Utils.lists import ListUtils
from Utils.strings import StringUtils


@dataclass()
class Marker:
    substring_length: int
    times_to_repeat: int


class SimpleFormatDecompressor:

    @staticmethod
    def decompress_all(list_of_strings: list[str]) -> list[str]:
        decompressed = []
        for string in list_of_strings:
            decompressed.append(SimpleFormatDecompressor.decrompress(string))
        return decompressed

    @staticmethod
    def decrompress(string: str) -> str:
        string_as_list = StringUtils.convert_string_to_char_list(string)
        decompressed_string = ""

        while len(string_as_list) != 0:
            current_character = ListUtils.get_first(string_as_list)
            if current_character != "(":
                decompressed_string += ListUtils.get_and_delete_first(string_as_list)
            else:
                marker = MarkerExtractor.extract_next_marker(string_as_list)
                decompressed_string += MarkerProcessor.process_marker(marker, string_as_list)

        return decompressed_string


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


class MarkerExtractor:

    @staticmethod
    def extract_next_marker(string_as_list: list[str]) -> Marker:
        ListUtils.get_and_delete_first(string_as_list)
        marker_list = []
        while ListUtils.get_first(string_as_list) != ")":
            marker_list += ListUtils.get_and_delete_first(string_as_list)

        marker_string = StringUtils.convert_char_list_to_string(marker_list)

        splitted_marker_string = marker_string.split("x")

        ListUtils.get_and_delete_first(string_as_list)
        marker = Marker(int(splitted_marker_string[0]), int(splitted_marker_string[1]))
        return marker

    @staticmethod
    def extract_next_marker_and_string(string_as_list: list[str]) -> [Marker, str]:
        marker = MarkerExtractor.extract_next_marker(string_as_list)
        string_length = marker.substring_length

        char_list = []
        for i in range(0, string_length):
            char_list.append(ListUtils.get_and_delete_first(string_as_list))

        marker_string = StringUtils.convert_char_list_to_string(char_list)

        return marker, marker_string


class DecompressedLengthCalculator:
    @staticmethod
    def compute_decompressed_length_recursively(string: str) -> int:
        string_as_list = StringUtils.convert_string_to_char_list(string)
        decompressed_length = 0

        while len(string_as_list) != 0:
            current_character = ListUtils.get_first(string_as_list)

            if current_character != "(":
                decompressed_length += 1
                ListUtils.delete_first(string_as_list)

            else:
                marker, marker_string = MarkerExtractor.extract_next_marker_and_string(string_as_list)
                decompressed_length += \
                    marker.times_to_repeat * DecompressedLengthCalculator.compute_decompressed_length_recursively(
                        marker_string)

        return decompressed_length
