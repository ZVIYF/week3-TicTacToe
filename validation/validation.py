def validate_location(user_input):
    if not user_input.isdigit():
        raise ValueError("please type a number")
    choice = int(user_input)
    if not (0 < choice < 10):
        raise ValueError("choice must be between 1 - 9")


def is_available(board:list, index_num:int)-> bool:
    return board[index_num] is None

