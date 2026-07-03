import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Play with Text and Font")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)

# Fill the background
screen.fill(WHITE)

# Create different fonts
font1 = pygame.font.SysFont("Arial", 40)
font2 = pygame.font.SysFont("Times New Roman", 30, bold=True)
font3 = pygame.font.SysFont("Comic Sans MS", 35, italic=True)

# Render text
text1 = font1.render("Welcome to Pygame!", True, BLUE)
text2 = font2.render("Playing with Fonts", True, RED)
text3 = font3.render("Python is Fun!", True, GREEN)

# Display text on the screen
screen.blit(text1, (150, 80))
screen.blit(text2, (170, 160))
screen.blit(text3, (200, 240))

# Update the display
pygame.display.update()

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()