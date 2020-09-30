"""Tetris game for AI testing.

Tetris game built in python with internal hooks for AI development.

Author: Jigar Hira
Version: 1.0
"""


import numpy as np
import math
import random
import pygame


class TetrisGame:
    """Tetris game built with pygame for AI testing.
    """
    # pygame parameters
    FRAMERATE = 1
    WINDOW_SIZE = (400, 100)
    WINDOW_TITLE = 'Tetris'

    # tetris parameters
    BOARD_SIZE = (44, 10)       # internal game board size, 20 rows are visable
    BOARD_BOTTOM_FILL_ROWS = 4  # hidden filled rows at the bottom of the board

    def __init__(self):
        """Initialization method.
        """
        # initialize pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.WINDOW_TITLE)
        pygame.display.flip()

        # initialize game board
        self.board = np.zeros(self.BOARD_SIZE, dtype=int)
        self.board[0:self.BOARD_BOTTOM_FILL_ROWS] = np.full((self.BOARD_BOTTOM_FILL_ROWS, self.BOARD_SIZE[1]), 7)   # fill hidden portion at the bottom of the board

        # initialize score
        self.score = 0


    def play(self):
        """Tetris game. Main game loop and event handling
        """
        # spawn the first piece
        self.spawn_piece()

        # game loop
        while True:

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:    # keypress
                    if event.key == pygame.K_w:
                        # rotate piece
                        self.piece_rotate()
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

            # move the piece down at one second intervals
                # check if piece should be placed

            # check board for completed row
            

            # render and print board
            self.print_board(self.render_board())

            # timing
            self.clock.tick(self.FRAMERATE)

    
    def print_board(self, board:np.ndarray):
        """Print board to console.

        Args:
            board (np.ndarray): Game board array.
        """
        print('\n\n------~ TETRIS ~------')
        print(np.flipud(board[0:26, :]))


    def coord_to_index(self, coord: (int, int)) -> (int, int):
        """Converts tetris coordinates to board indicies.

        Args:
            coord ((int, int)): Tetris coordinates with origin at bottom left.

        Returns:
            (int, int): Board indicies.
        """
        return (coord[0] + self.BOARD_BOTTOM_FILL_ROWS, coord[1])


    def spawn_piece(self):
        """Generate new piece.
        """
        self.piece = Tetrimino()


    def piece_down(self):
        """Move piece down one block if valid.
        """
        self.piece_move((-1, 0))


    def piece_left(self):
        """Move piece left one block if valid.
        """
        self.piece_move((0, -1))


    def piece_right(self):
        """Move piece right once block if valid.
        """
        self.piece_move((0, 1))


    def piece_move(self, offset: (int, int)):
        """Move piece by x and y offset if valid.

        Args:
            offset (int, int): x and y offset for new piece location.
        """
        # current and new piece locations
        location = self.piece.location
        new_location = (location[0] + offset[0], location[1] + offset[1])

        # check new piece position
        if self.check_piece_position(location=new_location):
            # update piece location
            self.piece.location = new_location


    def piece_rotate(self):
        """Rotate piece 90 degrees clockwise if valid.
        """
        # current and new piece rotation
        rotation = self.piece.shape
        new_rotation = np.rot90(rotation)

        # check new piece position
        if self.check_piece_position(shape=new_rotation):
            # update piece rotation
            self.piece.shape = new_rotation


    def check_piece_position(self, location=None, shape=None) -> bool:
        """Check if piece position and rotation is valid.

        Args:
            location ((int, int), optional): New piece location. Defaults to current piece location.
            shape (np.ndarray, optional): New piece shape or rotation. Defaults to current piece shape.

        Returns:
            bool: If piece position is valid on the current board.
        """
        # default parameters
        if location is None:
            location = self.piece.location
        if shape is None:
            shape = self.piece.shape

        # piece location and size
        (i, j) = self.coord_to_index(location)
        (piece_h, piece_w) = self.piece.size

        # board location
        sub_board = self.board[i:i + piece_h, j:j + piece_w]

        # TODO
        # THERE IS AN ERROR HERE. BOUNDARY BOX WILL RESTRICT MOVEMENT.

        # check left and right bounds
        if (j < 0) or (j + piece_w > self.BOARD_SIZE[1]):
            return False

        # check for overlap
        if np.sum(sub_board * shape) == 0:
            # valid position
            return True
        else:
            # overlap found
            return False

    
    def render_board(self) -> np.ndarray:
        """Render all game elements onto the board. Adds the current piece
        to the board. Returns fully rendered board.

        Returns:
            np.ndarray: Fully rendered board array.
        """
        # rendered board
        rendered_board = np.copy(self.board)

        # add piece to rendered board
        self.render_piece(rendered_board)

        return rendered_board
    
    
    def render_piece(self, board:np.ndarray):
        """Render the current piece onto the board.

        Args:
            board (np.ndarray): Board matrix to add the current piece to.
        """
        # piece size and location
        (i, j) = self.coord_to_index(self.piece.location)
        (piece_h, piece_w) = self.piece.size

        # add piece to board
        for k, row in enumerate(self.piece.shape):
            for l, block in enumerate(row):
                if block != 0:
                    board[i + k, j + l] = block
        



class Tetrimino:
    """Tetrimino (tetris piece) class.
    """
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
    