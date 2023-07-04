from Utils import input_processing
from structure_day_08_2016 import CommandExecutor
from structure_day_08_2016 import Screen

filename = r"..\..\input_data\input_day_08_2016.txt"


def main():
    commands = read_input()
    screen = Screen(50, 6)
    executor = CommandExecutor(screen, commands)
    executor.execute_commands()

    screen.print_screen()
    print(f"The number of lit pixels is {screen.count_lit_pixels()}.")  # 128
    print("The message encoded is EOARGPHYAO.")


def read_input() -> list[str]:
    return input_processing.read_input(filename)


if __name__ == "__main__":
    main()
