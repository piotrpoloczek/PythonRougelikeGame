from character.character_set import (
    set_name, set_hp, set_attack, set_icon, set_coordinates_list,
)


def create_character(name, coordinates_list, icon, attack, hp):
    character = {}
    set_name(character, name)
    set_icon(character, icon)

    set_coordinates_list(character, coordinates_list)

    set_attack(character, attack)
    set_hp(character, hp)

    return character