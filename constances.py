# COLOR
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
light_green = (0, 150, 0)
red = (255, 0, 0)

# WINDOW
screen_size = 600
screen_title = 'Snake Game'

# BOARD, CASES
nb_cases = 20 # number of cases in a line (also in a column)
case_width = int(screen_size / nb_cases)  # width (also height) of a board case
line_width = 1
cases_rect = ()  # top-left corner

# CLOCK
ticks = 12  # number of ticks per second

# GAME
RUNNING = True
GAME = True