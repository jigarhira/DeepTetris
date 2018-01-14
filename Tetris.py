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


def run():
    board = np.zeros((22, 10), dtype=np.int)   # Creates an array initialized to zeros to represent the game board

    block = block_spawn()

    board[block.s0_coord[1]][block.s0_coord[0]] = 1
    board[block.s1_coord[1]][block.s1_coord[0]] = 1
    board[block.s2_coord[1]][block.s2_coord[0]] = 1
    board[block.s3_coord[1]][block.s3_coord[0]] = 1


    print(board)


run()
