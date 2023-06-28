from hashlib import md5


class MD5Hasher:

    @staticmethod
    def hash(to_hash: str) -> str:
        return md5(to_hash.encode()).hexdigest()


class MD5Checker:

    @staticmethod
    def starts_with_substring(hashed: str, substring: str) -> bool:
        return hashed.startswith(substring)

    @staticmethod
    def starts_with_five_zeroes(hashed: str) -> bool:
        return MD5Checker.starts_with_substring(hashed, "00000")


class InOrderPasswordCracker:
    door_key: str
    password_length: int
    interesting_bit: int
    appendix: int
    password: str

    def __init__(self, door_key: str, password_length: int, interesting_bit: int):
        self.door_key = door_key
        self.password_length = password_length
        self.interesting_bit = interesting_bit - 1
        self.appendix = 1
        self.password = ""

    def crack_password(self) -> str:
        for i in range(0, self.password_length):
            next_hash_string = self.find_next_hash_string()
            self.password += next_hash_string[5]
        return self.password

    def find_next_hash_string(self) -> str:
        hashed_candidate = ""
        while not MD5Checker.starts_with_five_zeroes(hashed_candidate):
            candidate = self.door_key + str(self.appendix)
            hashed_candidate = MD5Hasher.hash(candidate)
            self.appendix += 1
        return hashed_candidate
