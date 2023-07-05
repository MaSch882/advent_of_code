from dataclasses import dataclass

from Utils.strings import StringUtils


class FormatDecrompessor:

    @staticmethod
    def decrompress(string: str) -> str:
        string_as_list = [x for x in string]
        decompressed_string = ""

        while len(string_as_list) != 0:
            current_character = string_as_list[0]
            if current_character != "(":
                decompressed_string += current_character
            else:
                marker = MarkerExtractor.extract_next_marker(string_as_list)
                decompressed_string += MarkerProcessor.process_marker(marker, string_as_list)
                print(marker)
                print(decompressed_string)

                # TODO Marker decompress implementieren
            string_as_list.pop(0)

        print(string_as_list)
        print(decompressed_string)


@dataclass()
class Marker:
    substring_length: int
    times_to_repeat: int


class MarkerExtractor:

    @staticmethod
    def extract_next_marker(string_as_list) -> Marker:
        StringUtils.get_and_delete_first(string_as_list)
        marker_list = []
        while string_as_list[0] != ")":
            marker_list += string_as_list.pop(0)
        marker_list.remove("x")
        StringUtils.get_and_delete_first(string_as_list)
        marker = Marker(marker_list[0], marker_list[1])
        return marker


class MarkerProcessor:

    @staticmethod
    def process_marker(marker: Marker, list_to_process: list[str]) -> str:
        print(list_to_process)
        return "?"
