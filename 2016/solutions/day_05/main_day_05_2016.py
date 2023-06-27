from structure_day_05_2016 import MD5Hasher, MD5Checker


def main():
    test_hash = MD5Hasher.hash("abc3231929")
    print(test_hash)
    print(MD5Checker.starts_with_five_zeroes(test_hash))


if __name__ == "__main__":
    main()
