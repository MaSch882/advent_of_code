import unittest

from loesungen.python.year_2024.day_07.calibration_equation import CalibrationEquation
from loesungen.python.year_2024.day_07.problem_07 import read_input, build_calibration_equations, solve_part_1, \
    solve_part_2

test_filename = "H:/git_repos/advent_of_code/2024/07_test.txt"


class TestCalibrationEquation(unittest.TestCase):
    def test_initialization(self):
        c = CalibrationEquation("161011: 16 10 13")
        self.assertEqual(161011, c.target_value)
        self.assertEqual([16, 10, 13], c.operands)

    def test_buildAllEquations(self):
        input_strings = read_input(test_filename)
        calibration_equations = build_calibration_equations(input_strings)

        self.assertIn(CalibrationEquation("190: 10 19"), calibration_equations)
        self.assertIn(CalibrationEquation("3267: 81 40 27"), calibration_equations)
        self.assertIn(CalibrationEquation("83: 17 5"), calibration_equations)
        self.assertIn(CalibrationEquation("156: 15 6"), calibration_equations)
        self.assertIn(CalibrationEquation("7290: 6 8 6 15"), calibration_equations)
        self.assertIn(CalibrationEquation("161011: 16 10 13"), calibration_equations)
        self.assertIn(CalibrationEquation("192: 17 8 14"), calibration_equations)
        self.assertIn(CalibrationEquation("21037: 9 7 18 13"), calibration_equations)
        self.assertIn(CalibrationEquation("292: 11 6 16 20"), calibration_equations)

        self.assertEqual(9, len(calibration_equations))

    def test_errorCase(self):
        c = CalibrationEquation("100: 10")
        self.assertRaises(RecursionError, lambda: c.is_solvable_using_addition_and_multiplication(c.operands))

    def test_baseCase_addition_true(self):
        c = CalibrationEquation("100: 90 10")
        self.assertTrue(c.is_solvable_using_addition_and_multiplication(c.operands))

    def test_baseCase_multiplication_true(self):
        c = CalibrationEquation("190: 10 19")
        self.assertTrue(c.is_solvable_using_addition_and_multiplication(c.operands))

    def test_baseCase_false(self):
        c = CalibrationEquation("100: 1 2")
        self.assertFalse(c.is_solvable_using_addition_and_multiplication(c.operands))

    def test_recursion_1(self):
        c = CalibrationEquation("3267: 81 40 27")
        self.assertTrue(c.is_solvable_using_addition_and_multiplication([81, 40, 27]))


class TestPartOne(unittest.TestCase):
    def test(self):
        actual = solve_part_1(build_calibration_equations(read_input(test_filename)))
        expected = 3749
        self.assertEqual(expected, actual)


class TestPartTwo(unittest.TestCase):
    def test(self):
        actual = solve_part_2(build_calibration_equations(read_input(test_filename)))
        expected = 11387
        self.assertEqual(expected, actual)
