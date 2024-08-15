def print_board(board):
    """Function to print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Function to check if the current player has won."""
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [player, player, player] in win_conditions:
        return True
    return False


def is_board_full(board):
    """Function to check if the board is full (i.e., no more moves left)."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Get the player's move
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
            if board[row][col] != " ":
                print("This cell is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two numbers between 0 and 2.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


# Start the game
tic_tac_toe()
