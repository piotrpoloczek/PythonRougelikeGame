from game.game_const import BOARD, OPPONENTS, PLAYER


def set_board(game, board):
    game[BOARD] = board

def set_player(game, player):
    game[PLAYER] = player

def set_opponents(game, opponents):
    game[OPPONENTS] = opponents

def pack_game(game, player, board, opponents):
    set_board(game, board)
    set_player(game, player)
    set_opponents(game, opponents)