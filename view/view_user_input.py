from view.view_key_input import key_pressed
from exception.exception_custom import ExitException


QUIT = 'q'


def get_user_input(label):
    return input(label)

def get_user_key():
    return key_pressed().lower()
    
def exit_game(user_input):
    if user_input == QUIT:
        raise ExitException

def get_user_key():
    user_input = get_user_input()
    try:
        exit_game(user_input)

    except ExitException:
        print('you exited the game!')
