from structure_day_05_2016 import InOrderPasswordCracker, PositionBasedPasswordCracker


def main():
    print_solution_part_1()  # f97c354d
    print_solution_part_2()  # 863dde27


def print_solution_part_1():
    door_key = "reyedfim"
    cracker = InOrderPasswordCracker(door_key, password_length=8)
    password = cracker.crack_password()

    print(f"The password for door {door_key} using InOrderCracking is {password}.")


def print_solution_part_2():
    door_key = "reyedfim"
    cracker = PositionBasedPasswordCracker(door_key, password_length=8, position_bit=6, password_bit=7)
    password = cracker.crack_password()

    print(f"The password for door {door_key} using PositionBasedCracking is {password}.")


if __name__ == "__main__":
    main()
