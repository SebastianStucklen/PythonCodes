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
ballpos = Vector2(500,800)
itsGoverBroski = False

rows = list()

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
        #right
        if self.pos.x+self.radius >= 1178 and self.pos.y > 32+self.radius and self.pos.y < 868-self.radius:
            self.xVel= -self.xVel 

    #x: 32 1178
    #y: 32 868 

    def draw(self):
        pygame.draw.circle(screen, (255,255,255),self.pos,self.radius)

    def collision(self,isbroken,brickposx,brickposy,brickwidth,brickheight):
        if isbroken == False:
            if self.pos.y == brickposy or self.pos.y == brickposy+brickheight:
                print("yay")
                if self.pos.x > brickposx and self.pos.x < brickposx+brickwidth:
                    self.yVel = -self.yVel
                    return True
                elif self.pos.x+self.radius == brickposx or self.pos.x-self.radius == brickposx+brickwidth:
                    self.xVel = -self.xVel
                    return True
        


#brick ------------------------
class Brick:
    def __init__(self,xpos,ypos):
        self.pos = Vector2(xpos,ypos)
        self.colorpal = [(191, 28, 45),(217, 122, 54),(230, 198, 80),(91, 166, 16),(6, 115, 70),(16, 129, 166),(54, 149, 217),(115, 6, 70),(242, 133, 178)]
        self.colors = random.choice(self.colorpal)
        self.broken = False
        self.width = 120
        self.height = 40

    def getPosx(self):
        return self.pos.x
    def getPosy(self):
        return self.pos.y
    def getBroken(self):
        return self.broken
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height

    def draw(self):
        if self.broken == False:
            pygame.draw.rect(screen, self.colors, (self.pos.x,self.pos.y, self.width, self.height))
    
    def collision(self,collided):
        if collided == True:
            self.broken = True

#CREATE ==========================================
theBall = Ball(ballpos)

x = 90
for i in range(8):
    rows.append(Brick(x,60))
    x+=130

x = 90
for i in range(8):
    rows.append(Brick(x,110))
    x+=130

x = 90
for i in range(8):
    rows.append(Brick(x,160))
    x+=130

x = 90
for i in range(8):
    rows.append(Brick(x,210))
    x+=130


#game loop ========================================
while itsGoverBroski == False:
    #foundation ---------------
    time.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            itsGoverBroski = True


    #update -------------------
    theBall.update()
    for i in range(len(rows)):
        rows[i].collision(theBall.collision(rows[i].getPosx(), rows[i].getPosy(),  rows[i].getBroken(),  rows[i].getWidth(),  rows[i].getHeight()))

    #render -------------------
    screen.fill((0,0,0))
    
    theBall.draw()
    for i in range(len(rows)):
        rows[i].draw()


    pygame.draw.rect(screen,(175,165,165),(0,0,1210,900),30)
    pygame.draw.rect(screen,(255,255,255),(30,30,1150,840),2)
    pygame.display.flip()