from entities.entities_get import get_coordinates, get_type
from entities.character.character_set import set_coordinates_list, set_experience
from entities.character.character_get import get_experience
from exception.exception_custom import FightException, ItemFoundException, DefenderDie, GameOver
from entities.character.character_coordinates import coordinate_list_append
from board.board_check import check_new_coordinates
from board.board_set import set_character_on_board, set_empty_coordinates_on_board
from entities.character.player.player_inventory import take_item
from level.level_get import get_board_opponents_items_characters
from entities.character.character_fight import fight


def move(character, direction, level):
    board, opponents, items, characters  = get_board_opponents_items_characters(level)
    old_coordinates_list = get_coordinates(character)
    new_coordinates_list = coordinate_list_append(old_coordinates_list, direction)

    check_new_coordinates(new_coordinates_list, character, level)
    set_empty_coordinates_on_board(board, old_coordinates_list)
    set_coordinates_list(character, new_coordinates_list)
    set_character_on_board(board, character)

def try_move(character, direction, level, player):
    board, opponents, items, characters  = get_board_opponents_items_characters(level)
    try:
        move(character, direction, level)
    except FightException as fight_exception:
        opponent = fight_exception.opponent
        print(opponent)
        try:
            fight(character, opponent)
        except DefenderDie as defender_die:
            defender = defender_die.defender
            if get_type(defender) == 'opponent':
                opponents.remove(opponent)
                experience = get_experience(defender)
                player_experience = get_experience(player) + experience
                set_experience(player, player_experience)
            else:
                """
                Raised game over when player die
                """
                raise GameOver
            set_empty_coordinates_on_board(board, get_coordinates(opponent))
            print('defendef died')
    except ItemFoundException as exception:
        item = exception.item
        take_item(character, item, level)
        try_move(character, direction, level, player)

