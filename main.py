# Modules
import pygame
import sys
from os import path
from random import randint
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
font = pygame.font.SysFont("ttf", 100)
FPS = 60
VELOCITY_X = 8
VELOCITY_Y = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GOLD = (171, 127, 44)

# Images
bee = pygame.transform.scale(pygame.image.load(
    path.join("Images", "bee.png")), (50, 50))
wasp = pygame.transform.scale(pygame.transform.flip(
    pygame.image.load(path.join("Images", "wasp.png")), True, False), (50, 50))
background = pygame.transform.scale(pygame.image.load(
    path.join("Images", "background.png")), (1000, 600))
flower_1 = pygame.transform.scale(pygame.image.load(
    path.join("Images", "flower_1.png")), (50, 50))
honey = pygame.transform.scale(pygame.image.load(
    path.join("Images", "honey.png")), (50, 50))


# Sounds
collect = pygame.mixer.Sound(path.join("Sounds", "collect.wav"))
hurt = pygame.mixer.Sound(path.join("Sounds", "hurt.wav"))
restore = pygame.mixer.Sound(path.join("Sounds", "restore.wav"))
lose = pygame.mixer.Sound(path.join("Sounds", "lose.wav"))
song = pygame.mixer_music.load(path.join("Sounds", "song.wav"))

# Player Physics


def player_physics(player):
    key_press = pygame.key.get_pressed()

    # Gravity
    player.y += VELOCITY_Y

    # Key Input
    if key_press[K_SPACE]:
        player.y -= VELOCITY_Y * 2

    # Floor/Ceiling
    if player.bottom >= 600:
        player.y = 550
    if player.top <= 0:
        player.y = 0


# Blit onto screen
def draw(player, enemies, currency, lives, LIVES, SCORE):
    # Background
    screen.blit(background, (0, 0))

    # Player
    screen.blit(bee, (player.x, player.y))

    # Sprites
    for sprite in enemies:
        screen.blit(wasp, (sprite.x, sprite.y))

    for flower in currency:
        screen.blit(flower_1, (flower.x, flower.y))
    
    for life in lives:
        screen.blit(honey, (life.x, life.y))

    screen.blit(font.render(f"Score: {SCORE}", True, WHITE), (0, 0))
    screen.blit(font.render(f"Lives: {LIVES}", True, WHITE), (675, 0))

    pygame.display.update()

# Gameloop


def game():
    global LIVES, SCORE
    LIVES = 3
    SCORE = 0
    # Rects
    enemies = [pygame.Rect(1100, randint(0, 550), 50, 50), pygame.Rect(
        1100, randint(0, 550), 50, 50), pygame.Rect(1100, randint(0, 550), 50, 50)]
    currency = [pygame.Rect(1100, randint(0, 550), 50, 50),
                pygame.Rect(1100, randint(0, 550), 50, 50)]
    lives = [pygame.Rect(1100, randint(0, 550), 50, 50)]
    player = pygame.Rect(100, 550, 50, 50)
    pygame.mixer_music.play(-1)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        player_physics(player)

        # Life Physics
        for life in lives:
            life.x -= 0.00000001
            if life.x == -100:
                life.x = 1100
                life.y = randint(0, 550)
            if player.colliderect(life):
                restore.play()
                life.x = 1100
                life.y = randint(0, 550)
                LIVES += 1
                

        # Currency Physics
        for flower in currency:
            flower.x -= VELOCITY_X / 2
            if flower.x == -100:
                flower.x = 1100
                flower.y = randint(0, 550)
            if player.colliderect(flower):
                collect.play()
                flower.x = 1100
                flower.y = randint(0, 550)
                SCORE += 1
                

        # Enemy Physics
        for sprite in enemies:
            sprite.x -= VELOCITY_X
            if sprite.x == -100:
                sprite.x = 1100
                sprite.y = randint(0, 550)
            if player.colliderect(sprite):
                hurt.play()
                sprite.x = 1100
                sprite.y = randint(0, 550)
                LIVES -= 1

        if LIVES == 0:
            lose.play()
            sys.exit()  

        draw(player, enemies, currency, lives, LIVES, SCORE)
