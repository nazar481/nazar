import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(f'image/Bullet.png')  # импортируе картику
        self.image = pygame.transform.rotozoom(self.image, 1, 0.1)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speed = 7

    def update(self):
        self.move()
        if self.rect.bottom < 0:
            self.kill()

    def move(self):
        self.rect.y -= self.speed
