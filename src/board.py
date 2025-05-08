class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def drop_piece(self, col, player_num):
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player_num
                return True
        return False

    def check_winner(self):
        for row in range(self.rows):
            for col in range(self.cols):
                player = self.grid[row][col]
                if player == 0:
                    continue
                if col <= self.cols - 4 and all(self.grid[row][col + i] == player for i in range(4)):
                    return player
                if row <= self.rows - 4 and all(self.grid[row + i][col] == player for i in range(4)):
                    return player
                if row <= self.rows - 4 and col <= self.cols - 4 and all(self.grid[row + i][col + i] == player for i in range(4)):
                    return player
                if row >= 3 and col <= self.cols - 4 and all(self.grid[row - i][col + i] == player for i in range(4)):
                    return player
        return 0