import pygame
import random
from pygame.locals import *
from pygame.time import Clock

pygame.init()


def random_nums():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 * 10, y//10 * 10)

def collision(c1,c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')


snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))  

apple_pos = random_nums()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

myDirection = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
             pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and myDirection != DOWN:
                myDirection = UP
            if event.key == K_DOWN and myDirection != UP:
                myDirection = DOWN 
            if event.key == K_RIGHT and myDirection != LEFT:
                myDirection = RIGHT
            if event.key == K_LEFT and myDirection != RIGHT:
                myDirection = LEFT

    for i in range(len(snake) -1, 1, -1):
        if snake[0] == snake[i]:
            pygame.quit()
        
        

    if collision(snake[0], apple_pos):
        apple_pos = random_nums()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    
    
    if myDirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if myDirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if myDirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if myDirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()