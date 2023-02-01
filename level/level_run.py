from exception.exception_custom import EndLevelException
from level.turn.turn_main import turn_run


"""
Tutaj nie znalazłem lepszego sposobu żeby wyjść z pętli,
jesli player przejdzie przez drzwi to wywołamy EndLevelException i tutj to przechwycimy

jeśli zakładamy że player nie może wrócić na wcześniejszy level, w przeciwnym przypadku
trzeba będzię to zmienić 
"""
def run_level(game):
    try:
        while True:
            turn_run(game)
    except EndLevelException:
        return