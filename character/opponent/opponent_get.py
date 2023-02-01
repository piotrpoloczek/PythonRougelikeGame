from copy import deepcopy
from character.character_const import SYMBOL
from character.opponent.opponent_list import OPPONENTS
from character.character_get import get_icon, get_coordinates
from character.character_set import set_coordinates_list
from board.board_get import get_board_coordiante, get_board_coordiantes_symbol
from coordinates.coordinates_get import get_x_y_coordinates
from coordinates.coordinates_create import create_coordinates


def get_all_symbols():
    symbols = []
    for opponent in OPPONENTS:
        symbols.append(get_icon(opponent))
    return symbols

def get_coordiantes_with_opponents(board):
    opponents_coordinates = []
    coordinates = get_board_coordiantes_symbol(board)
    symbols = get_all_symbols()
    for coordinate in coordinates:
        if get_icon(coordinate) in symbols:
            opponents_coordinates.append(coordinate)
    return opponents_coordinates

def remove_symbol(opponents_coordiantes_symbol):
    for opponent in opponents_coordiantes_symbol[:]:
        del opponent[SYMBOL]
    return opponents_coordiantes_symbol

def get_opponents_from_board(board):
    opponents = []
    opponents_coordinates = get_coordiantes_with_opponents(board)
    for opponent_coordinates in opponents_coordinates:
        opponent = deepcopy(get_opponent_by_symbol(get_icon(opponent_coordinates)))
        x_coordinate, y_coordinate = get_x_y_coordinates(opponent_coordinates)
        coordinates_list = [create_coordinates(x_coordinate, y_coordinate)]
        set_coordinates_list(opponent, coordinates_list)
        opponents.append(opponent)
    return opponents

    
def add_near_coordinates(coordinates):
    coordinates_list = []
    near_coordinates = get_near_coordiantes(coordinates)
    if len(near_coordinates) != 0:
        for near_coordiante in near_coordinates:
            coordinates_list.append(near_coordiante)
    return coordinates_list

def get_near_coordiantes(coordinates):
    near_coordinates = []
    x_coordinate, y_coordinate = get_x_y_coordinates(coordinates)
    for x in range(x_coordinate - 1, x_coordinate + 1):
        for y in range(y_coordinate -1, y_coordinate + 1):
            near_coordinates.append(create_coordinates(x, y))
    return near_coordinates

def get_opponent_by_symbol(symbol):
    for opponent in OPPONENTS:
        if get_icon(opponent) == symbol:
            return opponent

def get_opponent_by_coordiantes(items, coordinates):
    pass