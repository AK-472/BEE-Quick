# Modules
import pygame
from os import path
from pygame.locals import *
pygame.init()

# Screen
screen_size = screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode(screen_size)

# Title and Icon
title = pygame.display.set_caption("Neverending")
icon = pygame.image.load(path.join("Images", "icon.png"))
pygame.display.set_icon(icon)

# Game Vars
clock = pygame.time.Clock()
FPS = 60

# Images
credit = pygame.transform.scale(pygame.image.load(
    path.join("Images", "credits.png")), (1000, 600))

# Gameloop


def credition():

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(credit, (0, 0))
        pygame.display.update()
