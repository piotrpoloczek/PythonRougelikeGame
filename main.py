from entities.character.player.player_create import create_player
from level.level_run import run_level
from level.level_prepare import prepare_level, levels_files
from game.game_set import set_game


def main():
    player = create_player()
<<<<<<< HEAD
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed().lower()
        if key == "q":
            is_running = False
        elif key in DIRECTIONS.keys():
            dx, dy = DIRECTIONS[key]
            if 0 <= (player["x"] + dx ) < BOARD_WIDTH and 0 <= (player["y"] + dy) < BOARD_HEIGHT:
                player["x"] += dx
                player["y"] += dy
                board[player["y"]-dy][player["x"]-dx] = ' '
        else:
            pass
        util.clear_screen()
=======
    levels = levels_files()
    game = {}
>>>>>>> ab9bc23943800e1e84fcf9dbb75ed24ee39577a3

    for level in levels:
        level = prepare_level(level)
        set_game(game, player, level)
        run_level(game)

if __name__ == "__main__":
    main()