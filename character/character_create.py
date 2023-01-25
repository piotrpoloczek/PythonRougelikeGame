from character.character_set import (
    set_name, set_hp,
    set_attack, set_icon,
    set_x_position, set_y_position,
)


def create_character(name, x_position, y_position, icon, attack, hp):
    character = {}
    set_name(character, name)
    set_icon(character, icon)
    set_x_position(character, x_position)
    set_y_position(character, y_position)
    set_attack(character, attack)
    set_hp(character, hp)

    return character