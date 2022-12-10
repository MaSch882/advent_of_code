from dataclasses import dataclass

from Utils import input_processing as ip

INTERESTING_CYLCE_NUMBERS = [20, 60, 100, 140, 180, 220]


# Data model


@dataclass()
class State:
    cycle: int
    register_value: int
    signal_strength: int

    def process_one_command(self, command: str):
        if command.startswith("noop"):
            self.advance_cylce_counter_by_one_and_check_interesting_cylce_numbers()
        if command.startswith("addx"):
            self.process_add_x(command)

    def process_add_x(self, command: str):
        self.advance_cylce_counter_by_one_and_check_interesting_cylce_numbers()
        self.advance_cylce_counter_by_one_and_check_interesting_cylce_numbers()
        self.register_value += int(command.split(" ")[1])

    def update_signal_strength(self):
        self.signal_strength += self.cycle * self.register_value

    def advance_cylce_counter_by_one_and_check_interesting_cylce_numbers(self):
        self.cycle += 1
        if self.cycle in INTERESTING_CYLCE_NUMBERS:
            self.update_signal_strength()


# Problem 1


def process_list_of_commands(state: State, list_of_commands: list[str]):
    for command in list_of_commands:
        state.process_one_command(command)


def main():
    filename_test = "../input_data/10_12_test_data.txt"
    filename_problem = "../input_data/10_12_problem_data.txt"

    list_of_commands = ip.read_input(filename_problem)
    state = State(cycle=0, register_value=1, signal_strength=0)

    process_list_of_commands(state, list_of_commands)

    print(state)


if __name__ == "__main__":
    main()
