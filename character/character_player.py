from character.character_create import create_character
from view.view_user_input import get_user_input


PLAYER_ICON = "@"
PLAYER_POSITION = (3, 3)
PLAYER_START_X = 3
PLAYER_START_Y = 3
HP = 100
ATTACK = 50


def get_starting_inventory():
    return []

def create_player():
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!
    Returns:
    dictionary
    """
    name = get_user_input("Please choose the name for your hero")
    player = create_character(name, PLAYER_POSITION, PLAYER_ICON, ATTACK, HP)
    player['inventory'] = get_starting_inventory()

    return player