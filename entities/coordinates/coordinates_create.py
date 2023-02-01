from entities.coordinates.coordinates_set import set_x_coordinate, set_y_coordinate


def create_coordinates(x_coordinate, y_coordinate):
    coordinates = {}
    set_x_coordinate(coordinates, x_coordinate)
    set_y_coordinate(coordinates, y_coordinate)
    return coordinates

def create_coordinates_list_one_coordinate(x_coordinate, y_cooridinate):
    coordinates_list = []
    coordinates_list.append(create_coordinates(x_coordinate, y_cooridinate))
    return coordinates_list

def append_coordinate(coordinates, x_coordinate, y_coordiante):
    coordinates.append(create_coordinates(x_coordinate, y_coordiante))
