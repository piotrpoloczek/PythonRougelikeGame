from board.board_get import get_board_coordiantes_symbols
from entities.entities_get import get_symbol, get_coordinates
from board.board_set import set_empty_coordinates_on_board
from entities.coordinates.coordinates_create import create_coordinates, create_coordinates_list_one_coordinate
from entities.coordinates.coordinates_get import get_x_y_coordinates


def get_boss(board):
    board_symbols = get_board_coordiantes_symbols(board)
    
    for board_symbol in board_symbols:
        if 'B' == get_symbol(board_symbol):
            x, y = get_x_y_coordinates(board_symbol)
            new_coordiantes = create_coordinates_list_one_coordinate(x, y)
            set_empty_coordinates_on_board(board, new_coordiantes)
            return True
    return False
    