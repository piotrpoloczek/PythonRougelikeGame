def display_board(board):
    """
    Displays complete game board on the screen

    Returns:
    Nothing
    """
    for row in board:
        line = ""
        for column in row:
            if column == '-' or column == '_':
                line += "  "
            else:
                line += f" {column}"
        print(line)
