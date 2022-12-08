import hashlib


def find_lowest_number_with_leading_zeroes_in_md5_hast(key: str, number_of_leading_zeroes: int):
    number = 0
    while True:
        string_to_hash = key + str(number)
        md5_hash = hashlib.md5(string_to_hash.encode()).hexdigest()

        zeroes = ""
        for i in range(0, number_of_leading_zeroes):
            zeroes += "0"

        if md5_hash.startswith(zeroes):
            return number
        number += 1


def main():
    secret_key = "ckczppom"

    lowest_number_5_zeroes = find_lowest_number_with_leading_zeroes_in_md5_hast(secret_key, 5)
    print(f'Santas secret key needs to be appended with {lowest_number_5_zeroes}.')

    lowest_number_6_zeroes = find_lowest_number_with_leading_zeroes_in_md5_hast(secret_key, 6)
    print(f'And now it must be appended with {lowest_number_6_zeroes}.')


if __name__ == "__main__":
    main()
