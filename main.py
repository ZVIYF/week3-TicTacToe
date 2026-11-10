from get_func.inputs import get_location
from prints.prints import print_board, print_winner, print_draw
from logic.logics import update_board, is_winner, is_game_over, switch_players
from DATA.board import board
from DATA.lines import WINNING_LINES
from DATA.players import players_dict


def main_menu():
    while True:
        player = players_dict["current"]
        print_board(board)
        choice = get_location(player)
        update_board(board, choice, player)
        if is_winner(board, WINNING_LINES):
            print_board(board)            
            print_winner(player)
            break
        if is_game_over(board):
            print_board(board)
            print_draw()
            break
        switch_players(players_dict)

if __name__ == "__main__":
    main_menu()