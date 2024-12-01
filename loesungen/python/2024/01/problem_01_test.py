import unittest

from problem_01 import build_lists
from problem_01 import calculate_similarity
from problem_01 import calculate_total_distance
from problem_01 import sort_lists


class TestBuildLists(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([[], []], build_lists([]))

    def test_onePair(self):
        self.assertEqual([[3], [4]], build_lists(["3 4"]))

    def test_twoPairs(self):
        self.assertEqual([[3, 13], [4, 21]], build_lists(["3 4", "13 21"]))

    def test_testInput(self):
        actual = build_lists(["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"])
        expected = [[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]
        self.assertEqual(expected, actual)


class TestSortLists(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([[], []], sort_lists([[], []]))

    def test_onePairSorted(self):
        self.assertEqual([[1], [2]], sort_lists([[1], [2]]))

    def test_twoPairsSorted(self):
        self.assertEqual([[1, 2], [3, 4]], sort_lists([[1, 2], [3, 4]]))

    def test_twoPairsUnsorted(self):
        self.assertEqual([[1, 2], [3, 4]], sort_lists([[2, 1], [4, 3]]))

    def test_testInput(self):
        actual = sort_lists(build_lists(["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"]))
        expected = [[1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]]
        self.assertEqual(expected, actual)


class TestCalculateDistance(unittest.TestCase):
    def test_emptyLists(self):
        actual = calculate_total_distance([[], []])
        expected = 0
        self.assertEqual(expected, actual)

    def test_oneElementPerList(self):
        actual = calculate_total_distance([[1], [4]])
        expected = 3
        self.assertEqual(expected, actual)

    def test_oneElementPerListReverseOrder(self):
        actual = calculate_total_distance([[4], [1]])
        expected = 3
        self.assertEqual(expected, actual)

    def test_twoElementsPerList(self):
        actual = calculate_total_distance([[1, 3], [4, 9]])
        expected = 3 + 6
        self.assertEqual(expected, actual)

    def test_testInput(self):
        actual = calculate_total_distance(sort_lists(build_lists(["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"])))
        expected = 11
        self.assertEqual(expected, actual)


class TestCalculateSimilarity(unittest.TestCase):
    def test_emptyLists(self):
        actual = calculate_similarity([[], []])
        expected = 0
        self.assertEqual(expected, actual)

    def test_noMatch(self):
        actual = calculate_similarity([[1], [2, 3, 4]])
        expected = 0
        self.assertEqual(expected, actual)

    def test_oneMatchOneTime(self):
        actual = calculate_similarity([[2], [2, 3, 4]])
        expected = 2
        self.assertEqual(expected, actual)

    def test_oneMatchTwoTimes(self):
        actual = calculate_similarity([[2], [2, 2, 4]])
        expected = 4
        self.assertEqual(expected, actual)

    def test_twoMatchesOneTime(self):
        actual = calculate_similarity([[2, 3], [2, 3, 4]])
        expected = 5
        self.assertEqual(expected, actual)

    def test_testInput(self):
        lists = build_lists(["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"])
        actual = calculate_similarity(lists)
        expected = 31
        self.assertEqual(expected, actual)
