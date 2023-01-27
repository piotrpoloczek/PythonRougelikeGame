from coordinates.coordinates_get import get_x_coordinate, get_y_coordinate
from character.character_get import get_x_y_coordinate, get_coordinates
from character.character_set import set_coordinates_list
from coordinates.coordinates_create import create_coordinates_list_one_coordinate
from board.board_model import put_player_on_board, clear_place_on_board
from exception.exception_custom import (
    MoreCoordinatesInListException, FightException, 
    ItemFoundException, CoordinatesOutsideBoardException
)


def move(character, direction, board):
    print(direction)
    x_coordinate = get_x_coordinate(direction)
    y_coordinate = get_y_coordinate(direction)
    print(x_coordinate, y_coordinate)

    character_old_coordinates = get_coordinates(character)
    clear_place_on_board(board, character)

    old_x, old_y = get_x_y_coordinate(character)

    new_x = old_x + x_coordinate
    new_y = old_y + y_coordinate

    new_coordinates_list = create_coordinates_list_one_coordinate(new_x, new_y)
    set_coordinates_list(character, new_coordinates_list)

    put_player_on_board(board, character)

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

