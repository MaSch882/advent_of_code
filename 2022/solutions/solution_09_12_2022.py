from dataclasses import dataclass, field

from Utils import input_processing as ip


def preprocess_input(filename: str) -> list[str]:
    list_of_inputs = ip.read_input(filename)
    processed_strings = []
    for string in list_of_inputs:
        splitted_string = string.split(" ")
        direction = splitted_string[0]
        number_of_steps = int(splitted_string[1])
        processed_string = ""
        for i in range(0, number_of_steps):
            processed_string += direction
        processed_strings.append(processed_string)
    return processed_strings


# Data model

X = 0
Y = 1


@dataclass()
class Rope:
    head: tuple[int, int] = field(default_factory=list)
    tail: tuple[int, int] = field(default_factory=list)
    visited_positions: set[tuple[int, int]] = field(default_factory=list)

    def equals_softly(self, other):
        return self.head == other.head and self.tail == other.tail

    def __post_init__(self):
        self.visited_positions = {self.tail}

    def update_visited_positions(self, position: tuple[int, int]):
        self.visited_positions.add(position)

    def process_one_instruction(self, instruction: str):
        if "R" in instruction:
            for char in instruction:
                self.step_right()
        if "L" in instruction:
            for char in instruction:
                self.step_left()
        if "U" in instruction:
            for char in instruction:
                self.step_up()
        if "D" in instruction:
            for char in instruction:
                self.step_down()

    # step-Logik

    def step_right(self) -> None:
        head_x = self.head[X]
        head_y = self.head[Y]

        new_head_x = head_x + 1

        if self.is_tail_on_head() or self.is_tail_right_from_head() or \
                self.is_tail_below_from_head() or self.is_tail_above_from_head() or \
                self.is_tail_right_below_from_head() or self.is_tail_right_above_from_head():
            self.update_head(new_head_x, head_y)
        elif self.is_tail_left_from_head():
            self.update(new_head_x, head_y, head_x, head_y)
        elif self.is_tail_left_above_from_head():
            self.update(new_head_x, head_y, head_x, head_y)
        elif self.is_tail_left_below_from_head():
            self.update(new_head_x, head_y, head_x, head_y)

        self.update_visited_positions(self.tail)

    def step_left(self):
        head_x = self.head[X]
        head_y = self.head[Y]

        new_head_x = head_x - 1

        if self.is_tail_on_head() or self.is_tail_left_from_head() or \
                self.is_tail_below_from_head() or self.is_tail_above_from_head() or \
                self.is_tail_left_above_from_head() or self.is_tail_left_below_from_head():
            self.update_head(new_head_x, head_y)
        elif self.is_tail_right_from_head():
            self.update(new_head_x, head_y, head_x, head_y)
        elif self.is_tail_right_below_from_head():
            self.update(new_head_x, head_y, head_x, head_y)
        elif self.is_tail_right_above_from_head():
            self.update(new_head_x, head_y, head_x, head_y)

        self.update_visited_positions(self.tail)

    def step_up(self):
        head_x = self.head[X]
        head_y = self.head[Y]

        new_head_y = head_y + 1

        if self.is_tail_on_head() or self.is_tail_left_from_head() or \
                self.is_tail_right_from_head() or self.is_tail_above_from_head() or \
                self.is_tail_left_above_from_head() or self.is_tail_right_above_from_head():
            self.update_head(head_x, new_head_y)
        elif self.is_tail_below_from_head():
            self.update(head_x, new_head_y, head_x, head_y)
        elif self.is_tail_left_below_from_head():
            self.update(head_x, new_head_y, head_x, head_y)
        elif self.is_tail_right_below_from_head():
            self.update(head_x, new_head_y, head_x, head_y)

        self.update_visited_positions(self.tail)

    def step_down(self):
        head_x = self.head[X]
        head_y = self.head[Y]

        new_head_y = head_y - 1

        if self.is_tail_on_head() or self.is_tail_left_from_head() or \
                self.is_tail_right_from_head() or self.is_tail_below_from_head() or \
                self.is_tail_left_below_from_head() or self.is_tail_right_below_from_head():
            self.update_head(head_x, new_head_y)
        elif self.is_tail_above_from_head():
            self.update(head_x, new_head_y, head_x, head_y)
        elif self.is_tail_left_above_from_head():
            self.update(head_x, new_head_y, head_x, head_y)
        elif self.is_tail_right_above_from_head():
            self.update(head_x, new_head_y, head_x, head_y)

        self.update_visited_positions(self.tail)

    # Positionsupdates - Hilfsmethoden

    def update(self, new_x_head: int, new_y_head: int, new_x_tail: int, new_y_tail: int):
        self.update_head(new_x_head, new_y_head)
        self.update_tail(new_x_tail, new_y_tail)

    def update_head(self, new_x: int, new_y: int):
        self.head = (new_x, new_y)

    def update_tail(self, new_x: int, new_y: int):
        self.tail = (new_x, new_y)

    # Positionsbools fuer die Tailposition

    def is_tail_on_head(self) -> bool:
        return self.head == self.tail

    def is_tail_left_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x - 1 and tail_y == head_y

    def is_tail_right_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x + 1 and tail_y == head_y

    def is_tail_above_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x and tail_y == head_y + 1

    def is_tail_below_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x and tail_y == head_y - 1

    def is_tail_left_above_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x - 1 and tail_y == head_y + 1

    def is_tail_right_above_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x + 1 and tail_y == head_y + 1

    def is_tail_left_below_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x - 1 and tail_y == head_y - 1

    def is_tail_right_below_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.tail[X]
        tail_y = self.tail[Y]
        return tail_x == head_x + 1 and tail_y == head_y - 1


def process_instructions(rope: Rope, instructions: list[str]) -> None:
    for instruction in instructions:
        rope.process_one_instruction(instruction)


def count_visited_tail_positions(filename: str):
    rope = Rope((0, 0), (0, 0))
    instructions = preprocess_input(filename)
    process_instructions(rope, instructions)
    return len(rope.visited_positions)


def main():
    filename_test = "../input_data/09_12_test_data.txt"
    filename_problem = "../input_data/09_12_problem_data.txt"

    number_of_visited_tail_positions = count_visited_tail_positions(filename_problem)

    print(f'The number of positions visited by the tail is {number_of_visited_tail_positions}.')


if __name__ == "__main__":
    main()
