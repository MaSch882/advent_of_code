from functools import cache
from typing import Any

from treelib import Node, Tree

from framework import input_processing as ip


# Preprocessing
def preprocess_input(filename: str) -> list[list[str]]:
    trimmed_input = ip.read_input(filename)
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
            node_to_jump_to = tree.parent(current_node.identifier)
            if node_to_jump_to is not None:
                current_node = node_to_jump_to
            else:
                current_node = tree.get_node("dir: /")
        except AttributeError:
            current_node = tree.get_node("dir: /")
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


def find_all_directories(file_tree: Tree) -> list[Node]:
    node_iterator = file_tree.filter_nodes(lambda node: node.identifier.startswith("dir"))
    list_of_dir_nodes = list(node_iterator)
    return list_of_dir_nodes


def transform_directories_in_lists(directories: list[Node], file_tree: Tree) -> list[list[Any]]:
    list_of_directories_and_files_included = []
    for directory in directories:
        directory_in_filetree = file_tree.get_node(directory.identifier)
        successors_of_directory = [directory.identifier, directory_in_filetree.successors(file_tree.identifier)]
        list_of_directories_and_files_included.append(successors_of_directory)
    return list_of_directories_and_files_included


def calculate_sizes_of_directories(directories: list[Node], file_tree: Tree) -> dict[str, int]:
    mapping_directory_to_size = {}
    for directory in directories:
        size_of_directory = calculate_size_of_directory(directory, file_tree)
        mapping_directory_to_size.update({directory.identifier: size_of_directory})
    return mapping_directory_to_size


@cache
def calculate_size_of_directory(directory: Node, file_tree: Tree) -> int:
    size_of_directory = 0
    directory_in_filetree = file_tree.get_node(directory.identifier)
    successors_of_directory = directory_in_filetree.successors(file_tree.identifier)

    for structure in successors_of_directory:
        node_in_filetree = file_tree.get_node(structure)
        if node_in_filetree is None:
            continue
        if node_in_filetree.identifier.startswith("file"):
            strip_to_name_and_size = structure.split(";")
            size_of_directory += int(strip_to_name_and_size[1])
        else:
            size_of_directory += calculate_size_of_directory(node_in_filetree, file_tree)
    return size_of_directory


def calculate_sum_of_directories_with_sizes_at_most(mapping_dir_to_size: dict[str, int], upper_bound: int) -> int:
    sum_of_sizes = 0

    for value in mapping_dir_to_size.values():
        if value <= upper_bound:
            sum_of_sizes += value

    return sum_of_sizes


def main():
    print("Solutions to problem 7: [https://adventofcode.com/2022/day/7]")

    filename_test = "../input_data/07_12_2022_test_data.txt"
    filename_problem = "../input_data/07_12_problem_data.txt"

    test_input = preprocess_input(filename_test)
    problem_input = preprocess_input(filename_problem)

    directory_tree = build_directory_tree(problem_input)
    directories_in_tree = find_all_directories(directory_tree)
    sizes_of_directories = calculate_sizes_of_directories(directories_in_tree, directory_tree)
    sum_of_sizes_at_most_100000 = calculate_sum_of_directories_with_sizes_at_most(sizes_of_directories, 100000)
    # directory_tree.show()

    directories = result_directories()
    ids = [d.identifier for d in directories_in_tree]

    print(sum_of_sizes_at_most_100000)

    print("")


def result_directories():
    list_of_strings = ip.read_input("../input_data/07_12_problem_data - Kopie.txt")
    dirs = []
    list_copy = list_of_strings.copy()
    for string in list_copy:
        if not string.startswith("dir"):
            list_of_strings.remove(string)
    list_of_strings.append("dir: /")
    for string in list_of_strings:
        splitted = string.split(" ")
        dirs.append("dir: " + splitted[1])
    return list(set(dirs))


def two_lists_contain_the_same(list_1: list[Any], list_2: list[Any]):
    for item in list_1:
        if item not in list_2:
            print(item)
            return False
    return True


if __name__ == "__main__":
    main()
