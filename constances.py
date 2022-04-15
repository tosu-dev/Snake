# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (0, 255, 0)
green = (0, 200, 0)
red = (255, 0, 0)

# WINDOW
screen_size = 600
screen_title = 'Snake Game'

# BOARD, CASES
nb_cases = 20 # number of cases in a line (also in a column)
case_width = int(screen_size / nb_cases)  # width (also height) of a board case
line_width = 1

# FONTS
font = 'Arial'
# MENU
menu_size = 56
# SCORE
score_size = 32
# LOSE
lose_size = 56

# MENU OPEN
welcome_menu_open = True
pause_menu_open = False

# CLOCK
ticks = 120  # number of ticks per second (//15 for the snake movement)
snake_ticks = 0 # 15 ticks = one move

# GAME
RUNNING = True  # is window is running
GAME = False  # is game is running
