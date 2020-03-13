"""
pygameEvent3.py
Chapter 16 Game Programming
Author: William C. Gunnells
Rapid Python Programming
"""

# lib
import pygame


white = (255, 255, 255)
black = (0, 0, 0)
pygame.init()
display = pygame.display.set_mode((800,600))
x = 300
y = 300
xChange = 0
yChange = 0
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = - 10
                yChange = 0
            elif event.key == pygame.K_RIGHT:
                xChange = 10
                yChange = 0
            elif event.key == pygame.K_UP:
                yChange = - 10
                xChange = 0
            elif event.key == pygame.K_DOWN:
                yChange = 10
                xChange = 0

    # if x >= 800 or x <= 0 or y >= 600 or y <= 0:
    # 	break

    if x == 700:
        xChange = -10
        yChange = 0
    elif x == 10:
        xChange = 0
        yChange = 0

    x += xChange
    y += yChange

    display.fill(white)
    pygame.draw.rect(display, black, [x, y, 10, 10])
    pygame.display.update()
    clock.tick(10)
pygame.quit()
quit() 
