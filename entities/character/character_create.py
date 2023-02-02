from entities.entities_set import set_coordinates, set_name, set_symbol, set_type
from entities.character.character_set import set_hp, set_attack, set_lvl, set_experience


def create_character(type, name, coordinates_list, icon, attack, hp, lvl, experience):
    character = {}
    set_type(character, type)
    set_name(character, name)
    set_symbol(character, icon)

    set_coordinates(character, coordinates_list)

    set_attack(character, attack)
    set_hp(character, hp)
    set_lvl(character, lvl)
    set_experience(character, experience)


    return character