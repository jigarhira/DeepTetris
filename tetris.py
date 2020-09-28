"""Tetris game for AI testing.

Tetris game built in python with internal hooks for AI development.
"""


import numpy as np
import math
import random
import pygame


class TetrisGame:

    # pygame parameters
    FRAMERATE = 1
    WINDOW_SIZE = (400, 400)
    WINDOW_TITLE = 'Tetris'

    # tetris parameters
    BOARD_SIZE = (44, 10)       # internal game board size, 20 rows are visable
    BOARD_BOTTOM_FILL_ROWS = 4  # hidden filled rows at the bottom of the board

    def __init__(self):
        # initialize pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.WINDOW_TITLE)
        pygame.display.flip()

        # initialize game board
        self.board = np.zeros(self.BOARD_SIZE, dtype=int)
        self.board[0:self.BOARD_BOTTOM_FILL_ROWS] = np.full((self.BOARD_BOTTOM_FILL_ROWS, self.BOARD_SIZE[1]), 7)   # fill hidden portion at the bottom of the board


    def play(self):
        # spawn a new piece
        self.spawn_piece()

        while True:
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:    # keypress
                    if event.key == pygame.K_w:
                        # rotate piece
                        pass
                    elif event.key == pygame.K_a:
                        # move piece left
                        self.piece_left()
                    elif event.key == pygame.K_s:
                        # move piece down
                        self.piece_down()
                    elif event.key == pygame.K_d:
                        # move piece right
                        self.piece_right()        
                    elif event.key == pygame.K_SPACE:
                        # drop piece to bottom
                        pass
                elif event.type == pygame.QUIT:     # close window
                    pygame.quit()
                    break

            # render and print board
            self.print_board(self.render_board())

            # timing
            self.clock.tick(self.FRAMERATE)

    
    def print_board(self, board:np.ndarray):
        print('\n\n------~ TETRIS ~------')
        print(np.flipud(board[0:26, :]))


    def coord_to_index(self, coord: (int, int)) -> (int, int):
        return (coord[0] + self.BOARD_BOTTOM_FILL_ROWS, coord[1])


    def spawn_piece(self):
        # create new Tetrimino
        self.piece = Tetrimino()


    def piece_down(self):
        self.piece_move((-1, 0))


    def piece_left(self):
        self.piece_move((0, -1))


    def piece_right(self):
        self.piece_move((0, 1))


    def piece_move(self, offset: (int, int)):
        # current and new piece locations
        location = self.piece.location
        new_location = (location[0] + offset[0], location[1] + offset[1])

        # check new piece position
        if self.check_piece_position(new_location):
            # update piece location
            self.piece.location = new_location


    def check_piece_position(self, location=None) -> bool:
        # piece location and size
        if location is None:
            location = self.piece.location
        (i, j) = self.coord_to_index(location)
        (piece_h, piece_w) = self.piece.size

        # board location
        sub_board = self.board[i:i + piece_h, j:j + piece_w]

        # check left and right bounds
        if (j < 0) or (j + piece_w > self.BOARD_SIZE[1]):
            return False

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
        (i, j) = self.coord_to_index(self.piece.location)
        (piece_h, piece_w) = self.piece.size

        # add piece to board
        for k, row in enumerate(self.piece.shape):
            for l, block in enumerate(row):
                if block != 0:
                    board[i + k, j + l] = block
        



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
    