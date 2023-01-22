from main import DIRECTIONS, BOARD_HEIGHT, BOARD_WIDTH

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
    if 0 <= (player["x"] + dx ) < BOARD_WIDTH and 0 <= (player["y"] + dy) < BOARD_HEIGHT:
        player["x"] += dx
        player["y"] += dy
        board[player["y"]-dy][player["x"]-dx] = ' '
    else:
        pass