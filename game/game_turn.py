from game.game_get_set import unpack_game


def turn(game):
    player, board, opponents = unpack_game(game)
    player_turn(game)
    for opponent in opponents:
        opponent_turn(opponent, board)


def player_turn(player, board):
    pass

def opponent_turn(opponent, board):
    pass