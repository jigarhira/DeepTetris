import pygame
import numpy as np
import random
import time


screen = 0

width = 200
height = 400
window_title = 'Deep Tetris'

board = []

# Colors
CYAN = (60, 255, 255)
BLUE = (0, 30, 200)
ORANGE = (255, 170, 30)
YELLOW = (255, 255, 0)
GREEN = (0, 230, 0)
PURPLE = (100, 0, 150)
RED = (255, 0, 0)
GREY = (150, 150, 150)
BLACK = (0, 0, 0)


# Tetromino patterns
tetromino = [
    [[0,2],[1,2],[2,2],[3,2]], #0

    [[1,1],[1,2],[2,2],[3,2]], #1

    [[3,1],[1,2],[2,2],[3,2]], #2

    [[1,1],[1,2],[2,1],[2,2]], #3

    [[2,1],[3,1],[1,2],[2,2]], #4

    [[2,1],[1,2],[2,2],[3,2]], #5

    [[1.1],[2,1],[2,2],[3,2]]  #6
]

def tetris():

    game_init()

    # Play game loop
    while not check_events():
        game(board)


# Checks the pygame events
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Close window event
            return True

    return False


# Game initialization
def game_init():
    create_window()
    pygame.display.flip()   # updates the window
    global board
    board = np.zeros((10, 22), dtype=np.int8)   # initializes the board to zeros



# Main game
def game(board):
    shape_type = random.randint(0, 6)   # generates a random shape
    active_shape = spawn_shape(shape_type, board)

    for i in range(0, 10):
        active_shape = drop_shape(active_shape, board)

        draw_board(board)
        time.sleep(1)



# Creates game window
def create_window():
    (w, h) = (width, height)
    global screen
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption(window_title)
    return screen


# Move the shape down by one unit
def drop_shape(shape_coords, board):
    # shape marker
    shape_type = board[shape_coords[0][0]][shape_coords[0][1]]

    # new coords
    new_coords = [[],[],[],[]]

    # move down each block
    for i in range(3, -1, -1):  # iterate the list in reverse to start at the bottom blocks of the shape
        block = shape_coords[i]
        if ((board[block[0]][block[1] + 1] == 0) or (board[block[0]][block[1] + 1] == shape_type)) and (block[1] != 21):    # checks if we can move a block down
            board[block[0]][block[1] + 1] = shape_type
            new_coords[i] = [block[0], block[1] + 1]
            board[block[0]][block[1]] = 0

    return new_coords







# Checks if the shape can move lower, if not it adds the shape to the background blocks
def update_background(shape_coords, board):
    # drop the shape
    drop_shape(shape_coords, board)



# Spawn in a new shape
def spawn_shape(shape_type, board):
    # coords of the initial spawn location
    x_spawn = 3
    y_spawn = 0

    # gets the pattern of the shape
    shape = tetromino[shape_type]

    # board coord of active shape (so we know exactly where the active blocks are)
    active_shape = [[],[],[],[]]

    # iterate through the blocks
    for i in range(0,4):
        if board[x_spawn + shape[i][0]][y_spawn + shape[i][1]] == 0:  # checks for empty space
            board[x_spawn + shape[i][0]][y_spawn + shape[i][1]] = shape_type + 1
            active_shape[i] = [x_spawn + shape[i][0], y_spawn + shape[i][1]] # keeps track of the coordinates
        else:   # space taken
            pass    # GAME LOSS

    return active_shape


# Draw a block
def draw_block(x, y, color):
    # Draws the block onto the window
    pygame.draw.rect(screen, color, (x * (width / 10), (y * (width / 10)) - (2 * (width / 10)), (x * (width / 10)) + (width / 10), (y * (width / 10)) + (width / 10) - (2 * (width / 10)))) # -20 is so we do not display the top two lines


# Draws board to the screen
def draw_board(board):
    for i in range(10):
        for j in range(2, 22):
            if board[i][j] == 1:
                draw_block(i, j, CYAN)  # 1-7 are the colors
            elif board[i][j] == 2:
                draw_block(i, j, BLUE)
            elif board[i][j] == 3:
                draw_block(i, j, ORANGE)
            elif board[i][j] == 4:
                draw_block(i, j, YELLOW)
            elif board[i][j] == 5:
                draw_block(i, j, GREEN)
            elif board[i][j] == 6:
                draw_block(i, j, PURPLE)
            elif board[i][j] == 7:
                draw_block(i, j, RED)
            elif board[i][j] == 9:
                draw_block(i, j, GREY)  # 9 filled
            else:
                draw_block(i, j, BLACK) # 0 empty

    # updates the display
    pygame.display.flip()





if __name__ == '__main__':
    tetris()
