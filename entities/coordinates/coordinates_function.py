from entities.coordinates.coordinates_const import DIRECTIONS
from exception.exception_custom import CoordinateException
from entities.coordinates.coordinates_create import create_coordinates


def key_in_directions(key):
    if key in DIRECTIONS.keys():
        return True

def input_to_directions(input):
    if key_in_directions(input):
        return get_coordinates(input)
    else:
        raise CoordinateException

def get_coordinates(key):
    dx, dy = DIRECTIONS[key]
    return create_coordinates(dx, dy)