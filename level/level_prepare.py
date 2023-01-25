from game.game_set import set_player, set_board, set_opponents


def prepare_level(file):
    level = {}
    board = create_board(file)
    opponents = get_opponents(file)
    set_board(level, board)
    set_opponents(level, opponents)
    return level

def prepare_levels(files):
    levels = [prepare_level(file) for file in files]