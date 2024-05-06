class Triangle:
    side_a: int
    side_b: int
    side_c: int

    def __init__(self, sidelengths: list[int, int, int]):
        self.side_a = sidelengths[0]
        self.side_b = sidelengths[1]
        self.side_c = sidelengths[2]


class TriangleCounter:
    triangles: list[Triangle]
    number_of_possible_triangles: int

    def __init__(self, triangles_to_check: list[Triangle]):
        self.triangles = triangles_to_check
        self.number_of_possible_triangles = 0

    def count_possible_triangles(self):
        for triangle in self.triangles:
            if self.is_possible_triangle(triangle):
                self.number_of_possible_triangles += 1

    @staticmethod
    def is_possible_triangle(triangle: Triangle) -> bool:
        a = triangle.side_a
        b = triangle.side_b
        c = triangle.side_c

        return a + b > c and a + c > b and b + c > a
