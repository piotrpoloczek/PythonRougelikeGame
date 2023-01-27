from coordinates.coordinates_const import COORDINATE_X, COORDINATE_Y


def get_x_coordinate(coordinates):
    return coordinates[COORDINATE_X]

def get_y_coordinate(coordinates):
    return coordinates[COORDINATE_Y]

def get_x_y_coordinates(coordinates):
    print(coordinates)
    return get_x_coordinate(coordinates), get_y_coordinate(coordinates)