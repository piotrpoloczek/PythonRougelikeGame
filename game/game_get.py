from game.game_const import PLAYER, LEVEL


def get_player(game):
    return game[PLAYER]

def get_level(game):
    return game[LEVEL]

def get_game(game):
    return get_player(game), get_level(game)