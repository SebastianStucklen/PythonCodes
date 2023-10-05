#import ============================================
import random
import pygame
import time
from pygame.math import Vector2

#pygame ============================================
pygame.init()
pygame.display.set_caption("SUPER BREAKOUT ESCAPE WAHOOO YIPEEE")
screen = pygame.display.set_mode((1210,900))

#variables =========================================
ballpos = Vector2(600,800)
itsGoverBroski = False

row1 = list()
row2 = list()
row3 = list()
row4 = list()

time = pygame.time.Clock()
ticks = 0

#class =============================================

#paddle -----------------------
class Paddle:
    pass

#ball -------------------------
class Ball:
    def __init__(self,startpos):
        self.pos = Vector2(startpos)
        self.yVel = 5
        self.xVel = -5
        self.radius = 10

    def getPos(self):
        return self.pos

    def update(self):
        self.pos.x -= self.xVel
        self.pos.y -= self.yVel

    def collision(self,brickpos,isbroken):
        if self.pos:
            pass 
            #FIX THIS ____!@_IUBKIYdbiauewdbdliUAWBdliuwhianwclkjhndvluhnvlfshnfuewniueneiouwnhiunfoiuwehnfiuwhnevfuwhnefnwiuvfnwev


#brick ------------------------
class Brick:
    def __init__(self,xpos,ypos):
        self.pos = Vector2(xpos,ypos)
        self.colorpal = [(191, 28, 45),(217, 122, 54),(230, 198, 80),(91, 166, 16),(6, 115, 70),(16, 129, 166),(54, 149, 217),(115, 6, 70),(242, 133, 178)]
        self.colors = random.choice(self.colorpal)
        self.broken = False
        self.width = 120
        self.height = 40

    def getPos(self):
        if self.broken == False:
            return self.pos and self.broken and self.width and self.height
    
    def draw(self):
        if self.broken == False:
            pygame.draw.rect(screen, self.colors, (self.pos.x,self.pos.y, self.width, self.height))
    
    def collision(self):
        pass

x = 90
for i in range(8):
    row1.append(Brick(x,60))
    x+=130

x = 90
for i in range(8):
    row2.append(Brick(x,110))
    x+=130

x = 90
for i in range(8):
    row3.append(Brick(x,160))
    x+=130

x = 90
for i in range(8):
    row4.append(Brick(x,210))
    x+=130


#game loop ========================================
while itsGoverBroski == False:
    #foundation ---------------
    time.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            itsGoverBroski = True


    #update -------------------


    #render -------------------
    for i in range(len(row1)):
        row1[i].draw()
    for i in range(len(row2)):
        row2[i].draw()
    for i in range(len(row3)):
        row3[i].draw()
    for i in range(len(row4)):
        row4[i].draw()
    
    pygame.draw.rect(screen,(175,165,165),(0,0,1210,900),30)
    pygame.draw.rect(screen,(255,255,255),(30,30,1150,840),2)
    pygame.display.flip()