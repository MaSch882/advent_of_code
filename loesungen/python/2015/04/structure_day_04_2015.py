import hashlib


class MD5Hasher:

    @staticmethod
    def hash_string(string: str) -> str:
        return hashlib.md5(string.encode()).hexdigest()

    @staticmethod
    def find_lowest_number_with_leading_zeroes_in_md5_hash(key: str, number_of_leading_zeroes: int):
        number = 0
        while True:
            string_to_hash = key + str(number)
            md5_hash = MD5Hasher.hash_string(string_to_hash)

            zeroes = ""
            for i in range(0, number_of_leading_zeroes):
                zeroes += "0"

            if md5_hash.startswith(zeroes):
                return number
            number += 1
