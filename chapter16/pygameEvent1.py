"""
pygameEvent1.py
Chapter 16 Game Programming
Author: William C. Gunnells
Rapid Python Programming
"""

# lib
import pygame


white = (255,255,255) # RGB values
black = (0,0,0)
pygame.init()
display = pygame.display.set_mode((800,600))
x = 300
y = 300
while 1:
    for event in pygame.event.get():  # event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
    # not rendered yet without update
    display.fill(white)
    pygame.draw.rect(display, black, [x, y, 10, 10])
    pygame.display.update()  # update after graphics
pygame.quit()
quit() 
