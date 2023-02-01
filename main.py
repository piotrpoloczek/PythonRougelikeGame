from entities.character.player.player_create import create_player
from level.level_run import run_level
from level.level_prepare import prepare_level, levels_files


def main():
    player = create_player()
    levels = levels_files()
    game = {}

    for level in levels:
        game = prepare_level(player, level)
        run_level(game)


if __name__ == "__main__":
    main()