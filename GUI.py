import pygame


# Draws a block onto the screen
def draw_block(screen, index_x, index_y, color):
    # Dictionary to store the RGB data for each color
    color_data = {
        0: (0, 0, 0),
        1: (175, 175, 175),
        2: (66, 241, 244),
        3: (28, 42, 239),
        4: (247, 190, 59),
        5: (255, 255, 0),
        6: (84, 255, 79),
        7: (183, 61, 255),
        8: (255, 0, 0)
    }

    # Creates a tuple to store the rgb values
    rgb = color_data.get(color)

    # Converts the array index values to pixel coords
    pixel_x = index_x * 20
    pixel_y = (index_y * 20) - 40

    pygame.draw.rect(screen, rgb, (pixel_x, pixel_y, 20, 20))

    #pygame.display.update()


# Draws the board onto the screen
def draw_board(screen, board):
    # Clear screen
    screen.fill((0, 0, 0))

    # Draw squares
    for row in range(21, 1, -1):
        for index in range(10):
            draw_block(screen, index, row, board[row][index])

    # Update the screen
    pygame.display.update()
