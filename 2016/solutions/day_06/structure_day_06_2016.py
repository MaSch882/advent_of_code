from abc import ABC, abstractmethod


class ErrorCorrector(ABC):
    list_of_strings: list[str]
    most_frequent_chars: list[str]
    word_length: int

    def __init__(self, list_of_strings: list[str]):
        self.list_of_strings = list_of_strings
        self.most_frequent_chars = []
        self.word_length = len(self.list_of_strings[0])

    @abstractmethod
    def correct_error_of_message(self):
        raise NotImplementedError


class MostFrequentErrorCorrector(ErrorCorrector):

    def correct_error_of_message(self) -> str:
        corrected_message = ""
        for i in range(0, self.word_length):
            corrected_message += self.extract_most_frequent_char_at_position(i)
        return corrected_message

    def extract_most_frequent_char_at_position(self, index: int) -> str:
        mapping_char_to_number = {}

        for string in self.list_of_strings:
            char_at_position = string[index]
            try:
                mapping_char_to_number[char_at_position] += 1
            except KeyError:
                mapping_char_to_number.update({char_at_position: 1})

        sorted_mapping = sorted(mapping_char_to_number, key=lambda x: mapping_char_to_number[x])
        return sorted_mapping[-1]


class LeastFrequentErrorCorrector(ErrorCorrector):

    def correct_error_of_message(self) -> str:
        corrected_message = ""
        for i in range(0, self.word_length):
            corrected_message += self.extract_least_frequent_char_at_position(i)
        return corrected_message

    def extract_least_frequent_char_at_position(self, index: int) -> str:
        mapping_char_to_number = {}

        for string in self.list_of_strings:
            char_at_position = string[index]
            try:
                mapping_char_to_number[char_at_position] += 1
            except KeyError:
                mapping_char_to_number.update({char_at_position: 1})

        sorted_mapping = sorted(mapping_char_to_number, key=lambda x: mapping_char_to_number[x])
        return sorted_mapping[0]
