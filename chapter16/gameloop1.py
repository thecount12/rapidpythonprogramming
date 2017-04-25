#!/usr/bin/python
# gameloop1.py
# Chapter 16 Game Programming 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import pygame


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

def splash():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro=False
				if event.key==pygame.K_q:
					pygame.quit()
					quit()
		display.fill(white)
		message("Wellcome!!!", black,300,300 )
		message("Press 'c' to continue or 'q' to Quit",black,300,400)
		pygame.display.update()
		clock.tick(15) 

def message(msg,color,posx,posy): 
	mytext=font.render(msg,True,color)
	display.blit(mytext,[posx,posy])

def game(): 
	exit=False
	over=False
	x=300; y=300 
	xChange=0; yChange=0
	while not exit: # exit loop 
		while over == True: # over loop
			display.fill(blue)
			message("Game over 'c' to continue 'q' to quit", yellow, 300,300)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					over=False
					exit=True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						exit = True
						over = False
					if event.key == pygame.K_c:
						game()
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
			over=True 

		x += xChange # continue from previous location 
		y += yChange

		display.fill(black) # not rendered without update 
		message("Move square in any direction...", yellow, 300,50)
		message("Too far up exits loop...", yellow, 300,70)
		pygame.draw.rect(display,white,[x,y,20,20]) # coords, w,h 
		pygame.display.update()
		clock.tick(10) 
	pygame.quit()
	quit()

splash()
game()

