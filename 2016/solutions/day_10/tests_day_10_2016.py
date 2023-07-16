import unittest

from Utils.errors import IllegalArgumentError
from structure_day_10_2016 import Chip, Bot, NumberOfChipsError, BotBuilder, InstructionParser


class TestChip(unittest.TestCase):

    def test__lt__(self):
        chip_1 = Chip(value=2)
        chip_2 = Chip(value=4)

        vergleich_1_mit_2 = chip_1.__lt__(chip_2)
        vergleich_2_mit_1 = chip_2.__lt__(chip_1)
        vergleich_2_mit_2 = chip_2.__lt__(chip_2)

        self.assertTrue(vergleich_1_mit_2)
        self.assertFalse(vergleich_2_mit_1)
        self.assertFalse(vergleich_2_mit_2)

    def test_sort(self):
        chips = [Chip(value=5), Chip(value=1), Chip(value=3), Chip(value=10), Chip(value=8)]

        chips.sort()

        self.assertEqual(len(chips), 5)
        self.assertTrue(sorted(chips))


class TestBot(unittest.TestCase):

    def test__init__(self):
        bot = Bot(1, [Chip(value=2), Chip(value=3)])

        self.assertEqual(bot.id, 1)

        self.assertTrue(sorted(bot.chips))
        self.assertEqual(bot.chips[0].value, 2)
        self.assertEqual(bot.chips[1].value, 3)

    def test__init__raises_error(self):
        chips = [Chip(1), Chip(2), Chip(3)]

        with self.assertRaises(IllegalArgumentError):
            Bot(1, chips)

    def test_is_full(self):
        bot_1 = Bot(1, [])
        bot_2 = Bot(2, [Chip(10)])
        bot_3 = Bot(3, [Chip(10), Chip(20)])

        self.assertFalse(bot_1.is_full())
        self.assertFalse(bot_2.is_full())
        self.assertTrue(bot_3.is_full())

    def test_is_empty(self):
        bot_1 = Bot(1, [])
        bot_2 = Bot(2, [Chip(10)])
        bot_3 = Bot(3, [Chip(10), Chip(20)])

        self.assertTrue(bot_1.is_empty())
        self.assertFalse(bot_2.is_empty())
        self.assertFalse(bot_3.is_empty())

    def test_receive_chip_valid(self):
        bot_with_no_chip = Bot(1, [])
        bot_with_no_chip.receive_chip(Chip(5))

        self.assertEqual(len(bot_with_no_chip.chips), 1)
        self.assertEqual(bot_with_no_chip.chips[0].value, 5)

        bot_with_one_chip = Bot(1, [Chip(10)])
        bot_with_one_chip.receive_chip(Chip(5))

        self.assertEqual(len(bot_with_one_chip.chips), 2)
        self.assertEqual(bot_with_one_chip.chips[0].value, 5)
        self.assertEqual(bot_with_one_chip.chips[1].value, 10)

    def test_receive_chip_invalid(self):
        bot = Bot(1, [Chip(10), Chip(20)])

        with self.assertRaises(NumberOfChipsError):
            bot.receive_chip(Chip(30))

    def test_pop_low_chip_valid(self):
        bot_with_one_chip = Bot(1, [Chip(10)])
        chip = bot_with_one_chip.pop_low_chip()

        self.assertTrue(bot_with_one_chip.is_empty())
        self.assertIsNotNone(chip)
        self.assertEqual(chip.value, 10)

        bot_with_two_chips = Bot(2, [Chip(10), Chip(20)])
        chip = bot_with_two_chips.pop_low_chip()

        self.assertEqual(len(bot_with_two_chips.chips), 1)
        self.assertEqual(chip.value, 10)

    def test_pop_low_chip_invalid(self):
        bot = Bot(1, [])

        with self.assertRaises(NumberOfChipsError):
            bot.pop_low_chip()

    def test_pop_high_chip_valid(self):
        bot = Bot(1, [Chip(10), Chip(20)])
        chip = bot.pop_high_chip()

        self.assertEqual(len(bot.chips), 1)
        self.assertEqual(chip.value, 20)

        chip = bot.pop_high_chip()

        self.assertEqual(len(bot.chips), 0)
        self.assertEqual(chip.value, 10)

    def test_pop_high_chip_invalid(self):
        bot = Bot(1, [])

        with self.assertRaises(NumberOfChipsError):
            bot.pop_high_chip()


