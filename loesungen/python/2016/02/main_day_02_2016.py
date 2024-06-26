from loesungen.python.utils.input_processing import InputReader
from structure_day_02_2016 import ComplexKeypad
from structure_day_02_2016 import KeypadDecrypter
from structure_day_02_2016 import SimpleKeypad

test_data = ["ULL", "RRDDD", "LURDL", "UUUUD"]

filename = r"..\..\..\..\input_data/2016/2016_02.txt"


def main():
    set_of_commands = InputReader.read_input(filename)

    print_solution_part_1(set_of_commands)  # 52981
    print_solution_part_2(set_of_commands)  # 74CD2


def print_solution_part_1(set_of_commands: list[str]):
    simple_keypad = SimpleKeypad()
    keypad_decrypter = KeypadDecrypter(simple_keypad)
    keypad_decrypter.decrypt_set_of_commands(set_of_commands)
    passcode = keypad_decrypter.build_passcode()
    print(f"The passcode for the bathroom assuming the simple keypad is {passcode}.")


def print_solution_part_2(set_of_commands: list[str]):
    simple_keypad = ComplexKeypad()
    keypad_decrypter = KeypadDecrypter(simple_keypad)
    keypad_decrypter.decrypt_set_of_commands(set_of_commands)
    passcode = keypad_decrypter.build_passcode()
    print(f"The passcode for the bathroom using the complex keypad is {passcode}.")


if __name__ == "__main__":
    main()
