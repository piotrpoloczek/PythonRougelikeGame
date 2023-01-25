from player.player_create import create_player
from level.level_run import run_level
from level.level_prepare import prepare_levels
from game.game_set import set_game


def main():
    player = create_player()
    levels = prepare_levels()
    game = {}

    for level in levels:
        set_game(game, player, level)
        run_level(game)

if __name__ == "__main__":
    main()