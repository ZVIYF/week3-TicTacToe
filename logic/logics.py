from DATA.lines import WINNING_LINES
from validation.validation import is_available


def update_board(board:list, choice:int, player):
    board[choice] = player


def is_game_over(board: list)-> bool:
    for i in range(len(board)):
        if is_available(board, i):
            return False
    return True


def is_winner(board:list, winning_lines:list[tuple]):
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] != None:
            return True
    return False



def switch_players(players:dict):
    players["current"], players["next"] = players["next"], players["current"]


