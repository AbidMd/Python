import pygame
import sys
import random

pygame.init()

class Snake(object):
    pass

class Food(object):
    pass

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if ((x + y) % 2 == 0):
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, gray1, rect)
            else:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, gray2, rect)

#game variables library
WIDTH = 480
HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE

# Colors
gray1 = (93, 216, 228)
gray2 = (84, 194, 205)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    drawGrid()

    snake = Snake()
    food = Food()

    while True:
        clock.tick(10)

        # snake + food subfuctions
        drawGrid(surface)
        pygame.display.update()
main()