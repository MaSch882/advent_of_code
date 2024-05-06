from __future__ import annotations


class Screen:
    pixels: list[list[str]]
    screen_width: int
    screen_height: int

    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height
        self.pixels = self.preparate_empty_screen()

    def preparate_empty_screen(self) -> list[list[str]]:
        width = self.screen_width
        height = self.screen_height
        empty_column = ["."] * width
        matrix = [empty_column.copy() for i in range(0, height)]
        return matrix

    def print_screen(self):
        pixels = self.pixels
        for row in pixels:
            column_string = ""
            for column in row:
                column_string += column
            print(column_string)

    def replace_pixel(self, height: int, width: int, string: str):
        self.pixels[height][width] = string

    def draw_rectangle(self, width: int, height: int):
        for height_index in range(0, height):
            for width_index in range(0, width):
                self.replace_pixel(height_index, width_index, "#")

    def shift_row_by_offset(self, row_index: int, offset: int):
        """
        Counterintuitively implements the command 'rotate row y=A by B'.
        """
        pixels = self.pixels
        affected_row = pixels[row_index].copy()
        for index, char in enumerate(affected_row):
            new_index = (index + offset) % len(affected_row)
            pixels[row_index][new_index] = char

    def shift_column_by_offset(self, column_index: int, offset: int):
        """
        Counterintuitively implements the command 'rotate column x=A by B'.
        """
        pixels = self.pixels
        affected_column = self.extract_column(column_index)
        for index, char in enumerate(affected_column):
            new_index = (index + offset) % len(affected_column)
            pixels[new_index][column_index] = char

    def extract_column(self, column_index: int) -> list[str]:
        pixels = self.pixels
        column = []
        for i in range(0, self.screen_height):
            column.append(pixels[i][column_index])
        return column

    def count_lit_pixels(self):
        number_of_lit_pixels = 0
        for column in self.pixels:
            for row in column:
                if row == "#":
                    number_of_lit_pixels += 1
        return number_of_lit_pixels


class CommandExecutor:
    screen: Screen
    list_of_commands: list[str]

    def __init__(self, screen: Screen, commands: list[str]):
        self.screen = screen
        self.list_of_commands = commands

    def execute_commands(self):
        for command in self.list_of_commands:
            self.execute_one_command(command)

    def execute_one_command(self, command: str):
        if command.startswith("rect"):
            splitted_command = command.split()
            measures = splitted_command[1].split("x")
            self.screen.draw_rectangle(int(measures[0]), int(measures[1]))
        if command.startswith("rotate column"):
            splitted_command = command.split()
            column_number = int(splitted_command[2].split("=")[1])
            offset = int(splitted_command[4])
            self.screen.shift_column_by_offset(column_number, offset)
        if command.startswith("rotate row"):
            splitted_command = command.split()
            row_number = int(splitted_command[2].split("=")[1])
            offset = int(splitted_command[4])
            self.screen.shift_row_by_offset(row_number, offset)
