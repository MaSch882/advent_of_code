from dataclasses import dataclass

from anytree import Node, RenderTree

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


# Data model


@dataclass()
class Directory:
    type: str
    name: str


@dataclass()
class File(Directory):
    size: int


# Problem 1


def build_directory_tree(commands: list[str]) -> RenderTree:
    parent = Node(Directory(DIRECTORY, "/"))
    dir_tree = RenderTree(parent)
    current_node = parent

    for command in commands:
        update_tree(command, current_node)

    return dir_tree


def update_tree(command, current_node: Node) -> None:
    if command == "Test":
        new_node = Node(File(FILE, "Test", 42), parent=current_node)


def show_tree(tree: RenderTree):
    for pre, fill, node in tree:
        print("%s%s" % (pre, node.name))


def main():
    print("Solutions to problem 7: [https://adventofcode.com/2022/day/7]")

    filename_test = "../input_data/07_12_2022_test_data.txt"
    print(preprocess_input(filename_test))

    print("")


if __name__ == "__main__":
    main()
