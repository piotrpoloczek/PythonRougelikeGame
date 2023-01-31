from coordinates.coordinates_create import create_coordinates
from board.board_const import EMPTY_COORDINATES
from character.character_get import get_icon
from character.character_set import set_icon


def get_board_available_coordiantes(board):
    return get_board_coordiantes(board, EMPTY_COORDINATES)

def get_board_character_coordinates(board, character):
    character_icon = get_icon(character)
    return get_board_coordiantes(board, character_icon)

def get_board_coordiantes(board, checking_cell):
    available_coordiantes = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if board[row_index][item_index] == checking_cell:
                coordinate = create_coordinates(item_index, row_index)
                available_coordiantes.append(coordinate)
    return available_coordiantes

def get_board_coordiante(board, checking_cell):
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if board[row_index][item_index] == checking_cell:
                return create_coordinates(item_index, row_index)

def get_board_height(board):
    return len(board)

def get_board_width(board):
    return len(board[0])

def get_board_coordiantes_symbol(board):
    coordiantes = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            coordinate = create_coordinates(item_index, row_index)
            set_icon(coordinate, item)
            coordiantes.append(coordinate)
    return coordiantes