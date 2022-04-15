import pygame
from sys import exit
from os import system
from random import randint
from time import sleep

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

# FONTS/TEXTS
score_font = pygame.font.SysFont(font, score_size)

lose_font = pygame.font.SysFont(font, lose_size)
lose_text = lose_font.render("GAME OVER", True, WHITE)

menu_font = pygame.font.SysFont(font, menu_size)


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

# WELCOME SCREEN
def welcome_screen():
    global GAME
    global welcome_menu_open

    welcome_menu_open = True

    screen.fill(BLACK)
    # play
    play_text = menu_font.render("PLAY", True, WHITE)
    play_pos = (screen_size//2-play_text.get_width()//2, screen_size//3-play_text.get_height()//2)

    # option
    option_text = menu_font.render("OPTION", True, WHITE)
    option_pos = (screen_size//2-option_text.get_width()//2, screen_size//2-option_text.get_height()//2)

    # quit
    quit_text = menu_font.render("QUIT", True, WHITE)
    quit_pos = (screen_size//2-quit_text.get_width()//2, screen_size//2-quit_text.get_height()//2+option_text.get_height()+option_text.get_height()//2)

    screen.blit(play_text, play_pos)
    screen.blit(option_text, option_pos)
    screen.blit(quit_text, quit_pos)
    pygame.display.update()

    # while the game didn't start
    while not GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                print("[WINDOW CLOSED]")


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # play
                    if play_text.get_rect().move(play_pos).collidepoint(event.pos):
                        screen.fill(BLACK)
                        GAME = True
                        sleep(0.3)
                        draw_food(food)

                    # option

                    # quit
                    if quit_text.get_rect().move(quit_pos).collidepoint(event.pos):
                        pygame.quit()
                        exit()
                        print("[WINDOW CLOSED]")


    welcome_menu_open = False


def pause_screen():
    global GAME
    global pause_menu_open
    global snake
    global food
    global board

    pause_menu_open = True

    GAME = False
    # continue
    continue_text = menu_font.render("CONTINUE", True, WHITE)
    continue_pos = (screen_size//2-continue_text.get_width()//2, screen_size//3-continue_text.get_height()//2)

    # retry
    retry_text = menu_font.render("RETRY", True, WHITE)
    retry_pos = (screen_size//2-retry_text.get_width()//2, screen_size//2-continue_text.get_height()//2)

    # quit
    quit_text = menu_font.render("QUIT", True, WHITE)
    quit_pos = (screen_size//2-quit_text.get_width()//2, screen_size//2-quit_text.get_height()//2+retry_text.get_height()+retry_text.get_height()//2)


    screen.blit(continue_text, continue_pos)
    screen.blit(retry_text, retry_pos)
    screen.blit(quit_text, quit_pos)
    pygame.display.update()

    while not GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # continue
                    if continue_text.get_rect().move(continue_pos).collidepoint(event.pos):
                        screen.fill(BLACK)
                        draw_food(food)
                        draw_snake(snake, snake.get_last_case())
                        sleep(0.3)
                        GAME = True
                        break

                    # retry
                    if retry_text.get_rect().move(retry_pos).collidepoint(event.pos):
                        # reset
                        snake.reset()
                        board.score = 0
                        screen.fill(BLACK)
                        food.pos = food.set_pos(snake)
                        draw_food(food)
                        GAME = True
                        sleep(0.3)

                    # quit
                    if quit_text.get_rect().move(quit_pos).collidepoint(event.pos):
                        # reset
                        snake.reset()
                        board.score = 0
                        welcome_screen()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        screen.fill(BLACK)
                        draw_food(food)
                        draw_snake(snake, snake.get_last_case())
                        sleep(0.3)
                        GAME = True
                        break

    pause_menu_open = False


welcome_screen()

# INIT  DRAW SNAKE
draw_snake(snake, (0, 0))
pygame.display.update()

# CLOCK
clock = pygame.time.Clock()

# GAME LOOP
while RUNNING:

    for event in pygame.event.get():

        # QUIT
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
            exit()
            print("[WINDOW CLOSED]")

                
        # IF GAME IS WORKING
        if GAME:

            # PAUSE GAME
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_screen()

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

        snake_ticks += 1

        if snake_ticks >= ticks//13:

            snake_ticks = 0

            # FOOD
            if food.check_ate(snake):
                # SCORE
                board.score += 1

                # FOOD
                draw_food(food)
                # SNAKE
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

                score_text = score_font.render(f"score : {board.score}", True, WHITE)

                screen.blit(lose_text, (screen_size/2-165, screen_size/2-40))
                screen.blit(score_text, (screen_size/2-60, screen_size/2+30))
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

