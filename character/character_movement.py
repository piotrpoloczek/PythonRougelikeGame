from board.board_functions import can_move, clean_coordinates
from coordinates.coordinates_function import input_to_directions
from coordinates.coordinates_get import get_x_coordinate, get_y_coordinate
from character.character_set import set_x_position, set_y_position


def move(character, key, board):
    try:
        coordinates = input_to_directions(key)
        if can_move(character, coordinates, board):
            set_x_position(character, get_x_coordinate(coordinates))
            set_y_position(character, get_y_coordinate(coordinates))
            clean_coordinates()
            return True
    except:
        return False


            

