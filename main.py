import util
import engine
import ui

from pprint import pprint as pp

PLAYER_ICON = "@"
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


DIRECTIONS = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0),
}


def create_player():
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    """
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["symbol"] = PLAYER_ICON

    return player


def main():
    player = create_player()
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
            dx, dy = DIRECTIONS[key]
            if 0 <= (player["x"] + dx ) < BOARD_WIDTH and 0 <= (player["y"] + dy) < BOARD_HEIGHT:
                player["x"] += dx
                player["y"] += dy
                board[player["y"]-dy][player["x"]-dx] = ' '
        else:
            pass
        util.clear_screen()


if __name__ == "__main__":
    main()