from Utils import input_processing as ip


def read_input(filename: str) -> list[str]:
    list_of_inputs = ip.read_input_list(filename)
    trimmed_list = ip.trim_newlines(list_of_inputs)
    return trimmed_list


def convert_list_of_strings_in_matrix(list_of_strings: list[str]) -> list[list[int]]:
    converted = []
    for string in list_of_strings:
        integers = [int(x) for x in string]
        converted.append(integers)
    return converted


# Problem 1


def is_visible(x_coordinate: int, y_coordinate: int, tree_matrix: list[list[int]]) -> bool:
    number_of_columns = len(tree_matrix)
    number_of_rows = len(tree_matrix[0])
    tree_height = tree_matrix[x_coordinate][y_coordinate]

    if is_edge_tree(x_coordinate, y_coordinate, number_of_rows, number_of_columns):
        return True

    if is_visible_from_left(x_coordinate, y_coordinate, tree_matrix, tree_height):
        return True

    if is_visible_from_right(x_coordinate, y_coordinate, tree_matrix, tree_height):
        return True

    if is_visible_from_top(x_coordinate, y_coordinate, tree_matrix, tree_height):
        return True

    if is_visible_from_down(x_coordinate, y_coordinate, tree_matrix, tree_height):
        return True

    return False


def is_edge_tree(x_coordinate: int, y_coordinate: int, rows: int, columns: int) -> bool:
    return x_coordinate == 0 or y_coordinate == 0 or x_coordinate == rows - 1 or y_coordinate == columns - 1


def is_visible_from_left(x_coordinate, y_coordinate, tree_matrix, tree_height: int):
    for i in range(0, y_coordinate):
        compare_height = tree_matrix[x_coordinate][i]
        if compare_height >= tree_height:
            return False
    return True


def is_visible_from_right(x_coordinate, y_coordinate, tree_matrix, tree_height):
    for i in range(y_coordinate + 1, len(tree_matrix)):
        compare_height = tree_matrix[x_coordinate][i]
        if compare_height >= tree_height:
            return False
    return True


def is_visible_from_top(x_coordinate, y_coordinate, tree_matrix, tree_height):
    for i in range(0, x_coordinate):
        compare_height = tree_matrix[i][y_coordinate]
        if compare_height >= tree_height:
            return False
    return True


def is_visible_from_down(x_coordinate, y_coordinate, tree_matrix, tree_height):
    for i in range(x_coordinate + 1, len(tree_matrix[0])):
        compare_height = tree_matrix[i][y_coordinate]
        if compare_height >= tree_height:
            return False
    return True


def count_visible_tree(tree_matrix: list[list[int]]) -> int:
    number_of_visible_trees = 0

    number_of_rows = len(tree_matrix)
    number_of_columns = len(tree_matrix[0])

    for i in range(0, number_of_rows):
        for j in range(0, number_of_columns):
            if is_visible(i, j, tree_matrix):
                number_of_visible_trees += 1
    return number_of_visible_trees


def main():
    print("Solutions to problem 8: [https://adventofcode.com/2022/day/8]")

    filename_test = "../input_data/08_12_test_data.txt"
    filename_problem = "../input_data/08_12_problem_data.txt"

    tree_input = read_input(filename_problem)
    tree_matrix = convert_list_of_strings_in_matrix(tree_input)
    number_of_visible_trees = count_visible_tree(tree_matrix)
    print(f'The number of given trees in the forestation is {number_of_visible_trees}.')

    print("")


if __name__ == "__main__":
    main()
