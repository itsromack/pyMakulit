#!/usr/bin/python

# This is my first pygame script
# @author Romack Natividad <romacknatividad@gmail.com>

import pygame
from pygame.locals import *

def main():
	pygame.init()
	pygame.display.set_caption("Super Mario @ Python PH UG ~ pyMakulit")

	screen_width = 721
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))

	bg = pygame.image.load("images/pyconph.jpg")
	morefun = pygame.image.load("images/morefun-mini.jpg")

	mario = pygame.image.load("images/Mario.gif")
	supermario = pygame.image.load("images/Super Mario.gif")

	x,y,xs,ys,step_x,step_y = 0,182,screen_width,0,2,2

	running = True
	while running:
		# if mario is on edge, change direction
		if x > screen_width - 26 or x < 0:
			step_x = -step_x
		if y > screen_height - 32 or y < 0:
			step_y = -step_y
		x += step_x
		y += step_y

		screen.fill((255,255,255)) # white BG

		screen.blit(bg, (0,0))
		screen.blit(morefun, (screen_width-407, screen_height-150))
		screen.blit(mario, (x, y))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == "__main__":
	main()
