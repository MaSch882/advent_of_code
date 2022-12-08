from treelib import Node, Tree

from Utils import input_processing as ip

DIRECTORY = "dir"
FILE = "file"


# Preprocessing
def read_input(filename: str) -> list[str]:
    list_of_strings = ip.read_input_list(filename)
    trimmed_list = ip.trim_newlines(list_of_strings)
    return trimmed_list


def preprocess_input(filename: str) -> list[list[str]]:
    trimmed_input = read_input(filename)
    concatenated_string = concatenate_all_strings_in_given_list(trimmed_input)
    splitted_strings = split_string_at_dollar_and_remove_empty_strings(concatenated_string)
    list_of_commands = split_each_string_of_list_at_empty_string(splitted_strings)
    # Ergebnis dieser Vorverarbeitung ist eine Liste von Listen von Strings. Jede in dieser Liste
    # enthaltene Liste beginnt mit dem Command, alle weiteren Listenelemente sind dann die Antwort
    # bzw. die Parameter dieses Commands.
    # Die Verarbeitung erfolgt in den Methoden zum Aufbau des Dateibaums.
    return list_of_commands


def concatenate_all_strings_in_given_list(list_of_strings: list[str]) -> str:
    concatenated_string = ""
    for string in list_of_strings:
        concatenated_string += string
        concatenated_string += " "
    return concatenated_string


def split_string_at_dollar_and_remove_empty_strings(concatenated_string: str) -> list[str]:
    splitted_concatenated_string_at_dollar_signs = concatenated_string.split("$")
    splitted_concatenated_string_at_dollar_signs.remove("")
    return splitted_concatenated_string_at_dollar_signs


def split_each_string_of_list_at_empty_string(list_of_strings: list[str]) -> list[list[str]]:
    list_of_splitted_strings = []
    for string in list_of_strings:
        splitted = string.split(" ")
        # An erster und letzter Stelle der Liste steht als Ergebnis des Splits ein "". Diese
        # beiden Vorkommen werden hier entfernt.
        splitted.remove("")
        splitted.remove("")
        list_of_splitted_strings.append(splitted)
    return list_of_splitted_strings


# Problem 1


def build_directory_tree(commands: list[list[str]]) -> Tree:
    tree = Tree()
    tree.create_node(identifier="dir: /", tag="dir: /")  # parent
    current_node = tree.get_node("/")

    for command in commands:
        tree, current_node = update_tree(command, tree, current_node)

    return tree


def update_tree(command: list[str], tree: Tree, current_node: Node) -> (Tree, Node):
    if command[0] == "cd":
        tree, current_node = process_command_cd(command, tree, current_node)
    if command[0] == 'ls':
        tree = process_command_ls(command, tree, current_node)
    return tree, current_node


def process_command_cd(command: list[str], tree: Tree, current_node: Node) -> (Tree, Node):
    # command[1] enthaelt den String des Directories, zu dem wir springen wollen.
    dir_to_jump_to = "dir: " + command[1]
    # Wenn command[1] == ".." ist, springen wir zum Vorgaengerdirectory.
    if dir_to_jump_to == "dir: ..":
        try:
            current_node = tree.parent(current_node.identifier)
        except AttributeError:
            return tree, current_node
    # Wenn command[1] als Directory noch nicht vorhanden ist, legen wir es an und springen rein.
    elif not tree.contains(dir_to_jump_to):
        tree.create_node(identifier=dir_to_jump_to, parent=current_node)
        current_node = tree.get_node(dir_to_jump_to)
    # Andernfalls existiert das Directory bereits und wir koennen direkt hinspringen.
    else:
        current_node = tree.get_node(dir_to_jump_to)
    return tree, current_node


def process_command_ls(command: list[str], tree: Tree, current_node: Node) -> (Tree, Node):
    command.remove("ls")
    terminal_output = command

    while len(terminal_output) > 0:
        last_output = terminal_output.pop()
        second_last_output = terminal_output.pop()
        structure = [second_last_output, last_output]
        tree = add_structure_to_tree(structure, tree, current_node)

    return tree


def add_structure_to_tree(structure: list[str], tree: Tree, current_node: Node) -> (Tree, Node):
    if structure[0] == "dir":
        tree = add_directory_to_tree(structure, tree, current_node)
    else:
        tree = add_file_to_tree(structure, tree, current_node)
    return tree


def add_directory_to_tree(structure: list[str], tree: Tree, current_node: Node) -> Tree:
    node_string = "dir: " + structure[1]
    if not tree.contains(node_string):
        tree.create_node(identifier=node_string, parent=current_node)
    return tree


def add_file_to_tree(structure: list[str], tree: Tree, current_node: Node) -> Tree:
    node_string = "file: " + structure[1] + "; " + structure[0]
    if not tree.contains(node_string):
        tree.create_node(identifier=node_string, parent=current_node)
    return tree


def main():
    print("Solutions to problem 7: [https://adventofcode.com/2022/day/7]")

    filename_test = "../input_data/07_12_2022_test_data.txt"
    filename_problem = "../input_data/07_12_2022_problem_data.txt"

    processed_input = preprocess_input(filename_problem)

    directory_tree = build_directory_tree(processed_input)
    directory_tree.show()

    print("")


if __name__ == "__main__":
    main()
