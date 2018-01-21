import pygame
import numpy as np
import time
import random

from Block import Block

'''
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
'''

'''
--~~*TODO*~~--
BUG: rotating can phase through existing blocks
BUG: index exception not properly handled for right block movement
BUG: rotating near edge of the board can cause IndexError

CLEAN: create functions and clean repetitive code in Tetris.py and Block.py

TEST: test is completed lines above the bottom get cleared

'''


# Closes the window
def pygame_close():
    pygame.display.quit()
    pygame.quit()


# Creates a new Block object of a random type
def block_spawn():
    rand = random.randint(0, 6)
    b = Block(rand, 3, 0)

    return b


# Draws the block to the board with a placeholder
def block_draw(board, block, num):
    board[block.getSCoord(block.s0_coord)[1]][block.getSCoord(block.s0_coord)[0]] = num
    board[block.getSCoord(block.s1_coord)[1]][block.getSCoord(block.s1_coord)[0]] = num
    board[block.getSCoord(block.s2_coord)[1]][block.getSCoord(block.s2_coord)[0]] = num
    board[block.getSCoord(block.s3_coord)[1]][block.getSCoord(block.s3_coord)[0]] = num


# Checks if the block has hit the bottom of the board
def block_is_bottom(block):
    return ((block.getSCoord(block.s0_coord)[1] < 21) and
            (block.getSCoord(block.s1_coord)[1] < 21) and
            (block.getSCoord(block.s2_coord)[1] < 21) and
            (block.getSCoord(block.s3_coord)[1] < 21))


# Checks if the block has hit another block
def block_hit_block(board, block):
    return ((board[(block.getSCoord(block.s0_coord)[1]) + 1][block.getSCoord(block.s0_coord)[0]] != 2) and
            (board[(block.getSCoord(block.s1_coord)[1]) + 1][block.getSCoord(block.s1_coord)[0]] != 2) and
            (board[(block.getSCoord(block.s2_coord)[1]) + 1][block.getSCoord(block.s2_coord)[0]] != 2) and
            (board[(block.getSCoord(block.s3_coord)[1]) + 1][block.getSCoord(block.s3_coord)[0]] != 2))


# Checks for lines that need to be cleared
def board_get_clear_level(board):
    for row in range(21, 2, -1):
        clear = 1

        for element in board[row]:
            if element != 2:
                clear = 0

        if clear == 1:
            print("clear")
            return row
        else:
            return 0


# Clears the bottom lines of the board
def board_clear_lines(board, level):
    if level != 0:
        for row in range(level, 2, -1):
            for i in range(10):
                board[row][i] = board[row - 1][i]


def run():
    # Pygame setup
    pygame.init()
    pygame.display.set_mode((200, 440))

    board = np.zeros((22, 10), dtype=np.int)  # Creates an array initialized to zeros to represent the game board

    old_time = time.time()  # Saves first time

    # Creates and draws a block
    block = block_spawn()
    block_draw(board, block, 1)

    while True:

        # Event object for pygame
        events = pygame.event.get()

        # Clears any completed lines
        board_clear_lines(board, board_get_clear_level(board))

        # Checks if the stack reaches the top of the screen
        for element in board[2]:
            if element == 2:
                return

        if block_is_bottom(block) and block_hit_block(board, block):
            # Event handler for pygame events
            for event in events:
                # Keypress events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if ((board[block.getSCoord(block.s0_coord)[1]][block.getSCoord(block.s0_coord)[0] - 1] != 2) and
                                (board[block.getSCoord(block.s1_coord)[1]][
                                     block.getSCoord(block.s1_coord)[0] - 1] != 2) and
                                (board[block.getSCoord(block.s2_coord)[1]][
                                     block.getSCoord(block.s2_coord)[0] - 1] != 2) and
                                (board[block.getSCoord(block.s3_coord)[1]][
                                     block.getSCoord(block.s3_coord)[0] - 1] != 2)):
                            block_draw(board, block, 0)
                            block.left()
                            block_draw(board, block, 1)
                    if event.key == pygame.K_RIGHT:
                        # if block.location()[2] < 9: # FIX THIS BUG HERE
                        try:
                            if ((board[block.getSCoord(block.s0_coord)[1]][
                                     block.getSCoord(block.s0_coord)[0] + 1] != 2) and
                                    (board[block.getSCoord(block.s1_coord)[1]][
                                         block.getSCoord(block.s1_coord)[0] + 1] != 2) and
                                    (board[block.getSCoord(block.s2_coord)[1]][
                                         block.getSCoord(block.s2_coord)[0] + 1] != 2) and
                                    (board[block.getSCoord(block.s3_coord)[1]][
                                         block.getSCoord(block.s3_coord)[0] + 1] != 2)):
                                block_draw(board, block, 0)
                                block.right()
                                block_draw(board, block, 1)
                        except IndexError:
                            block_draw(board, block, 0)
                            block.right()
                            block_draw(board, block, 1)
                    if event.key == pygame.K_UP:
                        block_draw(board, block, 0)
                        block.rotate()
                        block_draw(board, block, 1)

                # Close window event
                if event.type == pygame.QUIT:
                    return

        else:
            block_draw(board, block, 2)
            block = block_spawn()

        # Executes every second
        if time.time() >= old_time + 0.5:
            old_time = time.time()

            if block_is_bottom(block) and block_hit_block(board, block):
                block_draw(board, block, 0)
                block.down()
                block_draw(board, block, 1)

            print("\n\n")
            print(board)

        '''
        try:

            if block_is_bottom(block) and block_hit_block(board, block):
                block_draw(board, block, 0)

                # Event handler for pygame events
                for event in events:
                    # Keypress events
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            block.left()
                        if event.key == pygame.K_RIGHT:
                            block.right()
                        if event.key == pygame.K_UP:
                            block.rotate()

                    # Close window event
                    if event.type == pygame.QUIT:
                        return

                block.down()
                block_draw(board, block, 1)

                print(board)

            else:
                block_draw(board, block, 2)

                block = block_spawn()

                print(board)

        except IndexError:
            pass
        '''


run()
pygame_close()
