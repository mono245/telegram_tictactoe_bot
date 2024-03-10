from random import choice


def bot_choice(fields: list[str]) -> int:
    empty_fields = [i for i, field in enumerate(fields) if field == "-"]

    if not empty_fields:  # if there's no free fields
        return -1
    
    return choice(empty_fields)
        

def is_win(fields: list[str], char: str) -> bool:
    """
    checking if char param wins in tic-tac-toe
    
    :param char: character, X or O
    """
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    
    for condition in win_conditions:
        if all(fields[i] == char for i in condition):
            return True
    return False