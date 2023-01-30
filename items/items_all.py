"""
file for storing all available items

"""

from items.items_foods import foods



def get_all_items():
    items_list = []
    for food in foods:
        items_list.append(food)
    return items_list




