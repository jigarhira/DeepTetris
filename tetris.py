"""Tetris game for AI testing.

Tetris game built in python with internal hooks for AI development.
"""


import numpy as np
import math
import random
import pygame


class TetrisGame:

    FRAMERATE = 1
    WINDOW_SIZE = (400, 400)
    WINDOW_TITLE = 'Tetris'

    BOARD_SIZE = (40, 10)   # internal game board size, only bottom 20 rows are visable

    def __init__(self):
        # initialize pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.WINDOW_TITLE)
        pygame.display.flip()

        # initialize game board
        self.board = np.zeros(self.BOARD_SIZE, dtype=int)


    def play(self):
        self.spawn_piece()

        while True:
            # move piece down
            self.piece_down()

            # render and print board
            self.print_board(self.render_board())

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # close window
                    pygame.quit()
                    break

            # timing
            self.clock.tick(self.FRAMERATE)

    
    def print_board(self, board:np.ndarray):
        print('\n\n------~ TETRIS ~------')
        print(np.flipud(board[:22][:]))


    def spawn_piece(self):
        # create new Tetrimino
        self.piece = Tetrimino()


    def piece_down(self):
        # piece location
        (x, y) = self.piece.location

        # check new piece position
        if self.check_piece_position((x - 1, y)):
            # update piece location
            self.piece.location = (x - 1, y)        


    def check_piece_position(self, location=None) -> bool:
        # piece location and size
        if location is None:
            location = self.piece.location
        (x, y) = location
        (piece_h, piece_w) = self.piece.size

        # board location
        sub_board = self.board[x:x + piece_h, y:y + piece_w]

        # check for overlap
        if np.sum(sub_board * self.piece.shape) == 0:
            # valid position
            return True
        else:
            # overlap found
            return False

    
    def render_board(self) -> np.ndarray:
        # rendered board
        rendered_board = np.copy(self.board)

        # add piece to rendered board
        self.render_piece(rendered_board)

        return rendered_board
    
    
    def render_piece(self, board:np.ndarray):
        # piece size and location
        (x, y) = self.piece.location
        (piece_h, piece_w) = self.piece.size

        # add piece to board
        for i, row in enumerate(self.piece.shape):
            for j, block in enumerate(row):
                if block != 0:
                    board[x + i, y + j] = block
        



class Tetrimino:

    # 7 types of Tetrimino pieces
    TETRIMINO_TYPES = [
        {                   # I
            'spawn': (19, 3),
            'color': (0, 255, 255),
            'shape': [    
                [0,0,0,0],
                [1,1,1,1],
                [0,0,0,0],
                [0,0,0,0],
            ]
        },
        {                   # O
            'spawn': (19, 3),
            'color': (255, 255, 0),
            'shape': [    
                [0,0,0,0],
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,0],
            ]
        },
        {                   # T
            'spawn': (19, 3),
            'color': (153, 0, 255),
            'shape': [    
                [0,0,0],
                [1,1,1],
                [0,1,0],
            ]
        },
        {                   # S
            'spawn': (19, 3),
            'color': (0, 255, 0),
            'shape': [
                [0,0,0],
                [1,1,0],
                [0,1,1],
            ]
        },
        {                   # Z
            'spawn': (19, 3),
            'color': (255, 0, 0),
            'shape': [
                [0,0,0],
                [0,1,1],
                [1,1,0],
            ]
        },
        {                   # J
            'spawn': (19, 3),
            'color': (0, 0, 255),
            'shape': [
                [0,0,0],
                [1,1,1],
                [1,0,0],
            ]
        },
        {                   # L
            'spawn': (19, 3),
            'color': (255, 170, 0),
            'shape': [
                [0,0,0],
                [1,1,1],
                [0,0,1],
            ]
        }
    ]

    def __init__(self):
        # generate a new random Tetrimino
        type_index = math.floor(random.random() * 7.0)

        # set attributes
        self.color = self.TETRIMINO_TYPES[type_index]['color']
        self.shape = self.TETRIMINO_TYPES[type_index]['shape']
        self.size = np.array(self.shape).shape
        self.location = self.TETRIMINO_TYPES[type_index]['spawn']




if __name__ == "__main__":
    #pass

    tetris = TetrisGame()
    tetris.play()
    