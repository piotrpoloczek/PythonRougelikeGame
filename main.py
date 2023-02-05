from exception.exception_custom import GameOver
from entities.character.player.player_create import create_player
from entities.entities_set import set_coordinates
from entities.coordinates.coordinates_create import create_coordinates
from level.level_run import run_level
from level.level_prepare import prepare_level, levels_files
from game.game_set import set_game
from maps.maps_const import MAPS



def main():
    player = create_player()
    levels = MAPS
    game = {}

    try:    
        for level in levels:
            level = prepare_level(level)
            player_coordinate_list = [create_coordinates(3, 3)]
            set_coordinates(player, player_coordinate_list)
            set_game(game, player, level)
            run_level(game)
        else:
            print("player won")
    except GameOver:
        print('Player died!')

if __name__ == "__main__":
    main()