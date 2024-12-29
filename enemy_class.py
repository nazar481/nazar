
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self,  w, h,):
        super().__init__()  # наследуем свойства родителя
        self.h, self.w = h, w

        # Загружаем изображение врага
        self.image = pygame.image.load('image/''shreck.png')
        self.rect = self.image.get_rect()

        # Задаем случайные координаты
        self.rect.x = random.randint(0, w - self.rect.width)
        self.rect.y = random.randint(-100, -40)  # Начальная позиция врага выше экрана

        # Задаем скорость врага
        self.speed = random.randint(2, 5)
        self.horizontal_speed = random.choice([-1, 1]) * random.randint(0, 3)

    def update(self):
        self.move()

        # Удаляем врагов, если они вышли за границу экрана
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()  # Удаляем врага из группы

    def move(self):
        # Логика изменения координат
        self.rect.y += self.speed  # Движение вниз
        self.rect.x += self.horizontal_speed  # Движение вбок

        # Ограничение движения по границам экрана
        if self.rect.left < 0:
            self.rect.left = 0
            self.horizontal_speed = abs(self.horizontal_speed)  # Меняем направление на право
        if self.rect.right > pygame.display.get_surface().get_width():
            self.rect.right = pygame.display.get_surface().get_width()
            self.horizontal_speed = -abs(self.horizontal_speed)  # Меняем направление на лево
