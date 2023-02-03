import random
from entities.coordinates.coordinates_const import KEYS
from entities.coordinates.coordinates_function import input_to_directions
from exception.exception_custom import CoordinateException
from entities.character.character_movement import try_move


def opponent_turn(opponent, player, level):
    random_key = random.choice(KEYS)
    try:
        direction = input_to_directions(random_key)
        try_move(opponent, direction, level, player)
    except CoordinateException:
        opponent_turn(opponent, player, level)