import pygame
from sys import exit
from os import system

import board
import snake
import food
from constances import *

system('cls')
pygame.init()

# COLOR
BLACK = pygame.Color(black)
WHITE = pygame.Color(white)
GREEN = pygame.Color(green)
LIGHT_GREEN = pygame.Color(light_green)
RED = pygame.Color(red)

# WINDOW
pygame.display.set_caption(screen_title)
screen = pygame.display.set_mode((screen_size, screen_size))

# BOARD, SNAKE, FOOD
snake = snake.Snake()
food = food.Food(snake)
board = board.Board(nb_cases, snake, food)

# GRID
x = 0
for i in range(nb_cases - 1):
    x += case_width
    pygame.draw.line(screen, WHITE, (x, 0), (x, screen_size), line_width)

y = 0
for i in range(nb_cases - 1):
    y += case_width
    pygame.draw.line(screen, WHITE, (0, y), (screen_size, y), line_width)

# DRAW SNAKE FUNCTION
def draw_snake(snake, last_case):

    # draw the snake
    for i, coord in enumerate(snake.body):
        if i == 0:
            pygame.draw.rect(screen, GREEN, pygame.Rect((coord[0]*case_width +1, coord[1]*case_width +1), (case_width-1, case_width-1)))
        else:
            pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect((coord[0]*case_width +1, coord[1]*case_width +1), (case_width-1, case_width-1)))

    
    # remove old position
    pygame.draw.rect(screen, BLACK, pygame.Rect((last_case[0]*30+1, last_case[1]*30+1), (case_width-1, case_width-1)))

# DRAW FOOD
def draw_food(food):
     pygame.draw.rect(screen, RED, pygame.Rect((food.pos[0]*case_width +1, food.pos[1]*case_width +1), (case_width-1, case_width-1)))

# DRAW SNAKE, FOOD 
draw_snake(snake, (0, 0))
draw_food(food)

pygame.display.update()

# CLOCK
clock = pygame.time.Clock()

# GAME LOOP
while RUNNING:

    for event in pygame.event.get():

        # QUIT
        if event.type == pygame.QUIT:
            print("[WINDOW CLOSED]")
            RUNNING = False
            pygame.quit()
            exit()

        # IF GAME IS WORKING
        if GAME:

            # KEYS
            if event.type == pygame.KEYDOWN:

                # ARROWS
                if event.key == pygame.K_UP and snake.direction != 'd':
                    snake.direction = 'u'
                if event.key == pygame.K_DOWN and snake.direction != 'u':
                    snake.direction = 'd'
                if event.key == pygame.K_RIGHT and snake.direction != 'l':
                    snake.direction = 'r'
                if event.key == pygame.K_LEFT  and snake.direction != 'r':
                    snake.direction = 'l'

    # IF GAME IS WORKING
    if GAME:

        if food.check_ate(snake):
            draw_food(food)
            snake.add_case()

        last_case = snake.move()
        # try to update the board
        try:
            board.update(snake, last_case, food)
        # if we can't, he is in the wall
        except IndexError:
            print("[GAME OVER]")
            GAME = False # he loses
            continue # to not exec next lines

        # draw snake, refresh display
        draw_snake(snake, last_case)
        pygame.display.update()

        # CLOCK
        clock.tick(ticks)

