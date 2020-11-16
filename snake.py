from constances import nb_cases

class Snake:
    
    def __init__(self):
        """
        init a snake
        """
        self.lenght = 1
        self.direction = 'd'  # u, d, r, l
        self.start = (0, nb_cases // 2)
        self.body = [self.start]  # first is head
        self.can_turn = True

    def get_head(self):
        """
        Get head postion of the snake
        :return: tuple
        """
        return self.body[0]

    def get_last_case(self):
        """
        Get the last cas of the snake (tail)
        :return: tuple
        """
        return self.body[-1]

    def check_collides(self):
        """
        check if he touch a wall or himself
        :return: bool
        """
        head = self.get_head()
        if head[0] < 0 or head[1] < 0:
            return True
        for i, coord in enumerate(self.body):
            if i != 0:
                if head == coord:
                    return True
        return False

    def add_case(self):
        """
        add a case for the snake when he eat a food
        :return: None   
        """
        self.lenght += 1
        self.body.append(self.body[-1])

    def move(self):
        """
        Move the snake in his direction and return the old last case
        :return: the old last case (tuple)
        """
        last_case = self.get_last_case()

        # move the head
        head = self.body[0]  # register the old head pos
        if self.direction == 'r':
            self.body[0] = (self.body[0][0], self.body[0][1]+1)
        elif self.direction == 'l':
            self.body[0] = (self.body[0][0], self.body[0][1]-1)
        elif self.direction == 'u':
            self.body[0] = (self.body[0][0]-1, self.body[0][1])
        elif self.direction == 'd':
            self.body[0] = (self.body[0][0]+1, self.body[0][1])
        
        # body follow
        if len(self.body) > 1:
            for i in range(len(self.body)-1, 1, -1):
                self.body[i] = self.body[i-1]
            self.body[1] = head # put the old head pos at the next body case

        return last_case

if __name__ == '__main__':
    pass
