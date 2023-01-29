from coordinates.coordinates_get import get_x_coordinate, get_y_coordinate
from character.character_get import get_coordinates
from character.character_set import set_coordinates_list
from coordinates.coordinates_create import create_coordinates_list_one_coordinate
from exception.exception_custom import (
    MoreCoordinatesInListException, FightException, ItemFoundException
)
from character.character_coordinates import coordinate_list_append
from board.board_check import check_new_coordinates
from board.board_set import set_character_on_board, set_empty_coordinates_on_board


def move(character, direction, board):
    old_coordinates_list = get_coordinates(character)
    new_coordinates_list = coordinate_list_append(old_coordinates_list, direction)

    check_new_coordinates(new_coordinates_list, board, character)
    set_empty_coordinates_on_board(board, old_coordinates_list)
    set_coordinates_list(character, new_coordinates_list)
    set_character_on_board(board, character)

def try_move(character, direction, board):
    try:
        move(character, direction, board)
    except MoreCoordinatesInListException:
        print('There is more coordinates to unpack, please implement the functions for bigger objects!!!')
    except FightException:
        print("There is opponent in front of you please implement the functions for fighting")
    except ItemFoundException:
        print("Implement the function for grabing the item!!!")
        move(character, direction, board)

