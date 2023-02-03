from view.menu_const import *
from entities.character.character_get import get_attack, get_hp, get_inventory, get_name, get_lvl, get_experience
from entities.entities_const import NAME
from entities.character.player.player_const import HP

def print_board(board,player):
    board_m = create_menu(player,board)
    for idx,i in enumerate(board):
        line = ''
        for j in i + board_m[idx]:
            if j == '-' or j == '_':
                line += "  "
            else:
                line += f" {j}"
        print(line)

def create_menu(player,board):
    menu_board = create_menu_board()
    menu_board[MENU_FRAME_POSOTION] = menu_frame()
    menu_board[MENU_HEADER_POSITION] = player_header_menu()
    menu_board[MENU_PLAYER_NAME_POSITION] = player_name_menu(player)
    menu_board[MENU_LVL_POSITION] = player_lvl_menu(player)
    menu_board[MENU_EXPERIENCE_POSITION] = player_experience_menu(player)
    menu_board[MENU_HP_POSITION] = player_hp_menu(player)
    menu_board[MENU_ATTACK_POSITION] = player_attack_menu(player)
    menu_board[MENU_EQUIPED_HEADER_POSITION] = player_equiped_header()
    menu_board[MENU_EQUIPED_POSITION] = player_equiped(player)
    menu_board[MENU_INVENTORY_POSITION-1] = player_inventory_menu()
    menu_board = display_inventory(player,menu_board,board)
    return menu_board

def create_menu_board():
    board = [[MENU_SPACER for j in range(MENU_WIDTH)] for i in range(MENU_HEIGHT)]
    return board

def player_header_menu():
    return fill_line(data=[MENU_PLAYER_HEADER])

def player_name_menu(player):
    return fill_line(data=[get_name(player)])

def player_lvl_menu(player):
    return fill_line(data=[MENU_LVL_HEADER,str(get_lvl(player))])

def player_experience_menu(player):
    return fill_line(data=[MENU_EXPERIENCE_HEADER,str(get_experience(player))])

def player_hp_menu(player):
    return fill_line(data=[MENU_HP_HEADER,str(get_hp(player)),'/',str(HP)])

def player_attack_menu(player):
    return fill_line(data=[MENU_ATTACK_HEADER,str(get_attack(player))])

def player_equiped_header():
    return fill_line(data=[MENU_EQUIPED_HEADER])

def player_equiped(player):
    equiped = player['equiped']
    return fill_line(data=[])

def player_inventory_menu():
    return fill_line(data=[MENU_INVENTORY_HEADER])

def display_inventory(player,menu_board,board):
    inventory = get_inventory(player)
    items = {}
    for i in inventory:
        if i[NAME] in items.keys():
            items[i[NAME]] = items[i[NAME]] + 1
        else:
            items[i[NAME]] = 1
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    sorted_items_copy = sorted_items
    sorted_items = dict(items)
    keysList = [key for key in sorted_items]
    a = 0
    for idx in range(len(items)):
        a = idx
        line = fill_line(data=[keysList[idx], ':', str(sorted_items_copy[idx][1])])
        menu_board[MENU_INVENTORY_POSITION + idx] = line
        if MENU_INVENTORY_POSITION + idx == len(board) - 2:
            return menu_board
    if items == {}:
        menu_board[MENU_INVENTORY_POSITION + a] = menu_frame()
    else:
        menu_board[MENU_INVENTORY_POSITION + a + 1] = menu_frame()
    return menu_board

def fill_end_of_line(line):
    return line + [ MENU_SPACER for i in range(MENU_WIDTH - (len(line)) - 1)] + [MENU_FRAME]

def input_data_to_line(line,data):
    return line + [i for i in data]

def fill_line(data):
    line = [MENU_FRAME]
    for i in data:
        line = input_data_to_line(line,i)
    line = fill_end_of_line(line)
    return line

def menu_frame():
    return [MENU_FRAME for i in range(MENU_WIDTH)]