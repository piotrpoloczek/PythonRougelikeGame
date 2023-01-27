from character.character_const import (
    NAME, POSITION_X, POSITION_Y, 
    ICON, ATTACK, HP, INVENTORY, COORDINATES
)
from coordinates.coordinates_get import get_x_coordinate, get_y_coordinate
from exception.exception_custom import MoreCoordinatesInListException


FIRST_INDEX_COORDINATES = 0


def get_name(character):
    return character[NAME]

def get_x_position(character):
    return character[POSITION_X]

def get_y_position(character):
    return character[POSITION_Y]

def get_icon(character):
    return character[ICON]

def get_attack(character):
    return character[ATTACK]

def get_hp(character):
    return character[HP]

def get_inventory(character):
    return character[INVENTORY]

def get_coordinates(character):
    return character[COORDINATES]

def get_x_y_coordinate(character):
    coordinates = get_coordinates(character)
    if len(coordinates) == 1:
        x = get_x_coordinate(coordinates[FIRST_INDEX_COORDINATES])
        y = get_y_coordinate(coordinates[FIRST_INDEX_COORDINATES])
        return x, y
    raise MoreCoordinatesInListException