class FirstNiceWordCounter:

    @staticmethod
    def count_nice_words(list_of_words: list[str]) -> int:
        number_of_nice_words = 0

        for word in list_of_words:
            if FirstNiceWordCounter.is_nice(word):
                number_of_nice_words += 1
        return number_of_nice_words

    @staticmethod
    def is_nice(word: str) -> bool:
        condition_1 = StringChecker.contains_at_least_three_vowels(word)
        condition_2 = StringChecker.contains_double_letter(word)
        condition_3 = StringChecker.contains_no_forbidden_strings(word)
        return condition_1 and condition_2 and condition_3


class StringChecker:
    @staticmethod
    def contains_at_least_three_vowels(word: str) -> bool:
        number_of_vowels = 0
        number_of_vowels += word.count("a")
        number_of_vowels += word.count("e")
        number_of_vowels += word.count("i")
        number_of_vowels += word.count("o")
        number_of_vowels += word.count("u")
        return number_of_vowels >= 3

    @staticmethod
    def contains_double_letter(s):
        for i in range(0, len(s) - 1):
            if s[i] is s[i + 1]:
                return True
        return False

    @staticmethod
    def contains_no_forbidden_strings(s):
        forbidden_strings = ["ab", "cd", "pq", "xy"]
        for string in forbidden_strings:
            if string in s:
                return False
        return True
