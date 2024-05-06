from functools import reduce


class StringUtils:

    @staticmethod
    def convert_char_list_to_string(list_to_convert: list[str]) -> str:
        return reduce(lambda x, y: x + y, list_to_convert)

    @staticmethod
    def convert_string_to_char_list(string_to_convert: str) -> list[str]:
        return [x for x in string_to_convert]
