from character.character_player import create_player
from board.board_create import create_board
from game.game_set import set_game


def prepare_game():
    board = create_board()
    player = create_player()
    opponents = []
    return set_game(player, board, opponents)