from constances import nb_cases

class Board:

    def __init__(self, nb_cases, snake, food):
        """
        init a board (bidimensional list) that contains a snake and a food
        """
        self.board = [[' ' for _ in range(nb_cases)] for _ in range(nb_cases)]
        self.board[snake.start[0]][snake.start[1]] = 'H'
        self.board[food.pos[0]][food.pos[1]] = 'F'

        self.score = 0

    def update(self, snake, last_case, food):
        """
        update the board with new pos of snake and food
        :param snake: Snake()
        :param last_case: 'old' last case of the snake
        :param food: Food()
        """
        # SNAKE
        # check if he touch a wall or himself
        if snake.check_collides():
            raise IndexError()

        # update the board
        self.board[last_case[0]][last_case[1]] = ' '
        for i, coord in enumerate(snake.body):
            if i == 0:
                self.board[coord[0]][coord[1]] = 'H'
            else:
                self.board[coord[0]][coord[1]] = 'S'

        # FOOD
        self.board[food.pos[0]][food.pos[1]] = 'F'

    def __len__(self):
        """
        Get the len of the board
        :return: int
        """
        return nb_cases

    def __repr__(self):
        msg = ""
        for elt in self.board:
            msg += str(elt) + '\n'
        return msg

if __name__ == '__main__':
    pass