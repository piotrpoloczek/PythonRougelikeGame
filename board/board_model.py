BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_board(width, height):
    """
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game boardyy
    """
    board = [[" " for _ in range(width)] for _ in range(height)]

    return board

def put_player_on_board(board, player):
    """
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    """
    board[player["y"]][player["x"]] = player["symbol"]

def get_board_height(board):
    return len(board)

def get_board_width(board):
    return len(board[0])

def check_possible_move(board, position_x, position_y):
    pass