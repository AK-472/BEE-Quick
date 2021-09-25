# Modules
import pygame
import sys
from main import game
from credit import credition
from os import path
from random import randint
from pygame.locals import *
pygame.init()

# Screen
screen_size = screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode(screen_size)

# Title and Icon
title = pygame.display.set_caption("Neverending")

# Game Vars
clock = pygame.time.Clock()
large_font = pygame.font.SysFont("ttf", 125)
font = pygame.font.SysFont("ttf", 100)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Button text
start = font.render("Start Game", True, GREEN)
quits = font.render("Quit Game", True, RED)
credit = font.render("Credits", True, BLUE)

# Sounds
song = pygame.mixer_music.load(path.join("Sounds", "song.wav"))

# Blit onto screen


def draw(start_button, quit_button, credit_button, mouse_rect, mouse_press):
    screen.fill(BLACK)
    screen.blit(large_font.render("BEE Quick", True, YELLOW), (275, 50))
    screen.blit(start, (start_button.x, start_button.y))
    screen.blit(quits, (quit_button.x, quit_button.y))
    screen.blit(credit, (credit_button.x, credit_button.y))

    if mouse_press[0]:
        if mouse_rect.colliderect(start_button):
            game()
        if mouse_rect.colliderect(quit_button):
            sys.exit()
        if mouse_rect.colliderect(credit_button): 
            credition()
    pygame.display.update()

# Gameloop


def main():
    # Rects
    start_button = start.get_rect(x=310, y=200)
    quit_button = quits.get_rect(x=310, y=325)
    credit_button = credit.get_rect(x=370, y=450)
    pygame.mixer_music.play(-1)
    running = True
    while running:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 16, 16)
        mouse_press = pygame.mouse.get_pressed(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        draw(start_button, quit_button, credit_button, mouse_rect, mouse_press)


if __name__ == "__main__":
    main()
