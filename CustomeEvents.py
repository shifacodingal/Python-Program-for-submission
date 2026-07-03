import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Custom Event Example")

CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 2000)

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0)
]

background = (255, 255, 255)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == CHANGE_COLOR:
            background = random.choice(colors)

    screen.fill(background)

    pygame.display.update()

pygame.quit()