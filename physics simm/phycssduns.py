import pygame
from pygame.math import Vector2
from pygame.rect import Rect
import math
from enum import Enum

# config:
FRAMERATE = 240
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")




def main():
	# game setup:
	clock = pygame.time.Clock()
	# definitions:
	b1_counter = 0
	b1_xpos = 100
	b1_ypos = 700
	b1_xvel = 0
	b1_mass = 1

	b1_rect = Rect(b1_xpos,b1_ypos,100,100)
	

	b2_xpos = 300
	b2_ypos = 600
	b2_xvel = -5
	b2_mass = 100

	b2_rect = Rect(b2_xpos,b2_ypos,200,200)

	# main loop:
	running = True
	while running:
		delta = clock.tick(FRAMERATE) / 1000

		# input:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if b1_rect.colliderect(b2_rect):
			b1_counter+=0.6
			#if b1_xvel > 0:
			#	b1_xvel = 0
			if b2_xvel < 0:
				#b1_xvel -= abs(b2_xvel*1.1)
				new_vel = b1_mass*b1_xvel + b2_mass*b2_xvel
				b1_xvel = (-abs(new_vel/(b1_mass+b2_mass)))-1
			if b2_xvel > 0:
				#b1_xvel -= abs(b2_xvel*0.9)
				new_vel = b1_mass*b1_xvel + b2_mass*b2_xvel
				b1_xvel = (-abs(new_vel/(b1_mass+b2_mass)))-1
			
			b2_xvel += 1#(b2_mass*b2_xvel + b1_mass*b1_xvel)

		if b1_rect.left <= 0: #left wall collision
			b1_xvel = abs(b1_xvel)
			b1_counter+=1

		elif b1_rect.right >= SCREEN_SIZE.x:
			b1_xvel = -abs(b1_xvel)
			b1_counter+=1

		if b2_rect.left <= 0: #left wall collision
			b2_xvel = abs(b2_xvel)

		elif b2_rect.right >= SCREEN_SIZE.x:
			b2_xvel = -abs(b2_xvel)

			

		b1_rect.x += int(b1_xvel)
		b2_rect.x += int(b2_xvel)

		#if b2_rect.x < b1_rect.right-5:
		#	b2_rect.x = b1_rect.right+1

		print(int(b1_counter))
		# draw:
		screen.fill("#000000")
		pygame.draw.rect(screen, (255, 0, 150), (b1_rect.x,b1_rect.top, 100, 100))

		pygame.draw.rect(screen, (255, 255, 255), (b2_rect.x,b2_rect.top, 200, 200))

		pygame.display.flip()

if __name__ == "__main__":
	main()