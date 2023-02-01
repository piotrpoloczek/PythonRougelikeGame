from entities.entities_const import NAME, SYMBOL, COORDINATES, TYPE


def get_name(entity):
    return entity[NAME]

def get_symbol(entity):
    return entity[SYMBOL]

def get_coordinates(entity):
    return entity[COORDINATES]

def get_type(entity):
    return entity[TYPE]

def get_attribute(entity, attribute):
    return entity[attribute]