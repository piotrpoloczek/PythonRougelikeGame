from main import DIRECTIONS, BOARD_HEIGHT, BOARD_WIDTH
from board import get_board_height, get_board_width

PLAYER_ICON = "@"
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    """
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["symbol"] = PLAYER_ICON

    return player

def move(key, player, board):
    dx, dy = DIRECTIONS[key]
    if 0 <= (player["x"] + dx ) < get_board_width(board) and 0 <= (player["y"] + dy) < get_board_height(board):
        player["x"] += dx
        player["y"] += dy
        board[player["y"]-dy][player["x"]-dx] = ' '
    else:
        pass