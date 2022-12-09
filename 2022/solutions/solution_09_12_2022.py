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

    # step-Logik

    def step_right(self):
        head_x = self.head[X]
        head_y = self.head[Y]
        new_head_coordinates = (head_x + 1, head_y)

    def step_left(self):
        pass

    def step_up(self):
        pass

    def step_down(self):
        pass

    # Positionsbools fuer die Tailposition

    def is_tail_on_head(self) -> bool:
        return self.head == self.tail

    def is_tail_left_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.head[X]
        tail_y = self.head[Y]
        return tail_x == head_x - 1 and tail_y == head_y

    def is_tail_right_from_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.head[X]
        tail_y = self.head[Y]
        return tail_x == head_x + 1 and tail_y == head_y

    def is_tail_above_head(self) -> bool:
        head_x = self.head[X]
        head_y = self.head[Y]
        tail_x = self.head[X]
        tail_y = self.head[Y]
        return head_x == tail_x and tail_y == head_y + 1


def main():
    filename_test = "../input_data/09_12_test_data.txt"

    rope = Rope((0, 0), (0, 0))
    print(rope)
    instructions = preprocess_input(filename_test)
    rope.process_one_instruction("RRRR")
    print(rope)


if __name__ == "__main__":
    main()
