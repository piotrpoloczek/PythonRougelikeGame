from entities.character.character_create import create_character
from entities.entities_const import TYPE_OPPONENT
from entities.coordinates.coordinates_create import create_coordinates


def create_boss():
    coordinates = [
        create_coordinates(20, 20),
        create_coordinates(21, 20),
        create_coordinates(20, 21),
        create_coordinates(21, 21),
    ]
    return create_character(TYPE_OPPONENT, 'boss', coordinates, 'B', 200, 2000, 30, 3000)