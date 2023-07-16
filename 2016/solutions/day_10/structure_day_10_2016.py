from __future__ import annotations

from dataclasses import dataclass

from Utils.errors import IllegalArgumentError


@dataclass()
class Chip:
    value: int

    def __lt__(self, other: Chip) -> bool:
        return self.value < other.value


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
            raise BotSizeError(f"Bot {self.id} already has 2 chips.")

        self.chips.append(chip)
        self.chips.sort()

    def pop_low_chip(self) -> Chip:
        if self.is_empty():
            raise BotSizeError(f"Bot {self.id} has no chips to pop.")

        return self.chips.pop(0)

    def pop_high_chip(self) -> Chip:
        if self.is_empty():
            raise BotSizeError(f"Bot {self.id} has no chips to pop.")

        # If only one chip is present, this is the high chip.
        if len(self.chips) == 1:
            return self.pop_low_chip()

        return self.chips.pop(1)


class BotSizeError(ValueError):
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


class CommandHandler:

    @staticmethod
    def take_chip_from_bot(value: int, bot_id: int):
        pass

    @staticmethod
    def give_chip_to_bot(value: int, bot_id: int):
        pass

    @staticmethod
    def put_chip_to_output_bin(value: int, output_id: int):
        pass


class OutputBin:
    id: int
    chips: list[Chip]

    def __init__(self, id: int):
        self.id = id
        self.chips = []
