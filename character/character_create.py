from character.character_set import (
    set_position, set_name, set_hp,
    set_attack, set_icon,
)


def create_character(name, position, icon, attack, hp):
    character = {}
    set_name(character, name)
    set_icon(character, icon)
    set_position(character, position)
    set_attack(character, attack)
    set_hp(character, hp)

    return character