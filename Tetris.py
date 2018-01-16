import sys
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


def run():

    # Pygame setup
    pygame.init()
    pygame.display.set_mode((200, 440))

    board = np.zeros((22, 10), dtype=np.int)   # Creates an array initialized to zeros to represent the game board

    block = block_spawn()
    block_draw(board, block, 1)

    while True:

        # Event object for pygame
        events = pygame.event.get()

        print("\n\n")

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

                    # Close window event
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        pygame.quit()
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

        time.sleep(0.5)


run()
