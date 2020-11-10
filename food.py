import random

class Food:

    def __init__(self, snake):
        self.pos = self.set_pos(snake)

    def set_pos(self, snake):
        impossible_pos = snake.body
        find_pos = False
        while not find_pos:
            food_pos = (random.randint(0, 19), random.randint(0, 19))
            if not food_pos in impossible_pos:
                find_pos = True
        return food_pos

    def check_ate(self, snake):
        if snake.get_head() == self.pos:
            self.pos = self.set_pos(snake)  # new pos
            return True
        return False
    