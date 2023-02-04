from game.game_get import get_game
from level.level_get import get_board_opponents_items_characters
from board.board_view import display_board
from view.view_functions import clear_screen
from level.turn.turn_player import player_turn
from level.turn.turn_opponent import opponent_turn
from board.board_set import set_character_on_board
from view.print_board import print_board


def turn_run(game):
    player, level = get_game(game)
    board, opponents, items, characters = get_board_opponents_items_characters(level)

    set_character_on_board(board, player)

    ##clear_screen()
    print_board(board,player)
    print('++++++++++++++++++++++++++++++++++++++++')
    print(player)
    print('++++++++++++++++++++++++++++++++++++++++')
    print(opponents)
    print('++++++++++++++++++++++++++++++++++++++++')

    player_turn(player, level)

    for opponent in opponents:
        set_character_on_board(board, opponent)
        opponent_turn(opponent, player, level)