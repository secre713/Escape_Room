def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        move = get_move(players[turn])
        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("Call already taken. Try again.")
            continue

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!and escapes the room")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = 1 - turn


if __name__ == "__main__":
    main()
