import pygame

# Initialize Pygame
pygame.init()

# Window size
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blocks Collision")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Block size
block_size = 50

# Player block
player = pygame.Rect(50, 150, block_size, block_size)

# Enemy block
enemy = pygame.Rect(400, 150, block_size, block_size)

# Movement speed
speed = 5

clock = pygame.time.Clock()

running = True

while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed

    if keys[pygame.K_RIGHT]:
        player.x += speed

    if keys[pygame.K_UP]:
        player.y -= speed

    if keys[pygame.K_DOWN]:
        player.y += speed

    # Check collision
    collision = player.colliderect(enemy)

    # Background
    screen.fill(WHITE)

    # Draw enemy
    pygame.draw.rect(screen, RED, enemy)

    # Change player color on collision
    if collision:
        pygame.draw.rect(screen, RED, player)
    else:
        pygame.draw.rect(screen, BLUE, player)

    # Display message
    font = pygame.font.SysFont("Arial", 28)

    if collision:
        text = font.render("Collision Detected!", True, RED)
    else:
        text = font.render("Move Blue Block", True, (0, 150, 0))

    screen.blit(text, (150, 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()