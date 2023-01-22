import util
import engine
import ui
import player as player_module

from pprint import pprint as pp


BOARD_WIDTH = 30
BOARD_HEIGHT = 20


DIRECTIONS = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0),
}


def main():
    player = player_module.create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        pp(player)
        key = util.key_pressed().lower()
        if key == "q":
            is_running = False
        elif key in DIRECTIONS.keys():
            player_module.move(key, player, board)
        util.clear_screen()


if __name__ == "__main__":
    main()