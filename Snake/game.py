import random
from snake import *

class SnakeGame:
    """
    Snake game
    """

    def __init__(self, block_size=20, width=500, height=500):
        self.block_size = block_size
        self.snake = Snake(self.block_size)
        self.food = (5 * self.block_size, 5 * self.block_size)
        self.width = width
        self.height = height
        self.over = False
        self.score = 0

    def random_position(self):
        return random.randint(0, self.width // self.block_size - 1)

    def add_food(self):
        """
        Add food at possible random position
        """
        food_x = self.random_position()
        food_y = self.random_position()
        food = (food_x * self.block_size, food_y * self.block_size)
        while self.snake.overlap(food):
            food_x = self.random_position()
            food_y = self.random_position()
            food = (food_x * self.block_size, food_y * self.block_size)
        self.food = food

    def move_forward(self):
        self.snake.grow()
        if self.snake.overlap(self.food):
            self.score += 10
            print(self.snake.body.length)
            self.add_food()
        else:
            self.snake.body.remove_tail()

        if (
            self.snake.head.x < 0 or self.snake.head.x >=self.width or
            self.snake.head.y < 0 or self.snake.head.y >=self.height
        ):
            self.snake.is_alive = False
            self.snake.dying_reason = "Touched the walls"

    @classmethod
    def available_actions(cls, direction):
        """
        All valid actions for snake given state
        """
        actions = []
        for dir in Direction.all():
            if Direction.opposite(dir) != direction:
                actions.append(dir)
        return actions

