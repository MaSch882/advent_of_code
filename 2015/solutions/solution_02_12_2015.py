from dataclasses import dataclass

import Utils.input_processing as ip


@dataclass()
class Present:
    width: int
    length: int
    height: int

    def organize_measures_as_list(self) -> list[int]:
        return [self.width, self.length, self.height]

    def calculate_volume(self) -> int:
        return self.width * self.height * self.length

    def calculate_surface_area(self) -> int:
        width = self.width
        length = self.length
        height = self.height
        return 2 * width * length + 2 * width * height + 2 * length * height

    def calculate_additional_wrapping_surface(self) -> int:
        sorted_measures = self.sort_measures()
        return sorted_measures[0] * sorted_measures[1]

    def calculate_ribbon_length(self) -> int:
        sorted_measures = self.sort_measures()
        return 2 * sorted_measures[0] + 2 * sorted_measures[1]

    def calculate_total_wrapping_area(self):
        return self.calculate_surface_area() + self.calculate_additional_wrapping_surface()

    def calculate_total_ribbon_length(self):
        return self.calculate_ribbon_length() + self.calculate_volume()

    def sort_measures(self) -> list[int]:
        sorted_measures = self.organize_measures_as_list()
        sorted_measures.sort()
        return sorted_measures


def calculate_total_wrapping_area_for_all_presents() -> int:
    list_of_all_measures = ip.read_input_list("../input_data/02_12_problem_data.txt")
    trimmed_list = ip.trim_newlines(list_of_all_measures)
    presents = unzip_measures_to_presents(trimmed_list)
    return calculate_total_wrapping_area(presents)


def calculate_total_ribbon_length_for_all_presents() -> int:
    list_of_all_measures = ip.read_input_list("../input_data/02_12_problem_data.txt")
    trimmed_list = ip.trim_newlines(list_of_all_measures)
    presents = unzip_measures_to_presents(trimmed_list)
    return calculate_total_ribbon_length(presents)


def unzip_measures_to_presents(list_of_measures: list[str]) -> list[Present]:
    presents = []
    for measure in list_of_measures:
        measures = extract_measures_from_string(measure)

        width = measures[0]
        length = measures[1]
        height = measures[2]

        present = Present(width, length, height)
        presents.append(present)
    return presents


def extract_measures_from_string(measure: str) -> list[int]:
    splitted_string = measure.split('x')
    return [int(string) for string in splitted_string]


def calculate_total_wrapping_area(presents: list[Present]) -> int:
    wrapping_area = 0
    for present in presents:
        wrapping_area += present.calculate_total_wrapping_area()
    return wrapping_area


def calculate_total_ribbon_length(presents: list[Present]) -> int:
    ribbon_length = 0
    for present in presents:
        ribbon_length += present.calculate_total_ribbon_length()
    return ribbon_length


def main():
    wrapping_area = calculate_total_wrapping_area_for_all_presents()
    print(f'The elves should order {wrapping_area} square feet of wrapping paper.')
    ribbon_length = calculate_total_ribbon_length_for_all_presents()
    print(f'The elves should order {ribbon_length} feet of ribbon.')
    pass


if __name__ == '__main__':
    main()
