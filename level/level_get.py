from level.level_const import BOARD, OPPONENTS, ITEMS, CHARACTERS


def get_board(level):
    return level[BOARD]

def get_opponents(level):
    return level[OPPONENTS]

def get_items(level):
    return level[ITEMS]

def get_characters(level):
    return level[CHARACTERS]

def get_board_opponents_items_characters(level):
    return get_board(level), get_opponents(level), get_items(level), get_characters(level)