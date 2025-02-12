import pygame
import sys
# from random import randint - для вызова рандомного фона


# clock = pygame.time.Clock() - замедление обновления фона до 1 в сек.

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My pygame")
fill_color = (32, 52, 71)

rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')

STEP = 10

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y = rect_y - STEP # rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP

    # screen.fill(pygame.Color('yellow')) - цвет фона желтый
    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255))) - для вызова рандомного фона
    screen.fill(fill_color) # нижний слой
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height)) # верхний слой
    pygame.display.update()

    # clock.tick(1) - замедление обновления фона до 1 в сек.