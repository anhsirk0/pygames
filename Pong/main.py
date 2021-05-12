import pygame
import sys

# initialize pygame
pygame.init()

# load images
ball = pygame.image.load('assets/ball.png')
bar = pygame.image.load('assets/bar.png')

# pygame screen
HEIGHT, WIDTH = 720, 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# initial positions and speeds 
# ball
x, y = 0, 50
xspeed, yspeed = 0.55, 0.55
# bar
bx,  by = WIDTH - 20, 300
bspeed = 0

# pygame window
run = True
while run:
    for event in pygame.event.get():
        # game event handling
        if event.type == pygame.QUIT:
            sys.exit()
            run = False
        # keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bspeed = 0.9
            if event.key == pygame.K_UP:
                bspeed = -0.9
        else:
            bspeed = 0

    # game logic
    if x >= WIDTH - 50:
        x = 0
    if x<0:
        xspeed = -xspeed
    if y >= HEIGHT - 50 or y < 0:
        yspeed = -yspeed
    if x >= WIDTH -70 and y >= by and y <= by + 150:
        xspeed = -xspeed

    screen.fill([11, 21, 21])
    screen.blit(ball, [x, y])
    screen.blit(bar, [bx, by])

    x += xspeed
    y += yspeed
    by += bspeed

    pygame.display.update()
