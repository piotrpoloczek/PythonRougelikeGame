from movement.movement_const import DIRECTIONS
from character.character_get import get


def move(character, direction, board):
    x, y = get

def input_to_directions(input):
    if input in DIRECTIONS.keys():
        dx, dy = DIRECTIONS[input]
        return (dx, dy)