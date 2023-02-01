from exception.exception_custom import DefenderDie
from entities.character.character_get import get_attack, get_hp
from entities.character.character_set import set_hp


def fight(attacker, defender):
    attack(attacker, defender)
    attack(defender, attacker)


def attack(attacker, defender):
    attacker_attack = get_attack(attacker)
    defender_hp = get_hp(defender)
    defender_hp -= attacker_attack
    print('++++++++++++++++++++++++++++++++++++++++')
    print('defender: ', defender, 'defender hp: ', defender_hp)
    print('++++++++++++++++++++++++++++++++++++++++')
    set_hp(defender, defender_hp)
    if defender_hp <= 0:
        raise DefenderDie(defender)