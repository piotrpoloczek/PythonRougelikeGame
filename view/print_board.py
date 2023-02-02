MENU_WIDTH = 20
MENU_HEIGHT = 30
MENU_PLAYER_HEADER = 'Player:'
MENU_LVL_HEADER = 'Lvl:'
MENU_EXPERIENCE_HEADER = 'Exp:'
MENU_HP_HEADER = 'HP:' 
MENU_ATTACK_HEADER = 'Attack:'
MENU_INVENTORY_HEADER = 'Inventory:'


def print_board(board,player):
    
    board_m = create_menu(player)
    # for i in range(len(board)):
    #     board[i] = board[i] + board_m[i]
    #     print(board[i])
    
    # for row in board:
    #     line = ""
    #     for column in row:
    #         if column == '-' or column == '_':
    #             line += "  "
    #         else:
    #             line += f" {column}"
    #     print(line)
    for idx,i in enumerate(board):
        line = ''
        for j in i + board_m[idx]:
            if j == '-' or j == '_':
                line += "  "
            else:
                line += f" {j}"
        print(line)


def create_menu(player):
    menu_board = create_menu_board()
    menu_board[1] = player_header_menu()
    menu_board[2] = player_name_menu(player)
    menu_board[3] = player_lvl_menu(player)
    menu_board[4] = player_experience_menu(player)
    menu_board[5] = player_hp_menu(player)
    menu_board[6] = player_attack_menu(player)
    menu_board[7] = player_inventory_menu(player)
    menu_board = display_inventory(player,menu_board)
    return menu_board


def create_menu_board():
    a = []
    for i in range(MENU_HEIGHT):
        b = []
        for j in range(MENU_WIDTH):
            b.append('#')
        a.append(b)
    return a

def player_header_menu():
    line = ['#']
    for i in MENU_PLAYER_HEADER:
        line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def player_name_menu(player):
    line = ['#']
    name = player['name']
    for i in name:
        line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def player_lvl_menu(player):
    line = ['#']
    # name = str(player['hp'])
    for i in MENU_LVL_HEADER:
        line.append(i)
    # for i in name:
    #     line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def player_experience_menu(player):
    line = ['#']
    # name = str(player['hp'])
    for i in MENU_EXPERIENCE_HEADER:
        line.append(i)
    # for i in name:
    #     line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def player_hp_menu(player):
    line = ['#']
    name = str(player['hp'])
    for i in MENU_HP_HEADER:
        line.append(i)
    for i in name:
        line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def player_attack_menu(player):
    line = ['#']
    name = str(player['attack'])
    for i in MENU_ATTACK_HEADER:
        line.append(i)
    for i in name:
        line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def player_inventory_menu(player):
    line = ['#']
    for i in MENU_INVENTORY_HEADER:
        line.append(i)
    for i in range(MENU_WIDTH-len(line)):
        line.append('#')
    return line

def display_inventory(player,menu_board):
    inventory = player['inventory']
    items = {}
    for i in inventory:
        if i['name'] in items.keys():
            items[i['name']] = items[i['name']] + 1
        else:
            items[i['name']] = 1
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    sorted_items_copy = sorted_items
    sorted_items = dict(items)
    keysList = [key for key in sorted_items]
    for idx in range(len(items)):
        line = ['#']
        for i in keysList[idx]:
            line.append(i)
        line.append(':')
        for i in str(sorted_items_copy[idx][1]):
            line.append(i)
        for i in range(MENU_WIDTH-len(line)):
            line.append('#')
        menu_board[8+idx] = line
        if 19+idx == 20:
            return menu_board
    return menu_board