import pygame, time
import numpy as np
import json

#initialize pygame
pygame.init()

#create screen
WIDTH, HEIGHT = 720, 720
SIZE = 15 # should be 18 for gospel 
screen = pygame.display.set_mode((WIDTH + 1, HEIGHT + 1))

BLACK = [39, 39, 39]
AQUA = [104, 157, 106]
GREEN=(0, 255, 0)
pygame.display.set_caption('Life')

screen.fill(BLACK)

def pixel(x, y):
    pygame.draw.rect(screen, GREEN, (x * SIZE, y * SIZE, SIZE, SIZE))

w = int(WIDTH/SIZE)
h = int(HEIGHT/SIZE)
grid = np.zeros((w, h)) # 100 cells

def check(x, y, grid):
    alive = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= x + i < w and 0 <= y + j < h and [i, j] != [0, 0]:
                if grid[x + i, y + j] == 1:
                    alive += 1

    if grid[x, y] and alive < 2:
        return 0
    elif grid[x, y] and alive > 3:
        return 0
    elif not grid[x, y] and alive == 3:
        return 1
    else:
        return grid[x, y]

def update(grid):
    screen.fill(BLACK)
    new = grid.copy()
    for a in range(w):
        for b in range(h):
            grid[a, b] = check(a, b, new)
            if grid[a, b]:
                pixel(a, b)

def draw_lines():
    for i in range(w + 1):
        pygame.draw.line(screen, (AQUA), (i * SIZE, 0), (i * SIZE, HEIGHT))
    for j in range(h + 1):
        pygame.draw.line(screen, (AQUA), (0, j * SIZE), (WIDTH, j * SIZE))

draw_lines()

def gospel(grid):
    file = "gospel.json"
    lst = json.loads(open(file).read())
    for row in lst:
        x = int(row[0])
        y = int(row[1])
        grid[x, y] = 1

gospel(grid)

def draw_grid(grid):
    for i in range(w):
        for j in range(h):
            if grid[i, j]:
                pixel(i, j)

draw_grid(grid)
pause = True
# pygame window
run = True
# run = False
coords = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx = event.pos[0]
            my = event.pos[1]
            grid[mx // SIZE, my // SIZE] = 1
            pixel(mx // SIZE, my // SIZE)
            coords.append([mx // SIZE, my // SIZE])
            # print(grid)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pause = not pause

    if not pause:
        update(grid)
        draw_lines()
        time.sleep(0.01)
    pygame.display.update()
