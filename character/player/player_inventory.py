from character.character_set import set_inventory
from character.character_get import get_inventory


def add_item_to_inventory(character, item):
    inventory = get_inventory(character)
    inventory.append(item)
    set_inventory(character, inventory)    