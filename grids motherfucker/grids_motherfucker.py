import pygame
pygame.init()
pygame.display.set_caption("GRIDS BITCH!!!!!")
screen = pygame.display.set_mode((500,500))

while(1):


	for i in range(6):
		for j in range(6):
			pygame.draw.rect(screen, (255,255,255),(i*80,j*80,80,80),1)



	pygame.display.flip()


pygame.quit()
