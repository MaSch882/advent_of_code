from structure_day_05_2016 import InOrderPasswordCracker


def main():
    print_solution_part_1()


def print_solution_part_1():
    door_key = "reyedfim"
    cracker = InOrderPasswordCracker(door_key, 8, 6)
    password = cracker.crack_password()

    print(f"The password for door {door_key} is {password}.")


if __name__ == "__main__":
    main()
