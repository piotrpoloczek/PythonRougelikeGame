def create_character(name, position, symbol, attack, hp):
    character = {
        'name': name,
        'x': position[0],
        'y': position[1],
        'symbol': symbol,
        'attack': attack,
        'hp': hp,
    }
    return character