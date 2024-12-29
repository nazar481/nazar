import pygame
import hero_class
import enemy_class

pygame.init()  # предварительный запуск зависимостей
clock = pygame.time.Clock()  # создание экземпляра класса слок
GREEN = (0, 255, 0)  # задаём цвета для удобной работы
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen_size = width, height = 800, 800  # задаём ширину высоту для удобной работы
screen = pygame.display.set_mode(screen_size)  # задаём размер экрана
pygame.display.set_caption('Моя игра')  # название окна

hero1 = hero_class.Player(width, height)  # создание экземпляра класса
hero2 = hero_class.Player(
    width, height, 2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, size_image=0.09
)

all_enemy = pygame.sprite.Group()

def create_enemy_group(num_enemies):
    for _ in range(num_enemies):  # создать num_enemies врагов
        mob = enemy_class.Enemy(width, height)
        all_enemy.add(mob)

create_enemy_group(10)  # создаем начальную группу врагов

running = True  # игровой цикл

while running:  # запуск игрового цикла
    screen.fill(BLACK)
    clock.tick(60)  # устанавливаем количество игровых фреймов в секунду (повторений while)

    for event in pygame.event.get():  # перебираем все события
        if event.type == pygame.QUIT:  # если нажали на крестик
            running = False

    hero1.update()  # обновление расположения корабля
    hero2.update()

    # обновление врагов
    all_enemy.update()

    # Проверка и создание новых врагов, если их меньше девяти
    if len(all_enemy) < 9:
        create_enemy_group(1)  # Добавляем одного врага

    # отрисовка врагов
    all_enemy.draw(screen)

    hero1.all_bullet.update()
    hero2.all_bullet.update()
    hero1.all_bullet.draw(screen)
    hero2.all_bullet.draw(screen)

    if pygame.sprite.spritecollide(hero1, all_enemy, False):  # остановка программы если спрайты столкнулись
        print("Hero 1 has been hit!")
        running = False

    if pygame.sprite.spritecollide(hero2, all_enemy, False):  # аналогично для второго героя
        print("Hero 2 has been hit!")
        running = False

    for bullet in hero1.all_bullet:
        hit_enemies = pygame.sprite.spritecollide(bullet, all_enemy, True)  # Удаляем врагов при попадании
        if hit_enemies:
            bullet.kill()

    for bullet in hero2.all_bullet:
        hit_enemies = pygame.sprite.spritecollide(bullet, all_enemy, True)  # Удаляем врагов при попадании
        if hit_enemies:
            bullet.kill()

    screen.blit(hero1.image, hero1.rect)  # отрисовка кораблика
    screen.blit(hero2.image, hero2.rect)  # отрисовка кораблика

    pygame.display.update()  # обновляем наш дисплей

pygame.quit()  # завершаем все зависимости pygame
