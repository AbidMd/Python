import pygame
import sys
import random

pygame.init()

class Snake(object):
    pass

class Food(object):
    pass

def drawGrid(surface):
    pass

#game variables
WIDTH = 800
HEIGHT = 600

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