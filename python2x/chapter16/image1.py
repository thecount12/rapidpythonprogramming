#!/usr/bin/python
# image1.py
# Chapter 16 Game Programming 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import pygame
import random


white=(255,255,255) # RGB values 
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,0)
blue=(0,0,255)
pygame.init() 
display=pygame.display.set_mode((800,600)) 
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,25)
bg=pygame.image.load("gimpbackground.png")


star=pygame.image.load('assortstar1.png') 

def message(msg,color,posx,posy): 
	mytext=font.render(msg,True,color)
	display.blit(mytext,[posx,posy])

def game(): 
	exit=False
	x=300; y=300 
	xChange=0; yChange=0
	boxX=round(random.randrange(0,800-10) /10.0) *10.0 
	boxY=round(random.randrange(0,600-10) /10.0) *10.0 
	while not exit: # exit loop 
		for event in pygame.event.get(): # event handling 
			if event.type==pygame.QUIT:
				exit=True
			k=pygame.key.get_pressed()
			if k[pygame.K_LEFT]:
				xChange-=10
			elif k[pygame.K_RIGHT]:
				xChange+=10	
			elif k[pygame.K_UP]:
				yChange-=10
			elif k[pygame.K_DOWN]:
				yChange+=10
			else:
				xChange=0
				yChange=0
		
		if x==700: # borders 
			xChange=-10 
			yChange=0
		if x==10:
			xChange=10 
			yChange=0	
		if y==500: 
			yChange=-10
			xChange=0 
		if y==10:
			exit=True 

		x += xChange # continue from previous location 
		y += yChange

		#display.fill(black) # not rendered without update 
		display.blit(bg,(0,0))
		message("Move square in any direction...", yellow, 300,50)
#		pygame.draw.rect(display,white,[x,y,20,20]) # coords, w,h 
		pygame.draw.rect(display,yellow,[boxX,boxY,20,20]) 
		display.blit(star,[x,y])
		pygame.display.update()
		clock.tick(10) 
	pygame.quit()
	quit()

game()

