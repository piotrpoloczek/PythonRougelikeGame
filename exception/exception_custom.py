class ExitException(Exception):
    pass


class CoordinateException(Exception):
    pass


class EndLevelException(Exception):
    pass


class MoreCoordinatesInListException(Exception):
    pass


class FightException(Exception):
    pass


class ItemFoundException(Exception):
    def __init__(self, coordinates):
        self.coordinates = coordinates

class CoordinatesOutsideBoardException(Exception):
    pass

class ItemNotFoundException(Exception):
    pass


class FightException(Exception):
    pass