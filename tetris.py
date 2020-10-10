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
    GAME_SPEED = 1.0                        # speed multiplier for game
    FRAMERATE = 1                           # rendering framerate
    DROP_INTERVAL_MS = 1000.0 / GAME_SPEED  # inverval for automatic drop (miliseconds)
    WINDOW_SIZE = (200, 100)
    WINDOW_TITLE = 'Tetris'
    # pygame events
    DROP_EVENT = pygame.USEREVENT + 1

    # tetris parameters
    BOARD_SIZE = (44, 18)           # internal game board size, 20 rows and middle 10 columns are visable
    BOARD_BOTTOM_FILL_ROWS = 4      # hidden filled rows at the bottom of the board
    BOARD_SIDE_FILL_COLUMNS = 4     # hidden filled columns on the sides of the board
    BOARD_FILL_VALUE = 7            # value for hidden filled regions of the board

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

        # fill hidden portions of the board on bottom and sides
        self.board[0:self.BOARD_BOTTOM_FILL_ROWS] = np.full((self.BOARD_BOTTOM_FILL_ROWS, self.BOARD_SIZE[1]), self.BOARD_FILL_VALUE)
        self.board[:, 0:self.BOARD_SIDE_FILL_COLUMNS] = np.full((self.BOARD_SIZE[0], self.BOARD_SIDE_FILL_COLUMNS), self.BOARD_FILL_VALUE)
        self.board[:, self.BOARD_SIZE[1] - self.BOARD_SIDE_FILL_COLUMNS:self.BOARD_SIZE[1]] = np.full((self.BOARD_SIZE[0], self.BOARD_SIDE_FILL_COLUMNS), self.BOARD_FILL_VALUE)

        # initialize score
        self.score = 0


    def play(self):
        """Tetris game. Main game loop and event handling
        """
        # setup timers
        pygame.time.set_timer(self.DROP_EVENT, int(self.DROP_INTERVAL_MS))

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
                elif event.type == self.DROP_EVENT: # drop piece
                    # move piece down
                    self.piece_down()
                elif event.type == pygame.QUIT:     # close window
                    pygame.quit()
                    break

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
        return (coord[0] + self.BOARD_BOTTOM_FILL_ROWS, coord[1] + self.BOARD_SIDE_FILL_COLUMNS)


    def spawn_piece(self):
        """Generate new piece.
        """
        self.piece = Tetrimino()


    def piece_down(self):
        """Move piece down one block if valid, otherwise spawn a new piece
        """
        if not self.piece_move((-1, 0)):
            # add current piece to board
            self.render_piece(self.board)

            # clear completed rows
            self.clear_rows()

            # spawn new piece
            self.spawn_piece()



    def piece_left(self):
        """Move piece left one block if valid.
        """
        self.piece_move((0, -1))


    def piece_right(self):
        """Move piece right once block if valid.
        """
        self.piece_move((0, 1))


    def piece_move(self, offset: (int, int)) -> bool:
        """Move piece by x and y offset if valid.

        Args:
            offset (int, int): x and y offset for new piece location.

        Returns:
            bool: If piece was moved.
        """
        # current and new piece locations
        location = self.piece.location
        new_location = (location[0] + offset[0], location[1] + offset[1])

        # check new piece position
        if self.check_piece_position(location=new_location):
            # update piece location
            self.piece.location = new_location
            return True
        
        return False


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

        # check for overlap
        if np.sum(sub_board * shape) == 0:
            # valid position
            return True
        else:
            # overlap found
            return False


    def clear_rows(self):
        # piece location and size
        (i, _) = self.coord_to_index(self.piece.location)
        (piece_h, _) = self.piece.size

        # clear and move down piece rows
        cleared_lines = 0
        row_top = i
        row = i - piece_h + 1
        for piece_row in range(piece_h):
            # check bottom row of piece
            if self.check_row_complete(row):
                # shift down piece rows
                self.shift_rows_down(1, row + 1, row_top)
                cleared_lines += 1
                row_top -= 1
            else:
                row += 1

        # shift all rows above piece down by the number of cleared lines
        self.shift_rows_down(cleared_lines, row)

        # update score
        self.score += cleared_lines


    
    def check_row_complete(self, i: int) -> bool:
        """Checks if row is completed.

        Args:
            i (int): Row index.

        Returns:
            bool: If row is complete.
        """
        # row to check
        row = self.board[i, self.BOARD_SIDE_FILL_COLUMNS:self.BOARD_SIZE[1] - self.BOARD_SIDE_FILL_COLUMNS]

        # check if row is complete
        for block in row:
            if block == 0 or block == self.BOARD_FILL_VALUE:
                return False
        
        return True


    def shift_rows_down(self, down_rows: int, start_row: int, end_row=None):
        """Shift rows down a specified number of times. Shifts in empty rows with hidden area filled.

        Args:
            down_rows (int): Number of rows to move down.
            start_row (int): Lower bound index of rows to shift.
            end_row: Upper bound index of rows to shift. Default is top of board.
        """
        # defualt end row is top of the board
        if end_row is None:
            end_row = self.BOARD_SIZE[0]

        # shift down each row
        for row in range(start_row, end_row):
            self.board[row - down_rows] = self.board[row]

        # fill hidden areas
        self.board[(end_row - down_rows):end_row, 0:self.BOARD_SIDE_FILL_COLUMNS] = np.full((down_rows, self.BOARD_SIDE_FILL_COLUMNS), self.BOARD_FILL_VALUE)
        self.board[(end_row - down_rows):end_row, self.BOARD_SIZE[1] - self.BOARD_SIDE_FILL_COLUMNS:self.BOARD_SIZE[1]] = np.full((down_rows, self.BOARD_SIDE_FILL_COLUMNS), self.BOARD_FILL_VALUE)

    
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
        """Tetrimino initialization.
        """
        # generate a new random Tetrimino
        type_index = math.floor(random.random() * 7.0)

        # set attributes
        self.color = self.TETRIMINO_TYPES[type_index]['color']
        self.shape = self.TETRIMINO_TYPES[type_index]['shape']
        self.size = np.array(self.shape).shape
        self.location = self.TETRIMINO_TYPES[type_index]['spawn']




if __name__ == "__main__":
    tetris = TetrisGame()
    tetris.play()
    