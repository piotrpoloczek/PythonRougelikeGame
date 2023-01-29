from view.view_user_input import get_user_key
from game.game_get import get_game, get_board_and_opponents
from board.board_view import display_board
from coordinates.coordinates_function import input_to_directions
from exception.exception_custom import CoordinateException
from character.character_movement import try_move
from view.view_functions import clear_screen


def turn_run(game):
    player, level = get_game(game)
    board, opponents = get_board_and_opponents(level)

    clear_screen()
    display_board(board)

    player_turn(player, board)
    for opponent in opponents:
        opponent_turn(opponent, board)

def player_turn(player, board):
    user_input = get_user_key()
    try:
        direction = input_to_directions(user_input)
        #print(player, direction, user_input)
        try_move(player, direction, board)
    except CoordinateException:
        player_turn(player, board)

def opponent_turn(opponent, board):
    pass