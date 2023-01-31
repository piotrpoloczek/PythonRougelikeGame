from const import BOARD, OPPONENTS, PLAYER, LEVEL, ITEMS_LIST


def set_board(game, board):
    game[BOARD] = board

def set_player(game, player):
    game[PLAYER] = player

def set_opponents(game, opponents):
    game[OPPONENTS] = opponents

def set_items(level, items):
    level[ITEMS_LIST] = items

def set_level(game, level):
    game[LEVEL] = level

def set_game(game, player, level):
    set_player(game, player)
    set_level(game, level)