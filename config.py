import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Error Detection IQ Test')

# Constants for Set 1 and Set 2 display
SIZE, OFFSET, PARTITION = 60, 2, 25
FONT = pygame.font.SysFont("Arial", 20)

SET1_ORIGIN_X = WIDTH / 2 - (SIZE * 3 + OFFSET * 4 + PARTITION)
SET1_ORIGIN_Y = PARTITION * 5
SET2_ORIGIN_X = WIDTH / 2 + PARTITION
SET2_ORIGIN_Y = SET1_ORIGIN_Y
SET_WIDTH = SIZE * 3 + OFFSET * 4
SET_HEIGHT = SIZE * 3 + OFFSET * 4
SET1_RECT = (SET1_ORIGIN_X, SET1_ORIGIN_Y, SET_WIDTH, SET_HEIGHT)
SET2_RECT = (SET2_ORIGIN_X, SET2_ORIGIN_Y, SET_WIDTH, SET_HEIGHT)
SET_DIMENSION = 3  # Determines how many rows and columns in the set

# Constants for keys display
KEY_SIZE = 35
KEYS_ORIGIN_X = WIDTH / 2 - (KEY_SIZE * 2.5 + OFFSET * 3)
KEYS_ORIGIN_Y = SET1_ORIGIN_Y + SET_HEIGHT + PARTITION
KEYS_WIDTH = KEY_SIZE * 5 + OFFSET * 6
KEYS_HEIGHT = KEY_SIZE * 2 + OFFSET * 3
KEYS_RECT = (KEYS_ORIGIN_X, KEYS_ORIGIN_Y, KEYS_WIDTH, KEYS_HEIGHT)

# Color constants
WHITE = (255, 255, 255)
BACKGROUND = (47, 247, 206)
BLACK = (0, 0, 0)
GREY = (163, 163, 159)


def create_positions():
    """
    Create positions for items in Set 1 and Set 2.
    """
    mirror_dist = SIZE * 3 + OFFSET * 4 + PARTITION * 2
    positions_set1 = {}
    positions_set2 = {}

    for row in range(SET_DIMENSION):
        for col in range(SET_DIMENSION):
            # Creating positions for Set 1
            position_id_1 = col + row * SET_DIMENSION + 1
            x1 = SET1_ORIGIN_X + SIZE * col + OFFSET * (col + 1)
            y1 = SET1_ORIGIN_Y + SIZE * row + OFFSET * (row + 1)
            positions_set1[position_id_1] = (int(x1), int(y1))

            # Creating positions for Set 2
            position_id_2 = position_id_1 + 9
            x2 = x1 + mirror_dist
            y2 = y1
            positions_set2[position_id_2] = (int(x2), int(y2))

    return positions_set1, positions_set2


pos_1, pos_2 = create_positions()

# Dictionary of colors
colors = {'red': (235, 58, 61), 'green': (55, 196, 57), 'blue': (37, 150, 190),
          'orange': (226, 135, 67), 'black': (0, 0, 0), 'yellow': (210, 210, 27),
          'purple': (146, 53, 189), 'brown': (135, 62, 35)}

# List of available shapes
shapes = ['circle', 'triangle', 'square', 'diamond', 'pentagon']

# List of available characters
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z',
         '!', '@', '#', '$', '%', '&', '+']
