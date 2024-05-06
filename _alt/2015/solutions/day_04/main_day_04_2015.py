from structure_day_04_2015 import MD5Hasher


def main():
    secret_key = "ckczppom"

    print_solution_part_1(secret_key)  # 117946
    print_solution_part_2(secret_key)  # 3938038


def print_solution_part_1(secret_key: str):
    lowest_number_5_zeroes = MD5Hasher.find_lowest_number_with_leading_zeroes_in_md5_hash(secret_key, 5)
    print(f'Santas secret key needs to be appended with {lowest_number_5_zeroes}.')


def print_solution_part_2(secret_key: str):
    lowest_number_6_zeroes = MD5Hasher.find_lowest_number_with_leading_zeroes_in_md5_hash(secret_key, 6)
    print(f'And now it must be appended with {lowest_number_6_zeroes}.')


if __name__ == "__main__":
    main()
