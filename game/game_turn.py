import random
from coordinates.coordinates_const import KEYS
from view.view_user_input import get_user_key
from game.game_get import get_game, get_board_opponents_items, get_items
from board.board_view import display_board
from coordinates.coordinates_function import input_to_directions
from exception.exception_custom import CoordinateException
from character.character_movement import try_move
from view.view_functions import clear_screen
from items.items_list import ITEMS


def turn_run(game):
    player, level = get_game(game)
    board, opponents, items  = get_board_opponents_items(level)
    items = get_items(level)

    #clear_screen()
    display_board(board)
    print(player)
    print(opponents)

    player_turn(player, level)
    for opponent in opponents:
        opponent_turn(opponent, player, level)

def player_turn(player, level):
    user_input = get_user_key()
    try:
        direction = input_to_directions(user_input)
        #print(player, direction, user_input)
        try_move(player, direction, level)
    except CoordinateException:
        player_turn(player, level)

def opponent_turn(opponent, player, level):
    random_key = random.choice(KEYS)
    try:
        direction = input_to_directions(random_key)
        try_move(opponent, direction, level)
    except CoordinateException:
        opponent_turn(opponent, player, level)