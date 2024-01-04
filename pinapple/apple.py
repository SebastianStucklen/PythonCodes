import pygame
pygame.init
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("py napple")
mousePos = (400,400)
while True:
	event = pygame.event.wait()
	if event.type == pygame.MOUSEMOTION:
		mousePos = event.pos
	print(mousePos)

	pygame.draw.ellipse(screen, (250,250,80), (400, 200, 200, 300))
	
	for i in range(-50,50,20):
		pygame.draw.line(screen,(0,0,0),(i,0),(i+100,100),4)
	
	for i in range(-100,200,10):
		pygame.draw.line(screen, (0,0,0), (0, i+100), (100, i), 4)

	pygame.draw.polygon(screen, (0, 100, 200), ((400,650), (200,50), (800,250)))

	pygame.display.flip()
	