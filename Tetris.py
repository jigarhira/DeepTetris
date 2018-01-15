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
    rand = random.randint(0,6)
    b = Block(rand, 3, 0)

    return b

# Draws the block to the board
def block_draw(board, block):
    board[block.getSCoord(block.s0_coord)[1]][block.getSCoord(block.s0_coord)[0]] = 1
    board[block.getSCoord(block.s1_coord)[1]][block.getSCoord(block.s1_coord)[0]] = 1
    board[block.getSCoord(block.s2_coord)[1]][block.getSCoord(block.s2_coord)[0]] = 1
    board[block.getSCoord(block.s3_coord)[1]][block.getSCoord(block.s3_coord)[0]] = 1


# Clears the block from the board
def block_clear(board, block):
    board[block.getSCoord(block.s0_coord)[1]][block.getSCoord(block.s0_coord)[0]] = 0
    board[block.getSCoord(block.s1_coord)[1]][block.getSCoord(block.s1_coord)[0]] = 0
    board[block.getSCoord(block.s2_coord)[1]][block.getSCoord(block.s2_coord)[0]] = 0
    board[block.getSCoord(block.s3_coord)[1]][block.getSCoord(block.s3_coord)[0]] = 0


def run():
    board = np.zeros((22, 10), dtype=np.int)   # Creates an array initialized to zeros to represent the game board

    block = block_spawn()
    block_draw(board, block)

    while True:

        print("\n\n")

        try:

            if (((block.getSCoord(block.s0_coord)[1] < 21) and
                 (block.getSCoord(block.s1_coord)[1] < 21) and
                 (block.getSCoord(block.s2_coord)[1] < 21) and
                 (block.getSCoord(block.s3_coord)[1] < 21)) and
                ((board[(block.getSCoord(block.s0_coord)[1]) + 1][block.getSCoord(block.s0_coord)[0]] != 2) and
                 (board[(block.getSCoord(block.s1_coord)[1]) + 1][block.getSCoord(block.s1_coord)[0]] != 2) and
                 (board[(block.getSCoord(block.s2_coord)[1]) + 1][block.getSCoord(block.s2_coord)[0]] != 2) and
                 (board[(block.getSCoord(block.s3_coord)[1]) + 1][block.getSCoord(block.s3_coord)[0]] != 2))):

                block_clear(board, block)
                block.down()
                block_draw(board, block)

                print(board)

            else:
                board[block.getSCoord(block.s0_coord)[1]][block.getSCoord(block.s0_coord)[0]] = 2
                board[block.getSCoord(block.s1_coord)[1]][block.getSCoord(block.s1_coord)[0]] = 2
                board[block.getSCoord(block.s2_coord)[1]][block.getSCoord(block.s2_coord)[0]] = 2
                board[block.getSCoord(block.s3_coord)[1]][block.getSCoord(block.s3_coord)[0]] = 2

                block = block_spawn()

                print(board)

        except IndexError:
            pass

        time.sleep(0.5)



run()