class TestBotBuilder(unittest.TestCase):

    def test_build_bot_from_values(self):
        id = 1
        low_value = 5
        high_value = 17

        bot = BotBuilder.build_bot_from_values(id, low_value, high_value)

        self.assertEqual(bot.id, id)
        self.assertEqual(bot.chips[0].value, low_value)
        self.assertEqual(bot.chips[1].value, high_value)

    def test_build_bot_from_value_list(self):
        id = 1
        low_value = 5
        high_value = 17

        bot = BotBuilder.build_bot_from_value_list(id, [low_value, high_value])

        self.assertEqual(bot.id, id)
        self.assertEqual(bot.chips[0].value, low_value)
        self.assertEqual(bot.chips[1].value, high_value)

    def test_build_from_chips(self):
        id = 1
        low_chip = Chip(value=5)
        high_chip = Chip(value=17)

        bot = BotBuilder.build_bot_from_chips(id, low_chip, high_chip)

        self.assertEqual(bot.id, id)
        self.assertEqual(bot.chips[0].value, low_chip.value)
        self.assertEqual(bot.chips[1].value, high_chip.value)

    def test_build_from_chip_list(self):
        id = 1
        low_chip = Chip(value=5)
        high_chip = Chip(value=17)

        bot = BotBuilder.build_bot_from_chip_list(id, [low_chip, high_chip])

        self.assertEqual(bot.id, id)
        self.assertEqual(bot.chips[0].value, low_chip.value)
        self.assertEqual(bot.chips[1].value, high_chip.value)

    def test_build_from_value(self):
        id = 1
        value = 5

        bot = BotBuilder.build_bot_from_value(id, value)

        self.assertEqual(bot.id, id)
        self.assertEqual(len(bot.chips), 1)
        self.assertEqual(bot.chips[0].value, value)

    def test_build_from_chip(self):
        id = 1
        chip = Chip(value=5)

        bot = BotBuilder.build_bot_from_chip(id, chip)

        self.assertEqual(bot.id, id)
        self.assertEqual(len(bot.chips), 1)
        self.assertEqual(bot.chips[0].value, chip.value)

    def test_build_from_id(self):
        id = 1

        bot = BotBuilder.build_bot_from_id(id)

        self.assertEqual(bot.id, id)
        self.assertIsNotNone(bot.chips)
        self.assertEqual(len(bot.chips), 0)


class TestInstructionParser(unittest.TestCase):

    def test_parse_command_value_assignment(self):
        command = "value 5 goes to bot 2"
        # Expected: ["assign", 5, 2]

        parsed_command = InstructionParser.parse_command(command)

        self.assertEqual(len(parsed_command), 3)
        self.assertEqual(parsed_command[0], "assign")
        self.assertEqual(parsed_command[1], 5)
        self.assertEqual(parsed_command[2], 2)

    def test_parse_command_transfer_chips_bot_bot(self):
        command = "bot 2 gives low to bot 1 and high to bot 0"
        # Excpected: ["transfer", 2, "bot", 1, "bot", 0]

        parsed_command = InstructionParser.parse_command(command)

        self.assertEqual(len(parsed_command), 6)
        self.assertEqual(parsed_command[0], "transfer")
        self.assertEqual(parsed_command[1], 2)
        self.assertEqual(parsed_command[2], "bot")
        self.assertEqual(parsed_command[3], 1)
        self.assertEqual(parsed_command[4], "bot")
        self.assertEqual(parsed_command[5], 0)

    def test_parse_command_transfer_chips_bot_output(self):
        command = "bot 2 gives low to bot 1 and high to output 0"
        # Excpected: ["transfer", 2, "output", 1, "bot", 0]

        parsed_command = InstructionParser.parse_command(command)

        self.assertEqual(len(parsed_command), 6)
        self.assertEqual(parsed_command[0], "transfer")
        self.assertEqual(parsed_command[1], 2)
        self.assertEqual(parsed_command[2], "bot")
        self.assertEqual(parsed_command[3], 1)
        self.assertEqual(parsed_command[4], "output")
        self.assertEqual(parsed_command[5], 0)

    def test_parse_command_transfer_chips_output_bot(self):
        command = "bot 2 gives low to output 1 and high to bot 0"
        # Excpected: ["transfer", 2, "bot", 1, "bot", 0]

        parsed_command = InstructionParser.parse_command(command)

        self.assertEqual(len(parsed_command), 6)
        self.assertEqual(parsed_command[0], "transfer")
        self.assertEqual(parsed_command[1], 2)
        self.assertEqual(parsed_command[2], "output")
        self.assertEqual(parsed_command[3], 1)
        self.assertEqual(parsed_command[4], "bot")
        self.assertEqual(parsed_command[5], 0)

    def test_parse_command_transfer_chips_output_output(self):
        command = "bot 2 gives low to output 1 and high to output 0"
        # Excpected: ["transfer", 2, "bot", 1, "bot", 0]

        parsed_command = InstructionParser.parse_command(command)

        self.assertEqual(len(parsed_command), 6)
        self.assertEqual(parsed_command[0], "transfer")
        self.assertEqual(parsed_command[1], 2)
        self.assertEqual(parsed_command[2], "output")
        self.assertEqual(parsed_command[3], 1)
        self.assertEqual(parsed_command[4], "output")
        self.assertEqual(parsed_command[5], 0)

    def test_parse_command_invalid_command(self):
        command = "do something odd"
        first = command.split()[0]

        with self.assertRaises(IllegalArgumentError) as error:
            InstructionParser.parse_command(command)

        self.assertEqual(error.exception.message, f"Given command starts with the unknown literal '{first}'.")
