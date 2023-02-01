from entities.items.items_create import create_food, create_weapon


FOODS = [
    create_food('sugar', 12, 'F'),
    create_food('honey', 14,'H'),
    create_food('health potion', 60, 'P'),
]
WEAPONS = [
    create_weapon('dagger', 5, 'D'),
    create_weapon('axe', 15, 'A'),
    create_weapon('sword', 25, 'S')
]
ITEMS = FOODS + WEAPONS