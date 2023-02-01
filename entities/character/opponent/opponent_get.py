from entities.coordinates.coordinates_get import get_x_y_coordinates
from entities.coordinates.coordinates_create import create_coordinates
from entities.entities_get_from_board import get_entities_from_board
from entities.character.opponent.opponent_list import OPPONENTS


    
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


def get_opponents_from_board(board):
    return get_entities_from_board(board, OPPONENTS)
