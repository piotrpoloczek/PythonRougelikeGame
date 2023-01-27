from game.game_set import set_player, set_board, set_opponents
# Dominik proszę o implementację z twoich funkcji ;)
from board.board_create import create_board
from board.board_model import put_player_on_board
from character.opponent.opponent_create import create_opponents
from game.game_set import set_level, set_player


"""
starting board is read from file and then string in variable board
starting popsitions of opponents are taken from the board
everything is wrapped in variable called level, and is returned for running
particular level.
"""
def prepare_level(player, file):
    level = {}
    board = create_board(file)
    opponents = create_opponents(file)
    set_board(level, board)
    set_opponents(level, opponents)
    put_player_on_board(board, player)
    game = {}
    set_player(game, player)
    set_level(game, level)
    return game

"""
files as input to this function list of files ['board_1.csv', 'board_2.csv', 'board_3.csv']
Thanks to it we change the list of files to the list of prepared levels, with opponents and board.
"""
def prepare_levels(files):
    return [prepare_level(file) for file in files]

def levels_files():
    return [i for i in range(0, 3)]