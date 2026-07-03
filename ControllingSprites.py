import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Controlling Sprites")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.center = (250, 200)

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if keys[pygame.K_UP]:
            self.rect.y -= 5

        if keys[pygame.K_DOWN]:
            self.rect.y += 5

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((255, 255, 255))

    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()