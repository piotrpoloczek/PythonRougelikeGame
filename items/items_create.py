from items.items_const import TYPE_ARMOR, TYPE_FOOD, TYPE_SKIL, TYPE_WEAPON
from items.items_set import set_power, set_name, set_quantity, set_symbol, set_type


def create_item():
    return {}

def set_attributes(item, name, quantity, power, symbol):
    set_name(item, name)
    set_quantity(item, quantity)
    set_power(item, power)
    set_symbol(item, symbol)

def create_food(name, quantity, power, symbol):
    food = create_item()
    set_type(food, TYPE_FOOD)
    set_attributes(food, name, quantity, power, symbol)
    return food

def create_weapon(name, quantity, power, symbol):
    weapon = create_item()
    set_type(weapon, TYPE_WEAPON)
    set_attributes(weapon, name, quantity, power, symbol)
    return weapon

def create_armor(name, quantity, power, symbol):
    armor = create_item()
    set_type(armor, TYPE_FOOD)
    set_attributes(armor, name, quantity, power, symbol)
    return armor

def create_skil(name, quantity, power, symbol):
    skil = create_item()
    set_type(skil, TYPE_SKIL)
    set_attributes(skil, name, quantity, power, symbol)
    return skil