def display_board(board):
    """
    Displays complete game board on the screen

    Returns:
    Nothing
    """
    print("# " * (len(board[0]) + 2))
    for row in board:
        line = "#"
        for column in row:
            line += f" {column}"
        line += " #"
        print(line)
    print("# " * (len(board[0]) + 2))