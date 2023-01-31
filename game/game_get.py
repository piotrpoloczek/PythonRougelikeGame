from const import BOARD, OPPONENTS, PLAYER, LEVEL, ITEMS_LIST


def get_board(game):
    return game[BOARD]

def get_player(game):
    return game[PLAYER]

def get_opponents(game):
    return game[OPPONENTS]

def get_items(game):
    return game[ITEMS_LIST]

def get_level(game):
    return game[LEVEL]

def get_game(game):
    return get_player(game), get_level(game)

def get_board_opponents_items(level):
    return get_board(level), get_opponents(level), get_items(level)
