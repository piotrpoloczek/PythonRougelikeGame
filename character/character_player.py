from character.character_create import create_character

PLAYER_ICON = "@"
PLAYER_POSITION = (3, 3)
PLAYER_START_X = 3
PLAYER_START_Y = 3
HP = 100
ATTACK = 50


def user_input_name():
    return input("Please choose the name for your hero: ")

def get_starting_inventory():
    return []

def use_item():
    pass

def get_item():
    pass

def create_player():
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!
    Returns:
    dictionary
    """
    name = user_input_name()
    player = create_character(name, PLAYER_POSITION, PLAYER_ICON, ATTACK, HP)
    player['inventory'] = get_starting_inventory()

    return player