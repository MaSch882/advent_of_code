from framework.input_processing import InputReader
from structure_day_03_2016 import Triangle
from structure_day_03_2016 import TriangleCounter

filename = r"..\..\input_data\input_day_03_2016.txt"


def main():
    triangles_horizontally = build_triangles_from_input_horizontally(filename)
    triangles_vertically = build_triangles_from_input_vertically(filename)

    print_solution_part_1(triangles_horizontally)  # 1050
    print_solution_part_2(triangles_vertically)  # 1921


def print_solution_part_1(triangles: list[Triangle]):
    counter = TriangleCounter(triangles)
    counter.count_possible_triangles()
    number_of_valid_triangles = counter.number_of_possible_triangles

    print(f"There are {number_of_valid_triangles} possible horizontal triangles.")


def print_solution_part_2(triangles: list[Triangle]):
    counter = TriangleCounter(triangles)
    counter.count_possible_triangles()
    number_of_valid_triangles = counter.number_of_possible_triangles

    print(f"There are {number_of_valid_triangles} possible vertical triangles.")


def build_triangles_from_input_vertically(name: str) -> list[Triangle]:
    # Einlesen und an ',' splitten
    inputs = InputReader.read_input(name)
    inputs = [x.split() for x in inputs]

    # Innere Listen auflösen und in ints konvertieren
    raw_inputs = denest_list_entries_and_convert_to_int(inputs)

    # Nach Spalten in Listen einsortieren
    inputs_first_row, inputs_second_row, inputs_third_row = extract_row_inputs(raw_inputs)

    # Listen in Dreier-Gruppen gruppieren
    sidelengths_first_row = group_list_by_three(inputs_first_row)
    sidelengths_second_row = group_list_by_three(inputs_second_row)
    sidelengths_third_row = group_list_by_three(inputs_third_row)

    # Dreiecke aus den Listen gießen
    triangles = []
    for sidelength_list in [sidelengths_first_row, sidelengths_second_row, sidelengths_third_row]:
        for triple in sidelength_list:
            triangles.append(Triangle(triple))

    return triangles


def denest_list_entries_and_convert_to_int(inputs) -> list[int]:
    raw_inputs = []
    for triple in inputs:
        for entry in triple:
            raw_inputs.append(int(entry))
    return raw_inputs


def extract_row_inputs(raw_inputs) -> (list[int], list[int], list[int]):
    inputs_first_row = []
    inputs_second_row = []
    inputs_third_row = []
    for index, element in enumerate(raw_inputs):
        if index % 3 == 0:
            inputs_first_row.append(element)
        if index % 3 == 1:
            inputs_second_row.append(element)
        if index % 3 == 2:
            inputs_third_row.append(element)
    return inputs_first_row, inputs_second_row, inputs_third_row


def group_list_by_three(list_to_group: list[int]) -> list[list[int]]:
    return [list_to_group[i:i + 3] for i in range(0, len(list_to_group), 3)]


def build_triangles_from_input_horizontally(name: str) -> list[Triangle]:
    inputs = InputReader.read_input(name)
    sidelength_tuples_as_strings = [x.split() for x in inputs]

    sidelength_tuples = []
    for string_tuple in sidelength_tuples_as_strings:
        sidelength_tuples.append([int(x) for x in string_tuple])

    triangles = [Triangle(sidelengths) for sidelengths in sidelength_tuples]

    return triangles


if __name__ == "__main__":
    main()
