import unittest

from guard import Guard
from laboratory import Laboratory
from loesungen.python.year_2024.day_06 import directions
from problem_06 import read_input, solve_part_1

test_filename = "H:/git_repos/advent_of_code/2024/06_test.txt"


class TestInputReading(unittest.TestCase):
    def test_testFile(self):
        actual = read_input(test_filename)
        expected = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."
        ]
        self.assertEqual(expected, actual)


class TestGuard(unittest.TestCase):
    def test_initializeGuard(self):
        guard = Guard(13, 27)
        self.assertEqual(13, guard.pos_x)
        self.assertEqual(27, guard.pos_y)
        self.assertEqual([(13, 27)], guard.visited_fields)
        self.assertEqual("U", guard.view_direction)


class TestLaboratory(unittest.TestCase):
    def test_initializeLaboratory(self):
        fields = read_input(test_filename)
        laboratory = Laboratory(fields)

        self.assertEqual(fields, laboratory.fields)
        self.assertEqual("^", laboratory.guard_symbol)
        self.assertEqual("#", laboratory.obstruction_symbol)
        self.assertTrue(laboratory.guard_is_inside)

        self.assertEqual(4, laboratory.guard.pos_x)
        self.assertEqual(6, laboratory.guard.pos_y)
        self.assertEqual([(4, 6)], laboratory.guard.visited_fields)
        self.assertEqual("U", laboratory.guard.view_direction)

    def test_facingObstruction_upwards_noObstruction(self):
        laboratory = Laboratory(fields=["...", ".^."])
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)

    def test_facingObstruction_upwards_obstruction(self):
        laboratory = Laboratory(fields=[".#.", ".^."])
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertTrue(actual)

    def test_facingObstruction_upwards_upperEdge(self):
        laboratory = Laboratory(fields=[".^.", "..."])
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)
        self.assertFalse(laboratory.guard_is_inside)

    def test_facingObstruction_downwards_noObstruction(self):
        laboratory = Laboratory(fields=[".^.", "..."])
        laboratory.guard.view_direction = directions.DOWNWARDS
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)

    def test_facingObstruction_downwards_obstruction(self):
        laboratory = Laboratory(fields=[".^.", ".#."])
        laboratory.guard.view_direction = directions.DOWNWARDS
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertTrue(actual)

    def test_facingObstruction_downwards_lowerEdge(self):
        laboratory = Laboratory(fields=["...", ".^."])
        laboratory.guard.view_direction = directions.DOWNWARDS
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)
        self.assertFalse(laboratory.guard_is_inside)

    def test_facingObstruction_left_noObstruction(self):
        laboratory = Laboratory(fields=[".^"])
        laboratory.guard.view_direction = directions.LEFT
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)

    def test_facingObstruction_left_obstruction(self):
        laboratory = Laboratory(fields=["#^"])
        laboratory.guard.view_direction = directions.LEFT
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertTrue(actual)

    def test_facingObstruction_left_leftEdge(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.LEFT
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)
        self.assertFalse(laboratory.guard_is_inside)

    def test_facingObstruction_right_noObstruction(self):
        laboratory = Laboratory(fields=["^."])
        laboratory.guard.view_direction = directions.RIGHT
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)

    def test_facingObstruction_right_obstruction(self):
        laboratory = Laboratory(fields=["^#"])
        laboratory.guard.view_direction = directions.RIGHT
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertTrue(actual)

    def test_facingObstruction_right_rightEdge(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.RIGHT
        actual = laboratory.is_guard_facing_an_obstruction()
        self.assertFalse(actual)
        self.assertFalse(laboratory.guard_is_inside)

    def test_updateViewDirections_upward(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.update_guard_view_direction()
        self.assertEqual(directions.RIGHT, laboratory.guard.view_direction)

    def test_updateViewDirections_right(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.RIGHT
        laboratory.update_guard_view_direction()
        self.assertEqual(directions.DOWNWARDS, laboratory.guard.view_direction)

    def test_updateViewDirections_downwards(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.DOWNWARDS
        laboratory.update_guard_view_direction()
        self.assertEqual(directions.LEFT, laboratory.guard.view_direction)

    def test_updateViewDirections_left(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.LEFT
        laboratory.update_guard_view_direction()
        self.assertEqual(directions.UPWARDS, laboratory.guard.view_direction)

    def test_updatePosition_upwards_notAtEdge(self):
        laboratory = Laboratory(fields=["...", "...", ".^."])
        laboratory.update_guard_position()
        laboratory.update_guard_position()
        self.assertEqual(1, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertTrue(laboratory.guard_is_inside)
        self.assertEqual([(1, 2), (1, 1)], laboratory.guard.visited_fields)

    def test_updatePosition_upwards_AtEdge(self):
        laboratory = Laboratory(fields=[".^."])
        laboratory.update_guard_position()
        self.assertEqual(1, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertFalse(laboratory.guard_is_inside)

    def test_updatePosition_downwards_notAtEdge(self):
        laboratory = Laboratory(fields=[".^.", "...", "..."])
        laboratory.guard.view_direction = directions.DOWNWARDS
        laboratory.update_guard_position()
        laboratory.update_guard_position()
        self.assertEqual(1, laboratory.guard.pos_x)
        self.assertEqual(2, laboratory.guard.pos_y)
        self.assertTrue(laboratory.guard_is_inside)
        self.assertEqual([(1, 0), (1, 1)], laboratory.guard.visited_fields)

    def test_updatePosition_downwards_AtEdge(self):
        laboratory = Laboratory(fields=[".^."])
        laboratory.guard.view_direction = directions.DOWNWARDS
        laboratory.update_guard_position()
        self.assertEqual(1, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertFalse(laboratory.guard_is_inside)

    def test_updatePosition_left_notAtEdge(self):
        laboratory = Laboratory(fields=["..^"])
        laboratory.guard.view_direction = directions.LEFT
        laboratory.update_guard_position()
        laboratory.update_guard_position()
        self.assertEqual(0, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertTrue(laboratory.guard_is_inside)
        self.assertEqual([(2, 0), (1, 0)], laboratory.guard.visited_fields)

    def test_updatePosition_left_AtEdge(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.LEFT
        laboratory.update_guard_position()
        self.assertEqual(0, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertFalse(laboratory.guard_is_inside)

    def test_updatePosition_right_notAtEdge(self):
        laboratory = Laboratory(fields=["^.."])
        laboratory.guard.view_direction = directions.RIGHT
        laboratory.update_guard_position()
        laboratory.update_guard_position()
        self.assertEqual(2, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertTrue(laboratory.guard_is_inside)
        self.assertEqual([(0, 0), (1, 0)], laboratory.guard.visited_fields)

    def test_updatePosition_right_AtEdge(self):
        laboratory = Laboratory(fields=["^"])
        laboratory.guard.view_direction = directions.RIGHT
        laboratory.update_guard_position()
        self.assertEqual(0, laboratory.guard.pos_x)
        self.assertEqual(0, laboratory.guard.pos_y)
        self.assertFalse(laboratory.guard_is_inside)


class TestPartOne(unittest.TestCase):
    def test(self):
        actual = solve_part_1(Laboratory(read_input(test_filename)))
        expected = 41
        self.assertEqual(expected, actual)
