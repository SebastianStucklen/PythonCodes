import pygame
import math
pygame.init()
pygame.display.set_caption("graphical for loops")
screen = pygame.display.set_mode((800,800))


gameover = False
angle = 0

while not gameover:

	angle += 1 #increment angle
	if angle > 360:
		angle = 0

	radians = angle/180*3.14 #convert from degrees to radians
	
	xpos = math.cos(radians) *400
	ypos = math.sin(radians) *400

	pygame.draw.circle(screen, (250, 250, 0), (xpos, ypos), 2)
	
	pygame.display.flip()

pygame.quit()
