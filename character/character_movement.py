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
from items.items_get import get_items_from_board, get_item_by_coordiantes, get_item_coordinates
from character.player.player_inventory import add_item_to_inventory
from game.game_get import get_board_opponents_items


def move(character, direction, level):
    board, opponents, items  = get_board_opponents_items(level)
    old_coordinates_list = get_coordinates(character)
    new_coordinates_list = coordinate_list_append(old_coordinates_list, direction)

    check_new_coordinates(new_coordinates_list, board, character)
    set_empty_coordinates_on_board(board, old_coordinates_list)
    set_coordinates_list(character, new_coordinates_list)
    set_character_on_board(board, character)

def take_item(character, item, board):
    item_coordiantes_list = [get_item_coordinates(item)]
    set_empty_coordinates_on_board(board, item_coordiantes_list)
    add_item_to_inventory(character, item)


def try_move(character, direction, level):
    board, opponents, items  = get_board_opponents_items(level)
    try:
        move(character, direction, level)
    except FightException:
        print("There is opponent in front of you please implement the functions for fighting")
    except ItemFoundException as exception:
        item_coordiantes = [exception.coordinates]
        item = get_item_by_coordiantes(items, item_coordiantes)
        take_item(character, item, board)
        move(character, direction, level)