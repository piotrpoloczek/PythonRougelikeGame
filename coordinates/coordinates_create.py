from coordinates.coordinates_set import set_x_coordinate, set_y_coordinate


def create_coordinates(x_coordinate, y_coordinate):
    coordinates = {}
    set_x_coordinate(coordinates, x_coordinate)
    set_y_coordinate(coordinates, y_coordinate)
    return coordinates
