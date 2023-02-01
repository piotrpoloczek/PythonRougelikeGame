from game.game_get import get_game
from level.level_get import get_board_opponents_items_characters
from board.board_view import display_board
from view.view_functions import clear_screen
from level.turn.turn_player import player_turn
from level.turn.turn_opponent import opponent_turn



def turn_run(game):
    player, level = get_game(game)
    board, opponents, items, characters = get_board_opponents_items_characters(level)

    clear_screen()
    display_board(board)

    player_turn(player, level)
    for opponent in opponents:
        opponent_turn(opponent, player, level)



