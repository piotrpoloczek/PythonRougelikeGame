from level.level_const import BOARD, OPPONENTS, ITEMS, CHARACTERS


def set_board(level, board):
    level[BOARD] = board

def set_opponents(level, opponents):
    level[OPPONENTS] = opponents

def set_items(level, items):
    level[ITEMS] = items

def set_characters(level, characters):
    level[CHARACTERS] = characters

def set_board_opponents_items_characters(level, board, opponents, items, characters):
    set_board(level, board)
    set_opponents(level, opponents)
    set_items(level, items)
    set_characters(level, characters)