from __future__ import annotations

from dataclasses import dataclass

from Utils.errors import IllegalArgumentError


@dataclass()
class Chip:
    value: int

    def __lt__(self, other: Chip) -> bool:
        return self.value < other.value


@dataclass()
class Bot:
    """
    A class modelling a bot.
    Has an identification number ('id') and a list containing its handled chips ('chips').
    At all points of execution it is guaranteed that the list of chips is sorted:
    chips[0] contains the lowest value, chips[1] contains the highest value.
    """
    id: int
    chips: list[Chip]

    def __init__(self, id: int, chips: list[Chip]):
        self.id = id

        chips.sort()
        self.chips = chips

        if len(chips) > 2:
            raise IllegalArgumentError("Es duerfen maximal zwei Chips uebergeben werden.")

    def is_full(self):
        return len(self.chips) == 2

    def is_empty(self):
        return len(self.chips) == 0

    def receive_chip(self, chip: Chip) -> None:
        if self.is_full():
            raise NumberOfChipsError(f"Bot {self.id} already has 2 chips.")

        self.chips.append(chip)
        self.chips.sort()

    def pop_low_chip(self) -> Chip:
        if self.is_empty():
            raise NumberOfChipsError(f"Bot {self.id} has no chips to pop.")

        return self.chips.pop(0)

    def pop_high_chip(self) -> Chip:
        if self.is_empty():
            raise NumberOfChipsError(f"Bot {self.id} has no chips to pop.")

        # If only one chip is present, this is the high chip.
        if len(self.chips) == 1:
            return self.pop_low_chip()

        return self.chips.pop(1)


class NumberOfChipsError(ValueError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class BotBuilder:

    @staticmethod
    def build_bot_from_values(id: int, value_1: int, value_2: int) -> Bot:
        return BotBuilder.build_bot_from_value_list(id, [value_1, value_2])

    @staticmethod
    def build_bot_from_value_list(id: int, values: list[int]) -> Bot:
        chip_1 = Chip(value=values[0])
        chip_2 = Chip(value=values[1])
        return BotBuilder.build_bot_from_chip_list(id, [chip_1, chip_2])

    @staticmethod
    def build_bot_from_chips(id: int, chip_1: Chip, chip_2: Chip) -> Bot:
        return BotBuilder.build_bot_from_chip_list(id, [chip_1, chip_2])

    @staticmethod
    def build_bot_from_chip_list(id: int, chips: list[Chip]) -> Bot:
        return Bot(id, chips)

    @staticmethod
    def build_bot_from_value(id: int, value: int) -> Bot:
        chip = Chip(value=value)
        return BotBuilder.build_bot_from_chip(id, chip)

    @staticmethod
    def build_bot_from_chip(id: int, chip: Chip) -> Bot:
        return Bot(id, [chip])

    @staticmethod
    def build_bot_from_id(id: int) -> Bot:
        return Bot(id, [])


class OutputBin:
    id: int
    chips: list[Chip]

    def __init__(self, id: int):
        self.id = id
        self.chips = []


@dataclass()
class FactorySimulation:
    bots: list[Bot]
    bot_ids: list[int]
    bins: list[OutputBin]
    bin_ids: list[int]
    commands: list[list[str]]

    def __init__(self, commands: list[str]):
        self.bots = []
        self.bot_ids = []
        self.bins = []
        self.bin_ids = []
        self.commands = InstructionParser.parse_commands(commands)


class InstructionParser:

    @staticmethod
    def parse_commands(commands: list[str]) -> list[list[str]]:
        return [InstructionParser.parse_command(command) for command in commands]

    @staticmethod
    def parse_command(command: str) -> list[str]:
        """
        Parses commands from the given format into a structured target format.

        Given format
            "value {x} goes to bot {n}"
        parses to
            ["assign", int(x), int(n)].

        Given format
            "bot {n} gives low to {entity1} {m} and high to {entity2} {k}"
        parses to
            ["transfer, int(n), str(entity1), int(m), str(entity2), int(k)].

        Invalid formats are ignored.

        :param command: The command using the given format.
        :return: The parsed command using above target format.
        """
        if command.startswith("value"):
            return InstructionParser.parse_assignment(command)

        if command.startswith("bot"):
            return InstructionParser.parse_transfer(command)

        raise IllegalArgumentError(f"Given command starts with the unknown literal '{command.split()[0]}'.")

    @staticmethod
    def parse_assignment(command: str) -> list[str]:
        parsed_command = ["assign"]

        splitted_command = command.split()
        filtered_values = list(filter(lambda x: x.isnumeric(), splitted_command))
        int_values = map(lambda x: int(x), filtered_values)
        parsed_command.extend(int_values)

        return parsed_command

    @staticmethod
    def parse_transfer(command: str) -> list[str]:
        parsed_command = ["transfer"]

        splitted_command = command.split()
        splitted_command.pop(0)

        while len(splitted_command) != 0:
            next_string = splitted_command.pop(0)
            if next_string in ["bot", "output"]:
                parsed_command.append(next_string)
            if next_string.isnumeric():
                parsed_command.append(int(next_string))

        return parsed_command
