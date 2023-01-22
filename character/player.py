from main import DIRECTIONS, BOARD_HEIGHT, BOARD_WIDTH
from board import get_board_height, get_board_width, check_possible_move

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

