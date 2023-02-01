from entities.character.character_const import POSITION_X, POSITION_Y, ATTACK, HP, INVENTORY
from exception.exception_custom import MoreCoordinatesInListException


FIRST_INDEX_COORDINATES = 0

def get_x_position(character):
    return character[POSITION_X]

def get_y_position(character):
    return character[POSITION_Y]

def get_attack(character):
    return character[ATTACK]

def get_hp(character):
    return character[HP]

def get_inventory(character):
    return character[INVENTORY]
