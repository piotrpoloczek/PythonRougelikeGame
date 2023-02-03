from view.view_user_input import get_user_key
from entities.coordinates.coordinates_function import input_to_directions
from exception.exception_custom import CoordinateException
from entities.character.character_movement import try_move


def player_turn(player, level):
    user_input = get_user_key()
    try:
        direction = input_to_directions(user_input)
        try_move(player, direction, level, player)
    except CoordinateException:
        player_turn(player, level)