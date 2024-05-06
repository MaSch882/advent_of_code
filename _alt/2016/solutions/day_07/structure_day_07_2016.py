from dataclasses import dataclass


class PalindromeChecker:

    def __init__(self):
        raise NotImplementedError("PalindromeChecker must not be instantiated.")

    @staticmethod
    def is_palindrome(sequence: str) -> bool:
        return sequence == sequence[::-1]

    @staticmethod
    def has_palindrome(sequence: str, length: int, different_characters: bool) -> bool:
        for i, char in enumerate(sequence):
            block = sequence[i:i + length]
            if len(block) != length:
                return False

            is_palindrome = PalindromeChecker.is_palindrome(block)
            if different_characters:
                has_different_characters = PalindromeChecker.contains_more_than_one_character(block)
                if is_palindrome and has_different_characters:
                    return True
            else:
                if is_palindrome:
                    return True
        return False

    @staticmethod
    def has_palindrome_of_length(sequence: str, length: int) -> bool:
        return PalindromeChecker.has_palindrome(sequence, length, different_characters=False)

    @staticmethod
    def has_palindrome_of_length_with_different_chars(sequence: str, length: int) -> bool:
        return PalindromeChecker.has_palindrome(sequence, length, different_characters=True)

    @staticmethod
    def contains_more_than_one_character(sequence: str) -> bool:
        return sequence.count(sequence[0]) != len(sequence)


class PalindromeExtractor:

    def __init__(self):
        raise NotImplementedError("PalindromeExtractor must not be instantiated.")

    @staticmethod
    def extract_palindromes_containing_more_than_one_character(to_extract: str, length: int):
        palindromes = []

        for i, char in enumerate(to_extract):
            block = to_extract[i:i + length]

            if len(block) != length:
                continue

            is_palindrome = PalindromeChecker.is_palindrome(block)
            contains_more_than_one_character = PalindromeChecker.contains_more_than_one_character(block)

            if is_palindrome and contains_more_than_one_character:
                palindromes.append(block)

        return palindromes


class AdjacentPalindromeCalculator:

    @staticmethod
    def calculate_adjacent_palindrome(palindrome: str):
        """
        Achtung: Hier nur fuer 3er-Palindrome. Sonst nicht definiert.
        Wir gehen ferner davon aus, dass die API richtig befüllt wird.
        """
        first_char = palindrome[0]
        second_char = palindrome[1]

        return second_char + first_char + second_char


@dataclass()
class IPAdress:
    raw_ip: str
    supernet_blocks: list[str]
    hypernet_blocks: list[str]

    def __init__(self, ip: str):
        self.raw_ip = ip
        self.supernet_blocks = []
        self.hypernet_blocks = []
        self.extract_sequences()

    def extract_sequences(self):
        splitted_ip = self.split_ip_up()
        for index, block in enumerate(splitted_ip):
            if index % 2 == 0:
                self.supernet_blocks.append(block)
            if index % 2 == 1:
                self.hypernet_blocks.append(block)

    def split_ip_up(self) -> list[str]:
        return self.raw_ip.replace("]", "[").split("[")


class TLSChecker:
    ip_adress: IPAdress
    hypernet_blocks: list[str]
    supernet_blocks: list[str]

    def __init__(self, ip: IPAdress):
        self.ip_adress = ip
        self.hypernet_blocks = ip.hypernet_blocks
        self.supernet_blocks = ip.supernet_blocks

    def supports_tls(self):
        has_hypertext_palindrome = self.has_palindrome_in_hypernet_seq()
        has_non_hypertext_palindrome = self.has_palindrome_in_non_hypernet_seq()
        return has_non_hypertext_palindrome and not has_hypertext_palindrome

    def has_palindrome_in_non_hypernet_seq(self):
        for sequence in self.supernet_blocks:
            has_palindrome = PalindromeChecker.has_palindrome_of_length_with_different_chars(sequence, 4)
            if has_palindrome:
                return True
        return False

    def has_palindrome_in_hypernet_seq(self):
        for sequence in self.hypernet_blocks:
            has_palindrome = PalindromeChecker.has_palindrome_of_length_with_different_chars(sequence, 4)
            if has_palindrome:
                return True
        return False


class TLSCounter:
    number_of_tls_ips: int

    def __init__(self):
        self.number_of_tls_ips = 0

    def count_ips_with_tls(self, ips: list[IPAdress]):
        for ip in ips:
            checker = TLSChecker(ip)
            if checker.supports_tls():
                self.number_of_tls_ips += 1

        return self.number_of_tls_ips


class SSLChecker:
    ip_adress: IPAdress
    hypernet_blocks: list[str]
    supernet_blocks: list[str]
    hypernet_palindromes: list[str]
    supernet_palindromes: list[str]

    def __init__(self, ip: IPAdress):
        self.ip_adress = ip
        self.hypernet_blocks = ip.hypernet_blocks
        self.supernet_blocks = ip.supernet_blocks
        self.hypernet_palindromes = []
        self.supernet_palindromes = []
        self.extract_all_palindromes()

    def extract_all_palindromes(self):
        for hypernet_block in self.hypernet_blocks:
            hypernet_palindromes = PalindromeExtractor.extract_palindromes_containing_more_than_one_character(
                hypernet_block, 3)
            self.hypernet_palindromes.extend(hypernet_palindromes)
        for supernet_block in self.supernet_blocks:
            supernet_palindromes = PalindromeExtractor.extract_palindromes_containing_more_than_one_character(
                supernet_block, 3)
            self.supernet_palindromes.extend(supernet_palindromes)

    def supports_ssl(self):
        supernet_palindromes = self.supernet_palindromes
        hypernet_palindromes = self.hypernet_palindromes

        for supernet_palindrome in supernet_palindromes:
            adjacent_palindrome = AdjacentPalindromeCalculator.calculate_adjacent_palindrome(supernet_palindrome)
            if adjacent_palindrome in hypernet_palindromes:
                return True
        return False


class SSLCounter:
    number_of_ssl_ips: int

    def __init__(self):
        self.number_of_ssl_ips = 0

    def count_ips_with_ssl(self, ips: list[IPAdress]):
        for ip in ips:
            checker = SSLChecker(ip)
            if checker.supports_ssl():
                self.number_of_ssl_ips += 1

        return self.number_of_ssl_ips
