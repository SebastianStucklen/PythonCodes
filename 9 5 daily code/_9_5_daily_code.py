import pygame
import time
pygame.init()
pygame.display.set_caption("graphical for loops")
screen = pygame.display.set_mode((800,800))
xpos = 0
ypos = 0
linex1 = 200
liney1 = 194
linex2 = 194
liney2 = 800
linex3 = 194
linex4 = 800
liney3 = 194
liney4 = 200
mousePos = (xpos, ypos)
ramp=1
ran=False
ran2=False
linex5 = 600
linex6 = 600
while(1):
	pygame.draw.circle(screen,(255,255,255),(400,400),(200),1)
	pygame.draw.circle(screen,(0,0,0),(400,400),(800),600)
	pygame.display.flip()
	#event = pygame.event.wait()
	#if event.type == pygame.MOUSEMOTION: #check if mouse moved
	#	mousePos = event.pos #refreshes mouse position
	#	print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
	if ran == False:
		for i in range(34):
			pygame.draw.line(screen, (148,113,169),(linex2,liney1),(linex1,liney2))
			linex1+=ramp
			pygame.draw.line(screen, (148,113,169),(linex3,liney4),(linex4,liney3))
			liney3+=ramp
			ramp+=1
			pygame.draw.circle(screen,(255,255,255),(400,400),(200),1)
			pygame.draw.circle(screen,(0,0,0),(400,400),(800),600)
			pygame.display.flip()
			time.sleep(0.1)
	ran = True
	if ran2 == False:
		for i in range(11):
			pygame.draw.line(screen, (255,0,50),(150,150),(linex5,600))
			pygame.draw.line(screen, (255,0,50),(150,150),(linex6,600))
			linex5+=1
			linex6-=1
			pygame.draw.circle(screen,(255,255,255),(400,400),(200),1)
			pygame.draw.circle(screen,(0,0,0),(400,400),(800),600)
			pygame.display.flip()
	ran2 = True
	#if linex1>200:
	#	linex1+=3
	#else:
	#	linex1-=3
	#if liney1<600:
	#	liney1-=3
	#else:
	#	liney1+=3
	#if linex2>200:
	#	linex2-=3
	#else:
	#	linex2+=3
	#if liney2<200:
	#	liney2+=3
	#else:
	#	liney2-=3
	#		




pygame.quit()
