#!/usr/bin/python

# This is my first pygame script
# @author Romack Natividad <romacknatividad@gmail.com>

import pygame
import random
from pygame.locals import *

def main():
	pygame.init()
	pygame.display.set_caption("Super Mario @ Python PH UG ~ pyMakulit")

	screen_width = 721
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))

	bg = pygame.image.load("images/pyconph.jpg")
	morefun = pygame.image.load("images/morefun-mini.jpg")

	orig_mario = pygame.image.load("images/Mario.gif")
	supermario = pygame.image.load("images/Super Mario.gif")
	fierymario = pygame.image.load("images/Fiery Mario.gif")
	github = pygame.image.load("images/github.jpg")
	mario = orig_mario
	icon_status = "mario"

	x,y,step_x,step_y = random.randint(0,screen_width-1),random.randint(0,screen_height-1),2,2
	gx,gy,step_gx,step_gy = random.randint(0,screen_width-1),random.randint(0,screen_height-1),2,2

	clock = pygame.time.Clock()

	running = True
	while running:
		# if mario is on edge, change direction
		if x > screen_width - 26 or x < 0:
			step_x = -step_x
		if y > screen_height - 32 or y < 0:
			step_y = -step_y
		if gx > screen_width - 16 or gx < 0:
                        step_gx = -step_gx
                if gy > screen_height - 16 or gy < 0:
                        step_gy = -step_gy

		x += step_x
		y += step_y
		gx += step_gx
		gy += step_gy

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			#elif event.type == pygame.MOUSEMOTION:
			#	print "Mouse @ (%d %d)" % event.pos
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				click_x = pos[0]
				click_y = pos[1]
				if click_x <= x + 26 and click_y <= y + 32:
					print "BOOM"
					if icon_status == "mario":
						mario = supermario
						icon_status = "supermario"
					elif icon_status == "supermario":
						mario = fierymario
						icon_status = "fierymario"
					else:
						mario = orig_mario
						icon_status = "mario"

		screen.fill((255,255,255)) # white BG
                screen.blit(bg, (0,0))
                screen.blit(morefun, (screen_width-407, screen_height-150))
                pygame.draw.line(screen, (0,0,0),(0,0),(screen_width, screen_height))
                screen.blit(mario, (x, y))
                screen.blit(github,(gx,gy))
                pygame.display.flip()

		clock.tick(100)
						

if __name__ == "__main__":
	main()
