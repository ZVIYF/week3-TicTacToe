from logic.logics import is_available


def print_board(board):
    print("\n\n\n")
    print("====================")
    print("      board")
    print("====================")
    print(f"[1]{board[0] if not is_available(board, 0) else ""} | [2]{board[1] if not is_available(board, 1) else ""} | [3]{board[2] if not is_available(board, 2) else ""}")
    print("------+-------+----")
    print(f"[4]{board[3] if not is_available(board, 3) else ""} | [5]{board[4] if not is_available(board, 4) else ""} | [6]{board[5] if not is_available(board, 5) else ""}")
    print("------+-------+----")
    print(f"[7]{board[6] if not is_available(board, 6) else ""} | [8]{board[7] if not is_available(board, 7) else ""} | [9]{board[8] if not is_available(board, 8) else ""}")
    print()
    

def print_winner(player: str):
    print(f"Winner is player {player}!")


def print_draw():
    print("Game is over. No winners.")

if __name__ == "__main__":
    print_board()