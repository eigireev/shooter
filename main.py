import pygame
import sys
from random import randint

# Инициализация Pygame
pygame.init()

game_font = pygame.font.Font(None, 30)

# Задаем параметры экрана
screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

# Устанавливаем заголовок окна
pygame.display.set_caption("Awesome Shooter Game")

# Начальные координаты коробля
FIGHTER_STEP = 0.25
fighter_image = pygame.image.load('images/fighter.png') # Загружаем изображение корабля
fighter_width, fighter_height = fighter_image.get_size() # Получаем размер изображения
fighter_x, fighter_y = (screen_width / 2 - fighter_width / 2,
                        screen_height - fighter_height) # Позиция корабля по центру внизу
fighter_is_moving_left, fighter_is_moving_right = False, False # Переменные для движения

# Начальные координаты шарика
BALL_STEP = 0.3
ball_image = pygame.image.load('images/ball.png')  # Загружаем изображение шарика
ball_width, ball_height = ball_image.get_size()  # Получаем размер изображения
ball_x, ball_y = 0, 0  # Начальные координаты шарика
ball_was_fired = False  # Переменная, проверяющая, был ли шарик запущен

# Начальные координаты инопланетянина
ALIEN_STEP = 0.0125
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')  # Загружаем изображение инопланетянина
alien_width, alien_height = alien_image.get_size()  # Получаем размер изображения
alien_x, alien_y = randint(0, screen_width - alien_width), 0  # Случайная позиция инопланетянина по горизонтали

# Основной игровой цикл
game_is_running = True

game_score = 0

while game_is_running:
    for event in pygame.event.get(): # Обработка событий

        if event.type == pygame.QUIT: # Закрытие окна
            sys.exit()

        # Реакция на нажатие клавишы
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # Движение влево
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT: # Движение вправо
                fighter_is_moving_right = True

            # Реакция на нажатие пробела
            if event.key == pygame.K_SPACE: # Стрельба
                ball_was_fired = True
                ball_x = fighter_x + fighter_width / 2 - ball_width / 2 # Позиция шарика по горизонтали
                ball_y = fighter_y - ball_height # Позиция шарика по вертикали

        # Реакция на отпуск клавишы
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: # Прекращение движения влево
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT: # Прекращение движения вправо
                fighter_is_moving_right = False

    # Движение корабля
    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    # Движение инопланетянина
    alien_y += alien_speed

    # Проверка на то, чтобы шарик не выходил за пределы экрана
    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False
    if ball_was_fired:
        ball_y -= BALL_STEP

    # Вывод изображений на экран
    screen.fill(screen_fill_color) # Заполнение фона цветом
    screen.blit(fighter_image, (fighter_x, fighter_y))  # Рисуем корабль
    screen.blit(alien_image, (alien_x, alien_y))  # Рисуем инопланетянина

    if ball_was_fired: # Если шарик был запущен, рисуем его
        screen.blit(ball_image, (ball_x, ball_y))

    game_score_text = game_font.render(f"Your score is: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    # Обновление экрана
    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False

    # Попадание шарика в инопланетянина
    if ball_was_fired and \
            alien_x < ball_x < alien_x + alien_width - ball_width and \
            alien_y < ball_y < alien_y + alien_height - ball_height:
        ball_was_fired = False
        alien_x, alien_y = randint(0, screen_width - alien_width), 0
        alien_speed += ALIEN_STEP / 2 # ускорение инопланетянина
        game_score += 1

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()



