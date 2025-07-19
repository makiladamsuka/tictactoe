# Simple Two-Player Tic-Tac-Toe Game
This is a basic command-line Tic-Tac-Toe game written in Python, allowing two players to compete against each other.

## Features
* Two-Player Mode: Play locally with a friend.

* 3x3 Grid: Standard Tic-Tac-Toe board.

* Input Validation: Handles incorrect input formats.

* Win/Draw Detection: Automatically identifies when a player wins or if the game ends in a draw.

## How to Play
* Save the code: Save the provided Python code as a .py file (e.g., tic_tac_toe.py).

* Run from terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using Python:

* ` python tic_tac_toe.py `


* Follow the prompts:

* Players will take turns entering their moves.

* Enter your move as row,column (e.g., 1,1 for the top-left corner, 2,3 for the middle-right).

* Player 1 uses 'X' and Player 2 uses 'O'.

## Game Rules
The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.

If all nine squares are filled and neither player has three marks in a row, the game is a draw.

## Code Structure
* main(): The main game loop, handling player turns, input, and game state.

* display_grid(grid): Prints the current state of the Tic-Tac-Toe board.

* get_inputs(): Prompts the user for their move and handles basic input parsing and validation.

* valid_move(grid, row, col): Checks if a chosen cell is empty and available.

* draw_grid(row, col, mark, grid): Updates the grid with the player's mark.

* check_winner(grid): Determines if there is a winner.

* draw_game(grid): Checks if the game has ended in a draw.

## Future Improvements (Ideas)
* AI Opponent: Add a single-player mode against a computer AI.

* Graphical User Interface (GUI): Implement a visual interface using libraries like Tkinter, Pygame, or PyQt.

* Score Tracking: Keep track of wins, losses, and draws over multiple games.

