from entities.character.character_create import create_character
from view.view_user_input import get_user_input
from entities.character.player.player_const import PLAYER_ICON, HP, ATTACK, LEVEL, EXPERIENCE
from entities.entities_const import TYPE_PLAYER
from entities.coordinates.coordinates_create import create_coordinates_list_one_coordinate, create_coordinates


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
    #player_coordinate_list = create_coordinates_list_one_coordinate(PLAYER_START_X, PLAYER_START_Y)
    # for debuging purpouses
    player_coordinate_list = [
        create_coordinates(3, 3),
        create_coordinates(3, 4),
        create_coordinates(4, 3),
        create_coordinates(4, 4),
    ]
    player = create_character(TYPE_PLAYER, name, player_coordinate_list, PLAYER_ICON, ATTACK, HP, LEVEL, EXPERIENCE)
    player['inventory'] = get_starting_inventory()
    player['equiped'] = []

    return player