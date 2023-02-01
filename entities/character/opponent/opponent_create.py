import random
from entities.character.character_const import RANDOM_MULTIPLICATOR
from entities.character.character_create import create_character


def random_attribute(attribute):
    return random.randint(int(attribute - attribute * RANDOM_MULTIPLICATOR), int(attribute + attribute * RANDOM_MULTIPLICATOR))

def create_opponent(name, icon, attack, hp):
    random_attack = random_attribute(attack)
    random_hp = random_attribute(hp)
    return create_character(name, None, icon, random_attack, random_hp)

def create_opponents(board):
    pass