from entities.items.items_const import TYPE, QUANTITY, POWER


def set_quantity(item, quantity):
    item[QUANTITY] = quantity

def set_power(item, power):
    item[POWER] = power

def set_type(item, type):
    item[TYPE] = type