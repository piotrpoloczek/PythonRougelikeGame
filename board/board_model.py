from character.character_get import get_x_y_coordinate
from exception.exception_custom import (
    MoreCoordinatesInListException, CoordinatesOutsideBoardException,
    CoordinateException,
)
import coordinates.coordinates_get as coordinates_module
from coordinates.coordinates_set import set_x_coordinate, set_y_coordinate
from coordinates.coordinates_create import create_coordinates
from board.board_const import EMPTY_COORDINATES, EMPTY_SPACE


BOARD_WIDTH = 30
BOARD_HEIGHT = 20



def create_board(width, height):
    """
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
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
    try:
        x, y = get_x_y_coordinate(player)
        board[y][x] = player["icon"]
    except IndexError:
        raise CoordinateException

def clear_place_on_board(board, coordinates_list):
    for coordinates in coordinates_list:
        x, y = coordinates_module.get_x_y_coordinates(coordinates)
        board[y][x] = '-'

def check_new_coordinates(coordiantes_list, board):
    available_coordiantes = get_board_available_coordiantes(board)
    #print('checking: ', coordiantes_list, available_coordiantes)
    for coordinates in coordiantes_list:
        if coordinates not in available_coordiantes:
            raise CoordinateException
    return True


def get_board_available_coordiantes(board):
    available_coordiantes = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if board[row_index][item_index] == EMPTY_COORDINATES:
                coordinate = create_coordinates(item_index, row_index)
                available_coordiantes.append(coordinate)
    return available_coordiantes
    
def get_board_height(board):
    return len(board)

def get_board_width(board):
    return len(board[0])

def check_possible_move(board, position_x, position_y):
    pass

def check_position(board, x, y):
    """
    check position
    """
    pass