import pygame
import random

# Initialize Pygame
pygame.init()

# Window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level Up Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 30)

# Player
player = pygame.Rect(50, 50, 40, 40)
player_speed = 5

# Enemy
enemy = pygame.Rect(300, 200, 40, 40)
enemy_speed = 3

# Score and Level
score = 0
level = 1

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Keep player inside window
    player.clamp_ip(screen.get_rect())

    # Enemy Movement
    enemy.x += enemy_speed

    if enemy.right >= WIDTH or enemy.left <= 0:
        enemy_speed *= -1

    # Collision
    if player.colliderect(enemy):
        score += 1
        level += 1

        # Move enemy to a random position
        enemy.x = random.randint(50, WIDTH - 50)
        enemy.y = random.randint(50, HEIGHT - 50)

        # Increase speed
        if enemy_speed > 0:
            enemy_speed += 1
        else:
            enemy_speed -= 1

    # Drawing
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    score_text = font.render(f"Score : {score}", True, BLACK)
    level_text = font.render(f"Level : {level}", True, BLACK)

    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 60))

    pygame.display.update()
    clock.tick(60)

pygame.quit()