class Board:

    def __init__(self, nb_cases, snake, food):
        """
        init a board that contains a snake and a food
        """
        self.board = [[' ' for _ in range(nb_cases)] for _ in range(nb_cases)]
        self.board[snake.start[0]][snake.start[1]] = 'H'
        self.board[food.pos[0]][food.pos[1]] = 'F'

    def update(self, snake, last_case, food):

        # SNAKE
        if snake.check_collides():
            raise IndexError("WALL")

        self.board[last_case[0]][last_case[1]] = ' '
        for i, coord in enumerate(snake.body):
            if i == 0:
                self.board[coord[0]][coord[1]] = 'H'
            else:
                self.board[coord[0]][coord[1]] = 'S'

        # FOOD
        self.board[food.pos[0]][food.pos[1]] = 'F'

    def __len__(self):
        return nb_cases

    def __repr__(self):
        msg = ""
        for elt in self.board:
            msg += str(elt) + '\n'
        return msg

if __name__ == '__main__':
    from constances import *
    import snake
    import food

    snake = snake.Snake()
    food = food.Food(snake)
    board = Board(nb_cases, snake, food)
    
    print(board)