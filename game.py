# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                        (0, 4, 8), (2, 4, 6)]             # diagonals
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    return all(space != " " for space in board)

# Main function to play the game
def play_game():
    board = [" " for _ in range(9)]  # Create an empty board
    current_player = "X"  # X always starts
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get valid input from the player
        while True:
            try:
                move = int(input("Choose a position (1-9): ")) - 1
                if board[move] == " ":
                    break
                else:
                    print("That position is already taken.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")
        
        # Place the player's move on the board
        board[move] = current_player
        
        # Check if the current player won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
