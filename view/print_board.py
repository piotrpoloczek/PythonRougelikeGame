from view.menu_const import *

def print_board(board,player):
    board_m = create_menu(player)
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
    menu_board[MENU_HEADER_POSITION] = player_header_menu()
    menu_board[MENU_PLAYER_NAME_POSITION] = player_name_menu(player)
    menu_board[MENU_LVL_POSITION] = player_lvl_menu(player)
    menu_board[MENU_EXPERIENCE_POSITION] = player_experience_menu(player)
    menu_board[MENU_HP_POSITION] = player_hp_menu(player)
    menu_board[MENU_ATTACK_POSITION] = player_attack_menu(player)
    menu_board[MENU_INVENTORY_POSITION-1] = player_inventory_menu()
    menu_board = display_inventory(player,menu_board)
    return menu_board

def create_menu_board():
    board = [[MENU_SPACER for j in range(MENU_WIDTH)] for i in range(MENU_HEIGHT)]
    return board

def player_header_menu():
    return fill_line(data=[MENU_PLAYER_HEADER])

def player_name_menu(player):
    return fill_line(data=[player['name']])

def player_lvl_menu(player):
    return fill_line(data=[MENU_LVL_HEADER])

def player_experience_menu(player):
    return fill_line(data=[MENU_EXPERIENCE_HEADER])

def player_hp_menu(player):
    return fill_line(data=[MENU_HP_HEADER,str(player['hp'])])

def player_attack_menu(player):
    return fill_line(data=[MENU_ATTACK_HEADER,str(player['attack'])])

def player_inventory_menu():
    return fill_line(data=[MENU_INVENTORY_HEADER])

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
        line = fill_line(data=[keysList[idx], ':', str(sorted_items_copy[idx][1])])
        menu_board[MENU_INVENTORY_POSITION+idx] = line
        if MENU_INVENTORY_POSITION + idx == MENU_HEIGHT - 1:
            return menu_board
    return menu_board

def fill_end_of_line(line):
    return line + [ MENU_SPACER for i in range(MENU_WIDTH-len(line))]

def input_data_to_line(line,data):
    return line + [i for i in data]

def fill_line(data):
    line = [MENU_SPACER]
    for i in data:
        line = input_data_to_line(line,i)
    line = fill_end_of_line(line)
    return line