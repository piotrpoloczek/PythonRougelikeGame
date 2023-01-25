from view.view_user_input import get_user_key
from game.game_get import get_game, get_board_and_opponents
from movement.movement_function import move, input_to_directions


def turn_run(game):
    player, level = get_game(game)
    board, opponents = get_board_and_opponents(level)
    player_turn(game)
    for opponent in opponents:
        opponent_turn(opponent, board)

def player_turn(player, board):
    user_input = get_user_key()
    direction = input_to_directions(user_input)
    move(player, direction, board)

def opponent_turn(opponent, board):
    pass