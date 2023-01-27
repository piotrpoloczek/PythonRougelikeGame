from game.game_set import set_player, set_board, set_opponents
# Dominik proszę o implementację z twoich funkcji ;)
from board.board_create import create_board
from character.opponent.opponent_create import create_opponents


def prepare_level(file):
    level = {}
    board = create_board(file)
    opponents = create_opponents(file)
    set_board(level, board)
    set_opponents(level, opponents)
    return level

def prepare_levels(files):
    levels = [prepare_level(file) for file in files]