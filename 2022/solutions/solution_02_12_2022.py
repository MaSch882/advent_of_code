from dataclasses import dataclass

import framework.input_processing as ip

POINTS_FOR_LOSE = 0
POINTS_FOR_DEUCE = 3
POINTS_FOR_WIN = 6


@dataclass()
class RockPaperScissor:
    opponents_figure: str
    players_figure: str

    def convert_figures_in_readable_strings_according_decrypting_player_to_figures(self) -> None:
        self.convert_opponent_figures_in_readable_strings()
        self.convert_player_figures_in_readable_strings()

    def convert_figures_in_readable_strings_according_decrypting_player_to_game_output(self) -> None:
        self.convert_opponent_figures_in_readable_strings()
        self.convert_player_figures_in_readable_strings_according_game_output()

    def convert_opponent_figures_in_readable_strings(self) -> None:
        if self.opponents_figure == 'A':
            self.opponents_figure = 'Rock'
        if self.opponents_figure == 'B':
            self.opponents_figure = 'Paper'
        if self.opponents_figure == 'C':
            self.opponents_figure = 'Scissors'

    def convert_player_figures_in_readable_strings(self) -> None:
        if self.players_figure == 'X':
            self.players_figure = 'Rock'
        if self.players_figure == 'Y':
            self.players_figure = 'Paper'
        if self.players_figure == 'Z':
            self.players_figure = 'Scissors'

    def convert_player_figures_in_readable_strings_according_game_output(self) -> None:
        if self.players_figure == 'X':
            self.players_figure = 'Lose'
        if self.players_figure == 'Y':
            self.players_figure = 'Deuce'
        if self.players_figure == 'Z':
            self.players_figure = 'Win'

    def calculate_players_total_points_in_this_game(self) -> int:
        points = 0
        points += self.calculate_players_points_for_chosen_figure()
        points += self.calculate_players_points_for_result_of_this_game()
        return points

    def calculate_players_points_for_chosen_figure(self) -> int:
        if self.players_figure == 'Rock':
            return 1
        if self.players_figure == 'Paper':
            return 2
        if self.players_figure == 'Scissors':
            return 3

    def calculate_players_points_for_result_of_this_game(self) -> int:
        opponents_figure = self.opponents_figure
        players_figure = self.players_figure

        if opponents_figure == 'Rock' and players_figure == 'Rock':
            return POINTS_FOR_DEUCE
        if opponents_figure == 'Rock' and players_figure == 'Paper':
            return POINTS_FOR_WIN
        if opponents_figure == 'Rock' and players_figure == 'Scissors':
            return POINTS_FOR_LOSE

        if opponents_figure == 'Paper' and players_figure == 'Rock':
            return POINTS_FOR_LOSE
        if opponents_figure == 'Paper' and players_figure == 'Paper':
            return POINTS_FOR_DEUCE
        if opponents_figure == 'Paper' and players_figure == 'Scissors':
            return POINTS_FOR_WIN

        if opponents_figure == 'Scissors' and players_figure == 'Rock':
            return POINTS_FOR_WIN
        if opponents_figure == 'Scissors' and players_figure == 'Paper':
            return POINTS_FOR_LOSE
        if opponents_figure == 'Scissors' and players_figure == 'Scissors':
            return POINTS_FOR_DEUCE

    def calculate_players_total_points_in_this_game_accordings_strategies(self) -> int:
        points = 0
        points += self.calculate_players_points_for_chosen_figure()
        points += self.set_correct_figure_according_to_players_strategy()
        return points

    def set_correct_figure_according_to_players_strategy(self) -> None:
        opponents_figure = self.opponents_figure
        players_figure = self.players_figure

        if players_figure == 'Deuce':
            self.players_figure = opponents_figure

        if players_figure == 'Win' and opponents_figure == 'Rock':
            self.players_figure = 'Paper'
        if players_figure == 'Win' and opponents_figure == 'Paper':
            self.players_figure = 'Scissors'
        if players_figure == 'Win' and opponents_figure == 'Scissors':
            self.players_figure = 'Rock'

        if players_figure == 'Lose' and opponents_figure == 'Rock':
            self.players_figure = 'Scissors'
        if players_figure == 'Lose' and opponents_figure == 'Paper':
            self.players_figure = 'Rock'
        if players_figure == 'Lose' and opponents_figure == 'Scissors':
            self.players_figure = 'Paper'


def convert_input_data_to_games_according_figures(filename: str) -> list[RockPaperScissor]:
    games = []
    input_strings = ip.read_input_list(filename)
    input_strings = ip.trim_newlines(input_strings)
    for string in input_strings:
        string = string.split(' ')
        game = RockPaperScissor(string[0], string[1])
        game.convert_figures_in_readable_strings_according_decrypting_player_to_figures()
        games.append(game)
    return games


def convert_input_data_to_games_according_strategies(filename: str) -> list[RockPaperScissor]:
    games = []
    input_strings = ip.read_input_list(filename)
    input_strings = ip.trim_newlines(input_strings)
    for string in input_strings:
        string = string.split(' ')
        game = RockPaperScissor(string[0], string[1])
        game.convert_figures_in_readable_strings_according_decrypting_player_to_game_output()
        games.append(game)
    return games


def calculate_points_for_all_games(list_of_games: list[RockPaperScissor]) -> int:
    points = 0
    for game in list_of_games:
        points += game.calculate_players_total_points_in_this_game()
    return points


def calculate_points_for_given_input_data(filename: str) -> int:
    games = convert_input_data_to_games_according_figures(filename)
    return calculate_points_for_all_games(games)


def calculate_points_for_given_input_data_according_strategy(filename: str) -> int:
    games = convert_input_data_to_games_according_strategies(filename)
    for game in games:
        game.set_correct_figure_according_to_players_strategy()
    return calculate_points_for_all_games(games)


def main():
    print("Solutions to problem 2: [https://adventofcode.com/2022/day/2]")

    total_points = calculate_points_for_given_input_data('../input_data/02_12_problem_data.txt')
    print(f'If we follow the given strategy guide we will score {total_points} points.')

    total_points_strategy = calculate_points_for_given_input_data_according_strategy(
        '../input_data/02_12_problem_data.txt')
    print(f'If we follow the top secret strategy guide we will score {total_points_strategy} points.')

    print("")


if __name__ == '__main__':
    main()
