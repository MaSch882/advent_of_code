import unittest

from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import read_input, count_all_vertical_occurences, \
    solve_part_2
from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import count_all_occurences
from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import count_all_horizontal_occurences
from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import count_all_diagonal_downwards_occurences
from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import count_all_diagonal_upwards_occurences
from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import count_all_occurences
from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import solve_part_1

from advent_of_code.loesungen.python.year_2024.day_04.problem_04 import is_cross


test_lattice_1 = read_input("C:/_Python/advent_of_code/advent_of_code/input/2024_04_test_1.txt")
test_lattice_2 = read_input("C:/_Python/advent_of_code/advent_of_code/input/2024_04_test_2.txt")
test_lattice_3 = read_input("C:/_Python/advent_of_code/advent_of_code/input/2024_04_test_3.txt")


# INPUT

class TestReadInput(unittest.TestCase):
    def test_readTestInput(self):
        actual = test_lattice_1
        expected = ["..X...", ".SAMX.", ".A..A.", "XMAS.S", ".X...."]
        self.assertEqual(actual, expected)

# PART 1

class TestFindAllHorizontalOccurences(unittest.TestCase):
    def test_emptyLattice(self):
        actual = count_all_horizontal_occurences([], "XMAS")
        expected = 0
        self.assertEqual(actual, expected)

    def test_oneRow_WithoutOccurence(self):
        actual = count_all_horizontal_occurences(["..X..."], "XMAS")
        expected = 0
        self.assertEqual(actual, expected)

    def test_oneRow_WithOccurence(self):
        actual = count_all_horizontal_occurences(["XMAS.S"], "XMAS")
        expected = 1
        self.assertEqual(actual, expected)

    def test_oneRow_WithTwoOccurences(self):
        actual = count_all_horizontal_occurences(["XMASXMAS"], "XMAS")
        expected = 2
        self.assertEqual(actual, expected)

    def test_twoRows_WithOccurencesEach(self):
        actual = count_all_horizontal_occurences(["XMAS", "XMAS", "MASX"], "XMAS")
        expected = 2
        self.assertEqual(actual, expected)

class TestFindAllVerticalOccurences(unittest.TestCase):
    def test_emptyLattice(self):
        actual = count_all_vertical_occurences([], "XMAS")
        expected = 0
        self.assertEqual(expected, actual)

    def test_twoFewRows(self):
        actual = count_all_vertical_occurences(["XXXX", "XXXX", "XXXX"], "XMAS")
        expected = 0
        self.assertEqual(expected, actual)

    def test_enoughRowsWithOneOccurence_StartingInFirstRow(self):
        actual = count_all_vertical_occurences(["XXXX", "MXXX", "AXXX", "SXXX"], "XMAS")
        expected = 1
        self.assertEqual(expected, actual)

    def test_enoughRowsWithMultipleOccurences_StartingInFirstRow(self):
        actual = count_all_vertical_occurences(["XXXX", "MMMM", "AAAA", "SSSS"], "XMAS")
        expected = 4
        self.assertEqual(expected, actual)

    def test_enoughRowsWithOneOccurence_StartingInSecondRow(self):
        actual = count_all_vertical_occurences(["JJJJ", "XXXX", "MXXX", "AXXX", "SXXX"], "XMAS")
        expected = 1
        self.assertEqual(expected, actual)

    def test_enoughRowsWithMultipleOccurences_StartingInSecondRow(self):
        actual = count_all_vertical_occurences(["JJJJ", "XXXX", "MMMM", "AADA", "SSSS"], "XMAS")
        expected = 3
        self.assertEqual(expected, actual)

    def test_enoughRowsWithAllOccurences_StartingInSecondRow(self):
        actual = count_all_vertical_occurences(["JJJJ", "XXXX", "MMMM", "AAAA", "SSSS"], "XMAS")
        expected = 4
        self.assertEqual(expected, actual)

class TestFindAllDiagonalDownwardsOccurences(unittest.TestCase):
    def test_emptyLattice(self):
        actual = count_all_diagonal_downwards_occurences([], "XMAS")
        expected = 0
        self.assertEqual(expected, actual)

    def test_enoughRowsWithOneOccurence_StartingInUpperLeft(self):
        actual = count_all_diagonal_downwards_occurences(["XXXX", "XMXX", "XXAX", "XXXS"], "XMAS")
        expected = 1
        self.assertEqual(expected, actual)

    def test_enoughRowsWithMultipleOccurence(self):
        actual = count_all_diagonal_downwards_occurences(["X...X...", ".M...M..", ".XA...A.", "..MS...S", "...A....", "....S..."], "XMAS")
        expected = 3
        self.assertEqual(expected, actual)

