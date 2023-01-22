from board.board_functions import can_move, clean_coordinates

DIRECTIONS = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0),
}

def get_user_coordinates():
    pass

def get_coordinates(key):
    dx, dy = DIRECTIONS[key]
    return {'x': dx, 'y': dy}

def move(character, coordinates, board):
    if can_move(character, coordinates, board):
        character["x"] += coordinates['x']
        character["y"] += coordinates['y']
        clean_coordinates()
    else:
        get_user_coordinates()
        