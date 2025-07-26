class TicTacToe:
    def __init__(self):
        self.player = 1
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display_grid(self):
        for row in self.grid:
            # Print each row of the grid
            print(' | '.join(row))
            print('-' * 10)

    def get_inputs(self):
        input_value = input("Enter your move (row , column): ")
    
        try:
            row, col = map(int, input_value.split(','))
            return row - 1, col - 1  # Adjusting for 0-based index
        except ValueError:
            print("Invalid input. Please enter row and column as integers separated by a comma.")
            return self.get_inputs()  # Retry input
        
    
    def valid_move(self, row, col):
        # Logic to check if the move is valid
        if self.grid[row][col] == ' ':
            return True
        else:
            return False
        
    def check_winner(self):
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != ' ':
                return True

        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != ' ':
                return True

            if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
                return True

            if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
                return True
    
        return False

    def display_grid(self):
        for row in self.grid:
            # Print each row of the grid
            print(' | '.join(row))
            print('-' * 10)


    def draw_grid(self, row, col, mark):
        self.grid[row][col] = mark  # Mark the cell as occupied
        return self.grid
    
    
    def draw_game(self):
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == ' ':
                    return False
        return True



    def play(self):
        while True:
            if self.player == 1:
                print("Player 1's turn")
                # Logic for Player 1's turn
                row, col  = self.get_inputs()

                if self.valid_move(row, col):
                    self.draw_grid(row, col, 'X')
                    self.display_grid()
                    self.player = 2

                else:
                    print("Invalid move, try again.")
                    continue

            else:
                print("Player 2's turn")
                row, col = self.get_inputs()

                if self.valid_move(row, col):
                    self.draw_grid(row, col, 'O')
                    self.display_grid()
                    self.player = 1

                else:
                    print("Invalid move, try again.")
                    continue

            if self.check_winner():
                if self.player == 1:
                    print("Player 2 wins!")
                else:
                    print("Player 1 wins!")
                break

            if self.draw_game():
                print("It's a draw!")
                break


def main():
    game = TicTacToe()
    game.play()



if __name__ == "__main__":
    main()