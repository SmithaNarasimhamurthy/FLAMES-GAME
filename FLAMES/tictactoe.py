import random

# Function to print the Tic Tac Toe board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# Function to check if there's a winner
def check_winner(board, marker):
    win_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6],  # Reverse diagonal
    ]
    return any(all(board[i] == marker for i in combo) for combo in win_combinations)


# Function to check if the game is a draw
def is_draw(board):
    return all(cell in ["X", "O"] for cell in board)


# Function for the computer to make a move
def computer_move(board):
    available_positions = [i for i in range(9) if board[i] not in ["X", "O"]]
    return random.choice(available_positions)


# Main Tic Tac Toe function
def tic_tac_toe():
    print("Welcome to Tic Tac Toe! 🎮")
    print("You (Player) are 'X', and the Computer is 'O'.")
    print("Enter a number (1-9) to place your marker on the board.\n")

    board = [str(i + 1) for i in range(9)]  # Initial board
    human_marker = "X"
    computer_marker = "O"

    while True:
        # Player's turn
        print_board(board)
        try:
            choice = int(input("Your turn! Choose your position (1-9): ")) - 1
            if board[choice] not in ["X", "O"]:
                board[choice] = human_marker

                # Check for a winner
                if check_winner(board, human_marker):
                    print_board(board)
                    print("🎉 Congratulations! You win! 🎉")
                    break

                # Check for a draw
                if is_draw(board):
                    print_board(board)
                    print("It's a draw! 🤝")
                    break

                # Computer's turn
                print("Computer's turn...")
                comp_choice = computer_move(board)
                board[comp_choice] = computer_marker

                # Check if the computer wins
                if check_winner(board, computer_marker):
                    print_board(board)
                    print("😞 The computer wins! Better luck next time!")
                    break

                # Check for a draw again after computer's turn
                if is_draw(board):
                    print_board(board)
                    print("It's a draw! 🤝")
                    break
            else:
                print("Position already taken. Choose another position.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

    print("Thanks for playing Tic Tac Toe! 😊")


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
