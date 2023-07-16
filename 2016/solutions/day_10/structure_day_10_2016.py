from __future__ import annotations

from dataclasses import dataclass

from Utils.errors import IllegalArgumentError


@dataclass()
class Chip:
    value: int

    def __lt__(self, other: Chip) -> bool:
        return self.value < other.value


class Bot:
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
    pass
