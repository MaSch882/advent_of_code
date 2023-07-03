class TLSChecker:
    ip_adress: str
    hypernet_seq: list[str]
    non_hypernet_seq: list[str]

    def __init__(self, ip: str):
        self.ip_adress = ip
        self.hypernet_seq = []
        self.non_hypernet_seq = []
        self.has_palindrome_hypernet_seq = None
        self.has_palindrome_non_hypernet_seq = None

    def supports_tls(self):
        self.extract_hypernet_sequences()
        print(f"1: {self.hypernet_seq}")
        print(f"2: {self.non_hypernet_seq}")
        has_hypertext_palindrome = self.has_palindrome_in_hypernet_seq()
        has_non_hypertext_palindrome = self.has_palindrome_in_non_hypernet_seq()
        return has_non_hypertext_palindrome and not has_hypertext_palindrome

    def split_ip_up(self) -> list[str]:
        return self.ip_adress.replace("]", "[").split("[")

    def extract_hypernet_sequences(self):
        splitted_ip = self.split_ip_up()
        for index, block in enumerate(splitted_ip):
            if index % 2 == 0:
                self.non_hypernet_seq.append(block)
            if index % 2 == 1:
                self.hypernet_seq.append(block)

    def has_palindrome_in_non_hypernet_seq(self):
        for sequence in self.non_hypernet_seq:
            has_palindrome = self.has_palindrome_of_length_four_with_different_chars(sequence)
            if has_palindrome:
                return True
        return False

    def has_palindrome_in_hypernet_seq(self):
        for sequence in self.hypernet_seq:
            has_palindrome = self.has_palindrome_of_length_four_with_different_chars(sequence)
            if has_palindrome:
                return True
        return False

    @staticmethod
    def has_palindrome_of_length_four_with_different_chars(sequence: str) -> bool:
        for i, char in enumerate(sequence):
            try:
                first = sequence[i]
                second = sequence[i + 1]
                third = sequence[i + 2]
                fourth = sequence[i + 3]

                if first == fourth and second == third and first != second:
                    return True

            except IndexError:
                return False
        return False


class TLSCounter:
    number_of_tls_ips: int

    def __init__(self):
        self.number_of_tls_ips = 0

    def count_ips_with_tls(self, ips: list[str]):
        for ip in ips:
            checker = TLSChecker(ip)
            if checker.supports_tls():
                self.number_of_tls_ips += 1

        return self.number_of_tls_ips
