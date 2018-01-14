import sys
import pygame
import numpy as np
import time

block_level =  0

# All 7 different types of blocks
block_styles = [[[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [1, 0, 0, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [0, 0, 1, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [0, 1, 1, 0],
                 [0, 1, 1, 0],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [0, 1, 1, 0],
                 [1, 1, 0, 0],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [0, 1, 0, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 0, 0]]]


# Spawns a random block
def block_spawn(board, block):
    i = 0
    for row in block:
        j = 3
        for element in row:
            board[i][j] = element
            j += 1
        i += 1


# Rotates a block
def block_rotate(block):

    for _ in range(3):
        block = np.rot90(block)

    return block


# Makes the block fall 1 level
def block_fall(board):

    global block_level

    if (block_level < 19):

        block_index = block_level + 3

        for _ in range(3):
            for j in range(0, 10):
                board[block_index][j] = board[block_index - 1][j]

            block_index -= 1

        board[block_index] = np.zeros(10, dtype=int)

        block_level += 1



def run():
    '''
    pygame.init()

    window_size = 200, 400

    screen = pygame.display.set_mode(window_size)

    open = True
    while open:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                open = False

    '''

    board = np.zeros((22, 10), dtype=np.int)

    block_spawn(board, block_rotate(block_styles[2]))

    for _ in range(26):
        block_fall(board)
        print(board)
        time.sleep(1)


run()
