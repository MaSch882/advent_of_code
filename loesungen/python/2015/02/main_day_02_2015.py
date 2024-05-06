from loesungen.python.utils.input_processing import InputReader

from structure_day_02_2015 import Present, PresentCalculator

filename = r"..\..\..\..\input_data/2015/2015_02.txt"


def main():
    presents = build_presents()

    print_solution_part_1(presents)  # 1586300
    print_solution_part_2(presents)  # 3737498


def build_presents():
    input_strings = InputReader.read_input(filename)
    return unzip_measures_to_presents(input_strings)


def unzip_measures_to_presents(list_of_measures: list[str]) -> list[Present]:
    presents = []
    for measure in list_of_measures:
        measures = extract_measures_from_string(measure)

        width, length, height = measures

        present = Present(width, length, height)
        presents.append(present)
    return presents


def extract_measures_from_string(measure: str) -> list[int]:
    splitted_string = measure.split('x')
    return [int(string) for string in splitted_string]


def print_solution_part_1(presents: list[Present]):
    wrapping_area = PresentCalculator.calculate_total_wrapping_area(presents)
    print(f'The elves should order {wrapping_area} square feet of wrapping paper.')


def print_solution_part_2(presents: list[Present]):
    ribbon_length = PresentCalculator.calculate_total_ribbon_length(presents)
    print(f'The elves should order {ribbon_length} feet of ribbon.')


if __name__ == '__main__':
    main()
