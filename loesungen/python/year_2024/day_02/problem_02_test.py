import unittest

from advent_of_code.loesungen.python.year_2024.day_02.problem_02 import build_lists
from advent_of_code.loesungen.python.year_2024.day_02.problem_02 import is_safe
from advent_of_code.loesungen.python.year_2024.day_02.problem_02 import is_increasing
from advent_of_code.loesungen.python.year_2024.day_02.problem_02 import is_decreasing
from advent_of_code.loesungen.python.year_2024.day_02.problem_02 import has_correct_difference
from advent_of_code.loesungen.python.year_2024.day_02.problem_02 import solve_part_1


class TestBuildLists(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], build_lists([]))

    def test_oneListOneNumber(self):
        self.assertEqual([[1]], build_lists(["1"]))

    def test_oneListTwoNumbers(self):
        self.assertEqual([[1, 2]], build_lists(["1 2"]))

    def test_twoLists(self):
        self.assertEqual([[1, 2], [3, 4]], build_lists(["1 2", "3 4"]))

    def test_testInput(self):
        numbers = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]
        expected = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]
        actual = build_lists(numbers)
        self.assertEqual(expected, actual)

class TestIsIncreasing(unittest.TestCase):
    def test_empty(self):
        actual = is_increasing([])
        expected = True
        self.assertEqual(expected, actual)

    def test_isIncreasing(self):
        actual = is_increasing([1,2,3,4,5])
        expected = True
        self.assertEqual(expected, actual)

    def test_isNotIncreasing(self):
        actual = is_increasing([2, 1, 3, 4, 5])
        expected = False
        self.assertEqual(expected, actual)

    def test_isNotIncreasingLastNumber(self):
        actual = is_increasing([1, 2, 3, 4, 4])
        expected = False
        self.assertEqual(expected, actual)

class TestIsDecreasing(unittest.TestCase):
    def test_empty(self):
        actual = is_decreasing([])
        expected = True
        self.assertEqual(expected, actual)

    def test_isIncreasing(self):
        actual = is_decreasing([5,4,3,2,1])
        expected = True
        self.assertEqual(expected, actual)

    def test_isNotIncreasing(self):
        actual = is_decreasing([5,4,3,1,2])
        expected = False
        self.assertEqual(expected, actual)

    def test_isNotIncreasingLastNumber(self):
        actual = is_decreasing([5,4,3,2,2])
        expected = False
        self.assertEqual(expected, actual)

class TestHasCorrectDifference(unittest.TestCase):
    def test_empty(self):
        actual = has_correct_difference([])
        expected = True
        self.assertEqual(expected, actual)

    def test_hasCorrect(self):
        actual = has_correct_difference([1,2,3,4,5])
        expected = True
        self.assertEqual(expected, actual)

    def test_hasNotCorrect(self):
        actual = has_correct_difference([1,2,8,10,12])
        expected = False
        self.assertEqual(expected, actual)

class TestIsSafe(unittest.TestCase):
    def test_empty(self):
        actual = is_safe([])
        expected = True
        self.assertEqual(expected, actual)

    def test_inputDate1(self):
        actual = is_safe([7,6,4,2,1])
        expected = True
        self.assertEqual(expected, actual)

    def test_inputDate2(self):
        actual = is_safe([1,2,7,8,9])
        expected = False
        self.assertEqual(expected, actual)

    def test_inputDate3(self):
        actual = is_safe([9,7,6,2,1])
        expected = False
        self.assertEqual(expected, actual)

    def test_inputDate4(self):
        actual = is_safe([1,3,2,4,5])
        expected = False
        self.assertEqual(expected, actual)

    def test_inputDate5(self):
        actual = is_safe([8,6,4,4,1])
        expected = False
        self.assertEqual(expected, actual)

    def test_inputDate6(self):
        actual = is_safe([1,3,6,7,9])
        expected = True
        self.assertEqual(expected, actual)

class TestSolvePart1(unittest.TestCase):
    def test_testInput(self):
        actual = solve_part_1([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]])
        expected = 2
        self.assertEqual(expected, actual)
