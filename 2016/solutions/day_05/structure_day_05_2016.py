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
