import pygame
from pygame.locals import *
import os
import sys

pygame.init()
clock = pygame.time.Clock()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('FRACTALIS')

done = False

while not done:
    clock.tick()

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    pygame.display.update()

pygame.quit()
sys.exit()