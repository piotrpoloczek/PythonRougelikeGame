from items.items_const import TYPE, TYPE_WEAPON, NAME, QUANTITY, POWER, SYMBOL
from items.items_create import create_weapon


items = [
    create_weapon('venom', 1, 25, 'V'),
    {TYPE: TYPE_WEAPON, NAME: 'venom', QUANTITY: 1, POWER: 25, SYMBOL: 'C'},
    {TYPE: TYPE_WEAPON, NAME: 'honey', QUANTITY: 1, POWER: 25, SYMBOL: 'D'},
    {TYPE: TYPE_WEAPON, NAME: 'maple syrup', QUANTITY: 1, POWER: 25, SYMBOL: 'E'},    
]