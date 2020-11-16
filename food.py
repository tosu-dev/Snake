from constances import nb_cases
from random import randint

class Food:

    def __init__(self, snake):
        """
        init a food with is position compared to snake pos
        """
        self.pos = self.set_pos(snake)

    def set_pos(self, snake):
        """
        Choose a new position available for the fodd
        :param snake: Snake()
        :return: tuple
        """
        impossible_pos = snake.body
        find_pos = False
        while not find_pos:
            food_pos = (randint(0, nb_cases-1), randint(0, nb_cases-1))
            if not food_pos in impossible_pos:
                find_pos = True
        return food_pos

    def check_ate(self, snake):
        """
        Check if the foos has been ate by a snake
        :return: bool
        """
        if snake.get_head() == self.pos:
            self.pos = self.set_pos(snake)  # new pos
            return True
        return False
    