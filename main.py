from exception.exception_custom import GameOver
from entities.character.player.player_create import create_player
from level.level_run import run_level
from level.level_prepare import prepare_level, levels_files
from game.game_set import set_game


def main():
    player = create_player()
    levels = levels_files()
    game = {}

    try:    
        for level in levels:
            level = prepare_level(level)
            set_game(game, player, level)
            run_level(game)
    except GameOver:
        print('Player died!')

if __name__ == "__main__":
    main()