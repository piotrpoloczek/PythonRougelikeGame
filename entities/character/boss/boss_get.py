from board.board_get import get_board_coordiantes_symbols
from entities.entities_get import get_symbol

def get_boss(board):
    board_symbols = get_board_coordiantes_symbols(board)
    
    for board_symbol in board_symbols:
        if 'B' == get_symbol(board_symbol):
            return True
    return False
    