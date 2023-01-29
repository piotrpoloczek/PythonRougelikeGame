from character.character_create import create_character
from view.view_user_input import get_user_input
from character.player.player_const import (
    PLAYER_ICON, PLAYER_POSITION, PLAYER_START_X, 
    PLAYER_START_Y, HP, ATTACK
)
from coordinates.coordinates_create import create_coordinates_list_one_coordinate


def get_starting_inventory():
    return []

def create_player():
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!
    Returns:
    dictionary
    """
    name = get_user_input("Please choose the name for your hero: ")
    player_coordinate_list = create_coordinates_list_one_coordinate(PLAYER_START_X, PLAYER_START_Y)
    player = create_character(name, player_coordinate_list, PLAYER_ICON, ATTACK, HP)
    player['inventory'] = get_starting_inventory()

    return player