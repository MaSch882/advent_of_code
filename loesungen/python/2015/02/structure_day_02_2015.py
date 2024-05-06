from dataclasses import dataclass


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


class PresentCalculator:

    @staticmethod
    def calculate_total_wrapping_area(presents: list[Present]) -> int:
        wrapping_area = 0
        for present in presents:
            wrapping_area += present.calculate_total_wrapping_area()
        return wrapping_area

    @staticmethod
    def calculate_total_ribbon_length(presents: list[Present]) -> int:
        ribbon_length = 0
        for present in presents:
            ribbon_length += present.calculate_total_ribbon_length()
        return ribbon_length
