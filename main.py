import util
import board

from pprint import pprint as pp




def main():
    player = player_module.create_player()
    board_present = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        .put_player_on_board(board, player)
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