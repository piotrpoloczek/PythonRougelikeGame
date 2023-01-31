from items.items_const import TYPE_ARMOR, TYPE_FOOD, TYPE_SKIL, TYPE_WEAPON
from items.items_set import set_power, set_name, set_symbol, set_type


"""
structure of the item object
{'type': 'food', 'name': 'sugar', 'power': 12, 'symbol': 'F', 'coordinates': {'x': 9, 'y': 6}}
initialize without the coordinates, add coordiantes from the board
"""

def create_item():
    return {}

def set_attributes(item, name, power, symbol):
    set_name(item, name)
    set_power(item, power)
    set_symbol(item, symbol)

def create_food(name, power, symbol):
    food = create_item()
    set_type(food, TYPE_FOOD)
    set_attributes(food, name, power, symbol)
    return food

def create_weapon(name, power, symbol):
    weapon = create_item()
    set_type(weapon, TYPE_WEAPON)
    set_attributes(weapon, name, power, symbol)
    return weapon

def create_armor(name, power, symbol):
    armor = create_item()
    set_type(armor, TYPE_ARMOR)
    set_attributes(armor, name, power, symbol)
    return armor

def create_skil(name, power, symbol):
    skil = create_item()
    set_type(skil, TYPE_SKIL)
    set_attributes(skil, name, power, symbol)
    return skil