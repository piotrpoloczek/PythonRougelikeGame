from entities.coordinates.coordinates_get import get_x_coordinate, get_y_coordinate
from entities.coordinates.coordinates_create import create_coordinates


def coordinate_list_append(coordinate_list, direction):
    x_direction = get_x_coordinate(direction)
    y_direction = get_y_coordinate(direction)

    new_coordinates_list = []

    for coordinate in coordinate_list:
        x_coordinate = get_x_coordinate(coordinate)
        y_coordinate = get_y_coordinate(coordinate)

        new_x_coordinate = x_coordinate + x_direction
        new_y_coordinate = y_coordinate + y_direction
        new_coordinates = create_coordinates(new_x_coordinate, new_y_coordinate)
        new_coordinates_list.append(new_coordinates)

    return new_coordinates_list

