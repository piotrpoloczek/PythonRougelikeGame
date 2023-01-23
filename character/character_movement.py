from board.board_functions import can_move, clean_coordinates


DIRECTIONS = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0),
}

def key_not_in_directions(key):
    if key not in DIRECTIONS:
        return True

def get_coordinates(key):
    dx, dy = DIRECTIONS[key]
    return {'x': dx, 'y': dy}

def move(character, key, board):
    if key_not_in_directions(key):
        return False
    coordinates = get_coordinates(key)
    if can_move(character, coordinates, board):
        character["x"] += coordinates['x']
        character["y"] += coordinates['y']
        clean_coordinates()
        return True
        

