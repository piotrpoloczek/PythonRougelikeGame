from board.board_create import create_board_from_file
from entities.character.opponent.opponent_get import get_opponents_from_board
from entities.items.items_get import get_items_from_board
from level.level_set import set_board_opponents_items_characters
from entities.character.boss.boss_get import get_boss
from entities.character.boss.boss_create import create_boss


"""
starting board is read from file and then string in variable board
starting popsitions of opponents are taken from the board
everything is wrapped in variable called level, and is returned for running
particular level.
"""
def prepare_level(file):
    level = {}
    board = create_board_from_file(file)
    opponents = get_opponents_from_board(board)
    if get_boss(board):
        boss = create_boss()
        opponents.append(boss)
    items = get_items_from_board(board)
    characters = []
    set_board_opponents_items_characters(level, board, opponents, items, characters)
    return level


def levels_files():
    return [i for i in range(0, 3)]