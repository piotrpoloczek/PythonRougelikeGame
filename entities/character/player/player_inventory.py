from entities.character.character_set import set_inventory
from entities.character.character_get import get_inventory
from level.level_get import get_board_opponents_items_characters
from entities.entities_get import get_coordinates
from board.board_set import set_empty_coordinates_on_board
from entities.items.items_function import remove_item_from_items


def add_item_to_inventory(character, item):
    inventory = get_inventory(character)
    inventory.append(item)
    set_inventory(character, inventory)    

def take_item(character, item, level):
    board, opponents, items, characters = get_board_opponents_items_characters(level)
    item_coordiantes_list = get_coordinates(item)
    set_empty_coordinates_on_board(board, item_coordiantes_list)
    add_item_to_inventory(character, item)
    remove_item_from_items(items, item)