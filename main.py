# Simple two-player tic-tac-toe game

def main():
    player = 1
    print("Welcome to the Two-Player Tic-Tac-Toe Game!")
    grid = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 grid
    display_grid(grid)

    while True:
        if player == 1:
            print("Player 1's turn")
            # Logic for Player 1's turn
            row, col  = get_inputs()
            if valid_move(grid, row, col):
                display_grid(draw_grid(row, col, "X", grid))
                player = 2

            else:
                print("Invalid move, try again.")
                continue
            
        else:
            print("Player 2's turn")
            # Logic for Player 2's turn
            row, col = get_inputs()

            if valid_move(grid, row, col):
                display_grid(draw_grid(row, col, "O", grid))
                player = 1

            else:
                print("Invalid move, try again.")
                continue

        # Check if there is a winner

        if check_winner(grid):
            if player == 1:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
            break

        # Check if the game is a draw
        if draw_game(grid):
            print("It's a draw!")
            break



def draw_grid(row, col, mark, grid):
    grid[row][col] = mark  # Mark the cell as occupied
    return grid

def display_grid(grid):
    for row in grid:
        # Print each row of the grid
        print(' | '.join(row))
        print('-' * 10)

def get_inputs():
    input_value = input("Enter your move (row , column): ")
    # Split the input by comma and convert to integers
    try:
        row, col = map(int, input_value.split(','))
        return row - 1, col - 1  # Adjusting for 0-based index
    except ValueError:
        print("Invalid input. Please enter row and column as integers separated by a comma.")
        return get_inputs()  # Retry input

def valid_move(grid,row, col):
    # Logic to check if the move is valid
    if grid[row][col] == ' ':
        return True
    else:
        return False
    

def draw_game(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                return False
    return True

def check_winner(grid):
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] != ' ':
            return True
        
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != ' ':
            return True
        
    if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
        return True
    
    if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
        return True
    
    return False


if __name__ == "__main__":
    main()