from dataclasses import dataclass


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
            has_palindrome = self.has_palindrome_of_length_four_with_different_chars(sequence)
            if has_palindrome:
                return True
        return False

    def has_palindrome_in_hypernet_seq(self):
        for sequence in self.hypernet_blocks:
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

    def count_ips_with_tls(self, ips: list[IPAdress]):
        for ip in ips:
            checker = TLSChecker(ip)
            if checker.supports_tls():
                self.number_of_tls_ips += 1

        return self.number_of_tls_ips


class SSLChecker:

    def __init__(self, ip: IPAdress):
        pass

    def supports_ssl(self):
        pass


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
