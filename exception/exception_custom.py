class ExitException(Exception):
    pass


class CoordinateException(Exception):
    pass


class EndLevelException(Exception):
    pass


class MoreCoordinatesInListException(Exception):
    pass


class FightException(Exception):
    def __init__(self, opponent):
        self.opponent = opponent


class ItemFoundException(Exception):
    def __init__(self, item):
        self.item = item


class CoordinatesOutsideBoardException(Exception):
    pass


class ItemNotFoundException(Exception):
    pass


class DefenderDie(Exception):
    def __init__(self, defender):
        self.defender = defender


class GameOver(Exception):
    pass