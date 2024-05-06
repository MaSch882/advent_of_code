from dataclasses import dataclass

from loesungen.python.utils.input_processing import InputReader as ip

INTERESTING_CYLCE_NUMBERS = [20, 60, 100, 140, 180, 220]


# Data model


@dataclass()
class State:
    cycle: int
    register_value: int
    signal_strength: int
    crt_position: int
    crt_output: str

    def process_one_command(self, command: str):
        if command.startswith("noop"):
            self.advance_cycle_counter_by_one_and_check_interesting_cycle_numbers()
        if command.startswith("addx"):
            self.process_add_x(command)

    def process_add_x(self, command: str):
        self.advance_cycle_counter_by_one_and_check_interesting_cycle_numbers()
        self.advance_cycle_counter_by_one_and_check_interesting_cycle_numbers()
        self.register_value += int(command.split(" ")[1])

    def update_signal_strength(self):
        self.signal_strength += self.cycle * self.register_value

    def advance_cycle_counter_by_one_and_check_interesting_cycle_numbers(self):
        self.cycle += 1
        self.render_crt_output_pixel()
        if self.cycle in INTERESTING_CYLCE_NUMBERS:
            self.update_signal_strength()

    def render_crt_output_pixel(self):
        register_value = self.register_value
        if self.crt_position in range(register_value - 1, register_value + 2):
            self.crt_output += "#"
        else:
            self.crt_output += '.'
        self.crt_position += 1
        if self.crt_position >= 40:
            self.crt_position = 0


# Problem 1


def process_list_of_commands(state: State, list_of_commands: list[str]):
    for command in list_of_commands:
        state.process_one_command(command)


# Problem 2

def render_crt_image(state: State):
    crt_output = state.crt_output
    for i in range(1, 7):
        crt_row = crt_output[(i - 1) * 40:i * 40]
        print(crt_row)


def main():
    print("Solutions to problem 10: [https://adventofcode.com/2022/day/10]")

    filename = r"..\..\..\..\input_data/2022/2022_10.txt"

    list_of_commands = ip.read_input(filename)
    state = State(cycle=0, register_value=1, signal_strength=0, crt_position=0, crt_output="")

    process_list_of_commands(state, list_of_commands)
    print(f'The sum of interesting signal strengths is {state.signal_strength}.')

    print(f'The rendered image contains the letters RKPJBPLA:')
    render_crt_image(state)

    print("")


if __name__ == "__main__":
    main()
