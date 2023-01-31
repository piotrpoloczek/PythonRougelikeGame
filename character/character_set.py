from character.character_const import (
    NAME, POSITION_X, POSITION_Y, 
    ICON, ATTACK, HP, INVENTORY, COORDINATES
)


def set_name(character, name):
    character[NAME] = name

def set_x_position(character, x_position):
    character[POSITION_X] = x_position

def set_y_position(character, y_position):
    character[POSITION_Y] = y_position

def set_icon(character, icon):
    character[ICON] = icon

def set_attack(character, attack):
    character[ATTACK] = attack

def set_hp(character, hp):
    character[HP] = hp

def set_inventory(character, inventory):
    character[INVENTORY] = inventory

def set_coordinates_list(character, coordinates_list):
    character[COORDINATES] = coordinates_list

