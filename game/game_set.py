from game.game_const import PLAYER, LEVEL


def set_player(game, player):
    game[PLAYER] = player

def set_level(game, level):
    game[LEVEL] = level

def set_game(game, player, level):
    set_player(game, player)
    set_level(game, level)