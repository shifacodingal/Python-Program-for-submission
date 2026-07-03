import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Add Sprites")

class Box(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_sprites = pygame.sprite.Group()

box1 = Box((255, 0, 0), 50, 100)
box2 = Box((0, 255, 0), 200, 100)
box3 = Box((0, 0, 255), 350, 100)

all_sprites.add(box1, box2, box3)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()