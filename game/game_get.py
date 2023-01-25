from const import BOARD, OPPONENTS, PLAYER, LEVEL


def get_board(game):
    return game[BOARD]

def get_player(game):
    return game[PLAYER]

def get_opponents(game):
    return game[OPPONENTS]

def get_level(game):
    return game[LEVEL]

def get_game(game):
    return get_player(game), get_level(game)

def get_board_and_opponents(level):
    return get_board(level), get_opponents(level)
