import pygame
from sys import exit
from os import system
from random import randint

import board
import snake
import food
from constances import *

system('cls')
pygame.init()
pygame.font.init()

# COLOR
BLACK = pygame.Color(black)
WHITE = pygame.Color(white)
LIGHT_GREEN = pygame.Color(light_green)
GREEN = pygame.Color(green)
RED = pygame.Color(red)

# WINDOW
pygame.display.set_caption(screen_title)
screen = pygame.display.set_mode((screen_size, screen_size))

# OBJECTS
snake = snake.Snake()
food = food.Food(snake)
board = board.Board(nb_cases, snake, food)

# FUNCTION
def random_color():
    """
    pick a random color
    :return: pygame.Color()
    """
    return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

def draw_snake(snake, last_case):
    """
    Draw a snake in the grid
    :param snake: Snake()
    :param last_case: 'old' last case of the snake (tuple)
    """
    # draw the snake
    for i, coord in enumerate(snake.body):
        if i == 0:
            pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect((coord[1]*case_width +1, coord[0]*case_width +1), (case_width-1, case_width-1)))
        else:
            pygame.draw.rect(screen, GREEN, pygame.Rect((coord[1]*case_width +1, coord[0]*case_width +1), (case_width-1, case_width-1)))

    
    # remove old position
    pygame.draw.rect(screen, BLACK, pygame.Rect((last_case[1]*30+1, last_case[0]*30+1), (case_width-1, case_width-1)))

# DRAW FOOD
def draw_food(food):
    """
    draw a food in the grid
    :param food: Food()
    """
    pygame.draw.rect(screen, RED, pygame.Rect((food.pos[1]*case_width +1, food.pos[0]*case_width +1), (case_width-1, case_width-1)))

# GRID
def draw_grid(nb_cases):
    """
    draw the grid in white
    :param nb_cases: the number of case in a row (same amout in a column)
    """
    x = 0
    for i in range(nb_cases - 1):
        x += case_width
        pygame.draw.line(screen, WHITE, (x, 0), (x, screen_size), line_width)

    y = 0
    for i in range(nb_cases - 1):
        y += case_width
        pygame.draw.line(screen, WHITE, (0, y), (screen_size, y), line_width)


# INIT  DRAW SNAKE, FOOD 
draw_snake(snake, (0, 0))
draw_food(food)
pygame.display.update()

# FONTS
score_font = pygame.font.SysFont(font, score_size)
score_text = score_font.render(f"score : {board.score}", True, WHITE)
screen.blit(score_text, (screen_size-100, screen_size-30))

lose_font = pygame.font.SysFont(font, lose_size)

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
                if event.key == pygame.K_UP and snake.direction != 'd' and snake.can_turn:
                    snake.direction = 'u'
                    snake.can_turn = False
                if event.key == pygame.K_DOWN and snake.direction != 'u' and snake.can_turn:
                    snake.direction = 'd'
                    snake.can_turn = False
                if event.key == pygame.K_RIGHT and snake.direction != 'l' and snake.can_turn:
                    snake.direction = 'r'
                    snake.can_turn = False
                if event.key == pygame.K_LEFT  and snake.direction != 'r' and snake.can_turn:
                    snake.direction = 'l'
                    snake.can_turn = False

    # IF GAME IS WORKING
    if GAME:

        # FOOD
        if food.check_ate(snake):
            # SCORE
            screen.fill(BLACK)
            board.score += 1
            score_text = score_font.render(f"score : {board.score}", True, WHITE)
            screen.blit(score_text, (screen_size-100, screen_size-30))
            # have to calcule the dest

            draw_food(food)
            snake.add_case()


        last_case = snake.move()
        # try to update the board
        # BOARD
        try:
            board.update(snake, last_case, food)

        # if we can't, he is in the wall
        # GAME OVER
        except IndexError:
            print("[GAME OVER]")
            GAME = False # he loses

            lose_text = lose_font.render("GAME OVER", True, WHITE)
            screen.blit(lose_text, (screen_size/2-165, screen_size/2-40))
            # have to calcule the dest
            pygame.display.update()

            continue # to not exec next lines

        # SNAKE
        draw_snake(snake, last_case)
        snake.can_turn = True

        # refresh display
        pygame.display.update()

        # CLOCK
        clock.tick(ticks)

