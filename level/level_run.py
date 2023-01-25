from game.game_set import set_game
from level.level_prepare import prepare_level
from game.game_turn import turn_run


def run_level(game):
    level_running = True
    while level_running:
        turn_run(game)
