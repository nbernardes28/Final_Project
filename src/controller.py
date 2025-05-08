import pygame
from src.board import Board
from src.player import Player

ROWS = 6
COLS = 7
TILE_SIZE = 100
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
RADIUS = TILE_SIZE // 2 - 10

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Connect Four")
        self.board = Board()
        self.players = [Player(1, RED), Player(2, YELLOW)]
        self.current_player = 0
        self.running = True
        self.winner = 0

    def draw_board(self):
        self.screen.fill(BLUE)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.grid[row][col]
                color = BLACK
                if piece == 1:
                    color = RED
                elif piece == 2:
                    color = YELLOW
                pygame.draw.circle(self.screen, color, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), RADIUS)
        pygame.display.flip()

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.winner == 0:
                    x = event.pos[0]
                    col = x // TILE_SIZE
                    if self.board.drop_piece(col, self.players[self.current_player].num):
                        self.winner = self.board.check_winner()
                        if self.winner != 0:
                            print(f"Player {self.winner} wins!")
                            # Log the result to external file
                            with open("assets/wins.txt", "a") as file:
                                file.write(f"Player {self.winner} won the game.\n")
                        self.current_player = (self.current_player + 1) % 2
            self.draw_board()
        pygame.quit()