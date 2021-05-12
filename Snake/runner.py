import pygame
import sys
import time
from game import SnakeGame
from snake import Direction

HEIGHT = 500
WIDTH = 500

BLACK = (39, 39, 39)
GREY = (100, 100, 100)
WHITE = (235, 219, 178)
AQUA = (104, 157, 106)
BLUE = (131, 165, 152)
RED = (251, 73, 52)

BLOCK_SIZE = 20

game = SnakeGame(block_size=BLOCK_SIZE, width=WIDTH, height=HEIGHT)
size = (WIDTH, HEIGHT)

pygame.init()

def draw_snake(snake, food):
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    j = 0
    i = [0, 0, 0]
    for block in snake.body.blocks:
        rect = (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
        color = [(104 + i[0]) % 255, (157 + i[1]) % 255, (106 + i[2]) % 255]
        pygame.draw.rect(screen, color, rect)
        j = (j + 1) % 3
        i[j] += 9

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

snake = game.snake
run = True
while run:

    # Check if game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if Direction.opposite(snake.direction) != Direction.DOWN:
                    snake.direction = Direction.DOWN
            elif event.key == pygame.K_UP:
                if Direction.opposite(snake.direction) != Direction.UP:
                    snake.direction = Direction.UP
            elif event.key == pygame.K_LEFT:
                if Direction.opposite(snake.direction) != Direction.LEFT:
                    snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                if Direction.opposite(snake.direction) != Direction.RIGHT:
                    snake.direction = Direction.RIGHT
            game.move_forward()
            time.sleep(0.15)
            draw_snake(snake, game.food)
        pygame.display.update()

    screen.fill(BLACK)
    if snake.is_alive:
        game.move_forward()
        time.sleep(0.15)
        draw_snake(snake, game.food)
    else:
        print(game.score)
        print(game.snake.body.length)
        sys.exit()
    pygame.display.update()
