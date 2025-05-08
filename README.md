# Final_Project
Connect 4
CS110 A0
Nico Bernardes
a simple digital version of the board game connect 4

###initial_gui
![alt text](initial_gui.png)

###final_gui
![alt text](final_gui.png)

1. turn-based gameplay
2. mouse input to drop discs
3. graphic display
4. win detection
5. game ends and prints winner

### Classes
- **Board** (`model_board.py`):
  - `__init__(self, rows, cols)`: Initializes the game board
  - `drop_piece(self, col, player_num)`: Attempts to drop a piece in the selected column
  - `check_winner(self)`: Checks and returns the winning player number if any

- **Player** (`model_player.py`):
  - `__init__(self, num, color)`: Initializes the player with a unique number and display color

- **Controller** (`controller.py`):
  - `__init__(self)`: Sets up the GUI, models, and state variables
  - `draw_board(self)`: Renders the game grid and player discs
  - `mainloop(self)`: Runs the event and game update loop

## ATP (Acceptance Test Procedure)

| Step | Procedure                        | Expected Result                       |
|------|----------------------------------|--------------------------------------|
| 1    | Run `main.py`                    | Game window appears                   |
| 2    | Click in a column                | Player 1 disc appears in column       |
| 3    | Click in another column          | Player 2 disc appears in column       |
| 4    | Fill a column completely         | No more discs accepted in that column |
| 5    | Make 4 in a row (any direction)  | Console displays "Player X wins!"     |
| 6    | Click close window               | Game exits without error              |