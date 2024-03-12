import pygame
import random
# Boilerplate code
pygame.init()
gamescreen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Particle Movement")
clock = pygame.time.Clock()
# Particle setup
xpos = 450 # X position of the particle
ypos = 450 # Y position of the particle
xVe1 = random.randint(-2, 2) # X velocity of the particle
yVe1 = random.randint(-2, 2) # Y velocity of the particle
# Game loop!
while True:
	clock.tick(60)
# Event handling------ —
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			break
# physics------------------------
# Update position
	xpos += xVe1
	ypos += yVe1
# Boundary checking
	if xpos < 0 or xpos > 900:
#check if hitting left or right wall
		xVe1 *= -1 #bounce!
	if ypos < 0 or ypos > 900:
#check if hitting top or bottom wall
		yVe1 *= -1 #bounce!
# Render section-------- — —
	gamescreen.fill((0, 0, 0))
	pygame.draw.circle(gamescreen, (255,255,255), (xpos, ypos), 5)
	pygame.display.flip( )
# End of game loop
pygame.quit()