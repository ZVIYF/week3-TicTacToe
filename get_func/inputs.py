from DATA.board import board
from validation.validation import validate_location, is_available

def get_location(player:str)-> int:
    while True:
        user_input = input(f"player {player}, choose a cell (1-9):").strip()
        try:
            validate_location(user_input)
            choice = int(user_input) - 1
            if not is_available(board, choice):
                raise ValueError("Cell already taken")
            return choice
        except ValueError as error:
            print(f"error: {error}")
