import util
from exception.exception_custom import ExitException


QUIT = 'q'


def get_user_input():
    return util.key_pressed().lower()
    
def exit_game(user_input):
    if user_input == "q":
        raise ExitException

def get_user_key():
    user_input = get_user_input()
    try:
        exit_game(user_input)
        return user_input
    except ExitException:
        print('you exited the game!')
