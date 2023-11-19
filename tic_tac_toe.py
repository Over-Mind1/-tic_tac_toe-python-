def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ' or \
                board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ' or \
            board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)

        # Get user input with validation
        while True:
            try:
                print(f" player {player}")
                row = int(input("choose row(0, 1, 2): "))
                col = int(input("choose col (0, 1, 2): "))

                # Check if the chosen cell is empty
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    break
                else:
                    print("error choose empty cell !")
            except ValueError:
                print("invalid number")

        # Update the board
        board[row][col] = player

        # Check for a winner
        if check_winner(board):
            print(f"player {player} is win  ")
            print_board(board)
            break

        # Check for a tie
        if is_board_full(board):
            print("tie!")
            break

        # Switch players
        player = 'O' if player == 'X'else 'X'


if __name__ == "__main__":
    play()