class TestFindAllDiagonalUpwardsOccurences(unittest.TestCase):
    def test_emptyLattice(self):
        actual = count_all_diagonal_upwards_occurences([], "XMAS")
        expected = 0
        self.assertEqual(expected, actual)

    def test_enoughRowsWithOneOccurence_StartingInBottomLeft(self):
        actual = count_all_diagonal_upwards_occurences(["XXXS", "XXAX", "XMXX", "XXXX"], "XMAS")
        expected = 1
        self.assertEqual(expected, actual)

    def test_enoughRowsWithMultipleOccurence(self):
        actual = count_all_diagonal_upwards_occurences(["......S", ".....A.", "...SM..", "..AX...", ".M.....", "X......"], "XMAS")
        expected = 2
        self.assertEqual(expected, actual)

class TestTestLattice1(unittest.TestCase):
    def test_testLattice1_horizontal(self):
        actual = count_all_horizontal_occurences(test_lattice_1, "XMAS") + count_all_horizontal_occurences(test_lattice_1, "SAMX")
        expected = 2
        self.assertEqual(expected, actual)

    def test_testLattice1_vertical(self):
        actual = count_all_vertical_occurences(test_lattice_1, "XMAS") + count_all_vertical_occurences(test_lattice_1, "SAMX")
        expected = 1
        self.assertEqual(expected, actual)

    def test_testLattice1_diagonal_downwards(self):
        actual = count_all_diagonal_downwards_occurences(test_lattice_1, "XMAS") + count_all_diagonal_downwards_occurences(test_lattice_1, "SAMX")
        expected = 1
        self.assertEqual(expected, actual)

    def test_testLattice1_diagonal_upwards(self):
        actual = count_all_diagonal_upwards_occurences(test_lattice_1, "XMAS") + count_all_diagonal_upwards_occurences(test_lattice_1, "SAMX")
        expected = 0
        self.assertEqual(expected, actual)

    def test_testLattice1_countAll_forward(self):
        actual = count_all_occurences(test_lattice_1, "XMAS")
        expected = 2
        self.assertEqual(expected, actual)

    def test_testLattice1_countAll_reversed(self):
        actual = count_all_occurences(test_lattice_1, "SAMX")
        expected = 2
        self.assertEqual(expected, actual)

    def test_testLattice1_solvePart1(self):
        actual = solve_part_1(test_lattice_1, "XMAS")
        expected = 4
        self.assertEqual(expected, actual)

class TestTestLattice2(unittest.TestCase):
    def test_testLattice2_solvePart1(self):
        actual = solve_part_1(test_lattice_2, "XMAS")
        expected = 18
        self.assertEqual(expected, actual)

class TestEdgeCases(unittest.TestCase):
    def test_multipleLines(self):
        actual = solve_part_1(["XMXX","ASXX","XXXX","XXXX"], "XMAS")
        expected = 0
        self.assertEqual(expected, actual)

    def test_overlap(self):
        actual = solve_part_1(["XMASAMX"], "XMAS")
        expected = 2
        self.assertEqual(expected, actual)

# PART 2

class TestPermutationsOfXmas(unittest.TestCase):
    def test_MasMas(self):
        actual = is_cross(["MXS", "XAX", "MXS"], 0, 0)
        self.assertTrue(actual)

    def test_MasSam(self):
        actual = is_cross(["MXM", "XAX", "SXS"], 0, 0)
        self.assertTrue(actual)

    def test_SamMas(self):
        actual = is_cross(["SXS", "XAX", "MXM"], 0, 0)
        self.assertTrue(actual)

    def test_SamSam(self):
        actual = is_cross(["SXS", "XAX", "MXM"], 0, 0)
        self.assertTrue(actual)

class TestTestLattice(unittest.TestCase):
    def test_MasMas(self):
        actual = is_cross(["MXS", "XAX", "MXS"], 0, 0)
        self.assertTrue(actual)

    def test_MasSam(self):
        actual = is_cross(["MXM", "XAX", "SXS"], 0, 0)
        self.assertTrue(actual)

    def test_SamMas(self):
        actual = is_cross(["SXS", "XAX", "MXM"], 0, 0)
        self.assertTrue(actual)

    def test_SamSam(self):
        actual = is_cross(["SXS", "XAX", "MXM"], 0, 0)
        self.assertTrue(actual)

class TestTestLattice3(unittest.TestCase):
    def test_testLattice3_solvePart2(self):
        actual = solve_part_2(test_lattice_2)
        expected = 9
        self.assertEqual(expected, actual)
