from character.character_const import (
    NAME, POSITION_X, POSITION_Y, 
    ICON, ATTACK, HP, INVENTORY
)


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