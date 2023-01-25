from game.game_const import BOARD, OPPONENTS, PLAYER



def get_board(game):
    return game[BOARD]

def get_player(game):
    return game[PLAYER]

def get_opponents(game):
    return game[OPPONENTS]

def get_game(game):
    return get_board(game), get_player(game), get_opponents(game)
