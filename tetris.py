"""Tetris game for AI testing.

Tetris game built in python with internal hooks for AI development.
"""


import numpy as np
import math
import random


class TetrisGame:

    BOARD_SIZE = (40, 10)   # internal game board size, only bottom 20 rows are visable

    def __init__(self):
        # initialize game board
        self.board = np.zeros(self.BOARD_SIZE, dtype=int)

        self.print_board()

    def spawn_piece(self):
        # create new Tetrimino
        piece = Tetrimino()


class Tetrimino:

    # 7 types of Tetrimino pieces
    TETRIMINO_TYPES = [
        {                   # I
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [0,0,0,0],
                [1,1,1,1],
                [0,0,0,0],
            ]
        },
        {                   # O
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,0],
            ]
        },
        {                   # T
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [0,1,0,0],
                [1,1,1,0],
                [0,0,0,0],
            ]
        },
        {                   # S
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [0,1,1,0],
                [1,1,0,0],
                [0,0,0,0],
            ]
        },
        {                   # Z
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [1,1,0,0],
                [0,1,1,0],
                [0,0,0,0],
            ]
        },
        {                   # J
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [1,0,0,0],
                [1,1,1,0],
                [0,0,0,0],
            ]
        },
        {                   # L
            'color': (49, 199, 239),
            'shape': [    
                [0,0,0,0],
                [0,0,1,0],
                [1,1,1,0],
                [0,0,0,0],
            ]
        }
    ]

    def __init__(self):
        # generate a new random Tetrimino
        type_index = math.floor(random.random() * 7.0)

        # set attributes
        self.color = self.TETRIMINO_TYPES[type_index]['color']
        self.shape = self.TETRIMINO_TYPES[type_index]['shape']




if __name__ == "__main__":
    #pass

    tetris = TetrisGame()
    