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
    appendix: int
    password: str

    def __init__(self, door_key: str, password_length: int):
        self.door_key = door_key
        self.password_length = password_length
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


class PositionBasedPasswordCracker:
    door_key: str
    password_length: int
    appendix: int
    password: list[str]

    position_bit: int
    password_bit: int
    visited_bits: list[int]

    def __init__(self, door_key: str, password_length: int, position_bit: int, password_bit: int):
        self.door_key = door_key
        self.password_length = password_length
        self.appendix = 1
        self.password = ["X" for x in range(0, password_length)]
        
        self.position_bit = position_bit - 1
        self.password_bit = password_bit - 1
        self.visited_bits = []

    def crack_password(self) -> str:
        while len(self.visited_bits) != self.password_length:
            next_hash_string = self.find_next_hash_string()
            next_position = int(next_hash_string[self.position_bit])
            if next_position not in self.visited_bits:
                print(f"Cracking position {next_position + 1}...")
                self.password[next_position] = next_hash_string[self.password_bit]
                self.visited_bits.append(next_position)
                print(f"Cracked position {next_position + 1}!\n")

        return self.build_password()

    def build_password(self):
        password = ""
        for char in self.password:
            password += char
        return password

    def find_next_hash_string(self) -> str:
        hashed_candidate = "XXXXXXXX"
        position_bit = self.extract_position_bit(hashed_candidate)
        while not MD5Checker.starts_with_five_zeroes(hashed_candidate) or position_bit not in range(0,
                                                                                                    self.password_length):
            candidate = self.door_key + str(self.appendix)
            hashed_candidate = MD5Hasher.hash(candidate)
            position_bit = self.extract_position_bit(hashed_candidate)
            self.appendix += 1
        return hashed_candidate

    def extract_position_bit(self, hashed: str) -> int:
        position_bit = hashed[self.position_bit]
        try:
            p = int(position_bit)
            if p in range(0, self.password_length + 1):
                return p
            return 9
        except ValueError:
            return 9
