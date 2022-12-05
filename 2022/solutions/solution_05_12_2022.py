from Utils import input_processing as ip


def read_input(filename: str) -> list[str]:
    list_of_inputs = ip.read_input_list(filename)
    trimmed_list = ip.trim_newlines(list_of_inputs)
    return trimmed_list


# Problem 1


def transform_input_in_integers(list_of_strings: list[str]) -> list[list[int]]:
    list_of_splitted_strings = []
    for string in list_of_strings:
        list_of_splitted_strings.append(string.split())
    list_of_integers = []
    for current_list in list_of_splitted_strings:
        list_of_integers.append([int(x) for x in current_list])
    return list_of_integers


#         [G]         [D]     [Q]
# [P]     [T]         [L] [M] [Z]
# [Z] [Z] [C]         [Z] [G] [W]
# [M] [B] [F]         [P] [C] [H] [N]
# [T] [S] [R]     [H] [W] [R] [L] [W]
# [R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
# [C] [N] [H] [R] [N] [H] [D] [J] [Q]
# [N] [D] [M] [G] [Z] [F] [W] [S] [S]
#  1   2   3   4   5   6   7   8   9

STACK_1 = ["N", "C", "R", "T", "M", "Z", "P"]
STACK_2 = ["D", "N", "T", "S", "B", "Z"]
STACK_3 = ["M", "H", "Q", "R", "F", "C", "T", "G"]
STACK_4 = ["G", "R", "Z"]
STACK_5 = ["Z", "N", "R", "H"]
STACK_6 = ["F", "H", "S", "W", "P", "Z", "L", "D"]
STACK_7 = ["W", "D", "Z", "R", "C", "G", "M"]
STACK_8 = ["S", "J", "F", "L", "H", "W", "Z", "Q"]
STACK_9 = ["S", "Q", "P", "W", "N"]

STACKS = [None, STACK_1, STACK_2, STACK_3, STACK_4, STACK_5, STACK_6, STACK_7, STACK_8, STACK_9]
INITIAL_STACKS = [None, STACK_1.copy(), STACK_2.copy(), STACK_3.copy(), STACK_4.copy(), STACK_5.copy(), STACK_6.copy(),
                  STACK_7.copy(), STACK_8.copy(), STACK_9.copy()]


def remove_and_return_last_item(list_of_strings: list[str]) -> str:
    return list_of_strings.pop()


def move_crates_from_stack_to_stack(number_of_crates: int, stack_start: int, stack_end: int) -> None:
    stack_to_move_from = STACKS[stack_start]
    stack_to_move_to = STACKS[stack_end]
    for i in range(1, number_of_crates + 1):
        current_item = remove_and_return_last_item(stack_to_move_from)
        stack_to_move_to.append(current_item)


def perform_crane_transitions(instructions: list[list[int]]) -> None:
    for instruction in instructions:
        number_of_crates = instruction[0]
        stack_start = instruction[1]
        stack_end = instruction[2]
        move_crates_from_stack_to_stack(number_of_crates, stack_start, stack_end)


def calculate_message_at_the_end() -> str:
    message_string = ""
    for stack in STACKS:
        if stack is None:
            continue
        message_string += stack.pop()
    return message_string


def perform_all_crane_instructions_and_calculate_message(filename: str) -> str:
    input_data = read_input(filename)
    crane_instructions = transform_input_in_integers(input_data)
    perform_crane_transitions(crane_instructions)
    message = calculate_message_at_the_end()
    return message


# Problem 2

def remove_and_return_last_items(list_of_strings: list[str], number_of_elements: int) -> list[str]:
    removed_elements = []
    for i in range(1, number_of_elements + 1):
        removed_elements.append(remove_and_return_last_item(list_of_strings))
    removed_elements.reverse()
    return removed_elements


def move_crates_together_from_stack_to_stack(number_of_crates: int, stack_start: int, stack_end: int) -> None:
    stack_to_move_from = STACKS[stack_start]
    stack_to_move_to = STACKS[stack_end]
    moved_items = remove_and_return_last_items(stack_to_move_from, number_of_crates)
    for item in moved_items:
        stack_to_move_to.append(item)


def perform_crane_transitions_together(instructions: list[list[int]]) -> None:
    for instruction in instructions:
        number_of_crates = instruction[0]
        stack_start = instruction[1]
        stack_end = instruction[2]
        move_crates_together_from_stack_to_stack(number_of_crates, stack_start, stack_end)


def perform_all_crane_instructions_together_and_calculate_message(filename: str) -> str:
    input_data = read_input(filename)
    crane_instructions = transform_input_in_integers(input_data)
    perform_crane_transitions_together(crane_instructions)
    message = calculate_message_at_the_end()
    return message


def revert_changes_on_stacks() -> None:
    for i, stack in enumerate(STACKS):
        stack = INITIAL_STACKS[i]
        STACKS[i] = stack


def main():
    print("Solutions to problem 5: [https://adventofcode.com/2022/day/5]")

    message = perform_all_crane_instructions_and_calculate_message("../input_data/05_12_problem_data.txt")
    print(f'The message delivered after all crane instructions are performed is {message}.')

    revert_changes_on_stacks()

    message_with_new_crane = perform_all_crane_instructions_together_and_calculate_message(
        "../input_data/05_12_problem_data.txt")
    print(
        f'The message delivered after all crane instructions are performed on the new model is {message_with_new_crane}.')

    print("")


if __name__ == "__main__":
    main()
