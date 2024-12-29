import pygame
from bullet_hero import Bullet



class Player(pygame.sprite.Sprite):  # наследуем класс от класса спрайтов

    def __init__(self, w, h, number_image=1,
                 k_move_forward=pygame.K_w, k_move_backward=pygame.K_s,
                 k_move_left=pygame.K_a,
                 k_move_right=pygame.K_d,
                 size_image=0.15):  # создаём иницилизатор класса ( запускаеться при созданиее экземпляра класса)
        super().__init__()  # наследуем свойства родителя
        self.h, self.w = h, w  # созраняем в аргументы ширины высоты
        self.image = pygame.image.load(f'image/playerShip{number_image}_orange.png')  # импортируе картику
        self.image = pygame.transform.rotozoom(self.image, 1, size_image)  # кортинку уменьшаем
        self.rect = self.image.get_rect()  # получаем кординаты кортинки , для работы с ней
        self.rect.centerx = 0 + 200 * number_image  # размещаем корабль при создании центр ширина
        self.rect.centery = self.h // 1.5  # размещаем корабль при создании почти центр высота
        self.speedx = 0  # скорость по x
        self.speedy = 0  # скорость по y
        self.k_move_forward, self.k_move_backward, self.k_move_left, self.k_move_right = (
            k_move_forward, k_move_backward, k_move_left, k_move_right
        )
        self.all_bullet = pygame.sprite.Group()
        self.speed_shooting = 15
        self.speed_shooting_quantity = 0
    def update(self):  # отвечает за все изменения персонажа
        self.move()  # вызываем функцию передвижения

    def draw(self, screen):  # потенциально , тут отрисовываем наш корабль
        pass

    def move(self):
        self.speedx = 0  # при каждом вызове обнуляем скорость
        self.speedy = 0

        key_pres = pygame.key.get_pressed()  # достаём какие клавиши нажаты
        if key_pres[pygame.K_SPACE]:
            self.speed_shooting_quantity += 1
            if self.speed_shooting_quantity >= self.speed_shooting:
                self.shoot()
                self.speed_shooting_quantity = 0
        else:
            self.speed_shooting_quantity = self.speed_shooting
        if key_pres[self.k_move_forward]:  # проверяем нажато ли движение в перёд W
            self.speedy -= 4  # изменяем скорость до следующего вызова defmove
        if key_pres[self.k_move_backward]:
            self.speedy += 4
        if key_pres[self.k_move_left]:
            self.speedx -= 4
        if key_pres[self.k_move_right]:
            self.speedx += 4
        if self.rect.bottom > self.h:  # если низ коробля , ниже границы экрана
            self.rect.bottom = self.h
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.w:
            self.rect.right = self.w

        self.rect.centery += self.speedy  # увеличиваем кординаты коробля на его скорость
        self.rect.centerx += self.speedx  # увеличиваем кординаты коробля на его скорость

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        self.all_bullet.add(bullet)