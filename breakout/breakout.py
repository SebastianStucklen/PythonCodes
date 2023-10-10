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

rows = list()

time = pygame.time.Clock()
ticks = 0
score = 0
totalbricks = 32
#class =============================================

#paddle -----------------------
class Paddle:
    pass

#ball -------------------------
class Ball:
    def __init__(self,startpos):
        self.pos = Vector2(startpos)
        self.yVel = 6
        self.xVel = -4.5
        self.radius = 12
        self.gover = False

    def getPos(self):
        return self.pos

    def update(self):
        self.pos.x -= self.xVel
        self.pos.y -= self.yVel
        #right
        if self.pos.x+self.radius >= 1178 and self.pos.y > 32+self.radius and self.pos.y < 868-self.radius:
            self.xVel= -self.xVel 
        #top
        if self.pos.y-self.radius <= 32 and self.pos.x > 32+self.radius and self.pos.x < 1178-self.radius:
            self.yVel= -self.yVel
        #left
        if self.pos.x-self.radius <= 32 and self.pos.y > 32+self.radius and self.pos.y < 868-self.radius:
            self.xVel= -self.xVel 
        #bottom
        if self.pos.y+self.radius >= 868 and self.pos.x > 32+self.radius and self.pos.x < 1178-self.radius:
            self.yVel= -self.yVel
            #self.gover = True
        
        #corner
        if self.pos.x < 30 or self.pos.x > 1180 or self.pos.y < 30 or self.pos.y > 870:
            self.pos.x = 600
            self.pos.y = 800
            if self.yVel >0:
                self.yVel = -self.yVel
            pygame.time.wait(1200)

    #x: 32 1178
    #y: 32 868 

    def draw(self):
        pygame.draw.circle(screen, (255,255,255),self.pos,self.radius)

    def collision(self,isbroken,brickposx,brickposy,brickwidth,brickheight):
        if isbroken == False:
            if self.pos.y+self.radius >= brickposy and self.pos.y-self.radius <= brickposy+brickheight:
                if self.pos.x > brickposx and self.pos.x < brickposx+brickwidth:
                    self.yVel = -self.yVel
                    return True
            if self.pos.y > brickposy and self.pos.y < brickposy+brickheight:
                if self.pos.x+self.radius >= brickposx and self.pos.x-self.radius <= brickposx+brickwidth:
                    self.xVel = -self.xVel
                    return True
    
    def paddleCollision(self,padPosX,padPosY,padW):
        if self.pos.y+self.radius >= padPosY:
            if self.pos.x+self.radius >= padPosX and self.pos.x-self.radius <= padPosX:
                self.yVel = -self.yVel


    def end(self,run):
        if self.gover == True:
            screen.fill((0,0,0))
        if self.gover == True or run == True:
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text1 = my_font.render(str("GOVER"),1,(255,255,255))
            screen.blit(text1,(600,450))
            self.xVel = 0
            self.yVel = 0


#brick ------------------------
class Brick:
    def __init__(self,xpos,ypos):
        self.pos = Vector2(xpos,ypos)
        self.colorpal = [(191, 28, 45),(217, 122, 54),(230, 198, 80),(91, 166, 16),(6, 115, 70),(16, 129, 166),(54, 149, 217),(115, 6, 70),(242, 133, 178)]
        self.colors = random.choice(self.colorpal)
        self.broken = False
        self.width = 120
        self.height = 40
        self.animTimer = 0
        #IMAGES
        self.brickimg = pygame.image.load("breakout/brick.png")
        self.crack = pygame.image.load("breakout/crack.png")
        self.plode1 = pygame.image.load("breakout/plode1.png")
        self.plode2 = pygame.image.load("breakout/plode2.png")
        self.plode3 = pygame.image.load("breakout/plode3.png")

        

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
            screen.blit(self.brickimg,self.pos)
        if self.broken == True:
            if self.animTimer<=111:
                self.animTimer += 1
            if self.animTimer <= 30:
                pygame.draw.rect(screen, self.colors, (self.pos.x,self.pos.y, self.width, self.height))
                screen.blit(self.crack,self.pos)
            elif self.animTimer <= 36:
                screen.blit(self.plode1,self.pos)
            elif self.animTimer <= 70:
                screen.blit(self.plode2,self.pos)
            elif self.animTimer <= 110:
                screen.blit(self.plode3,self.pos)


    
    def collision(self):
        self.broken = True

#CREATE ==========================================
theBall = Ball(ballpos)

x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,60))
    x+=130

x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,110))
    x+=130

x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,160))
    x+=130

x = 90
for i in range(totalbricks//4):
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
        if theBall.collision(rows[i].getBroken(), rows[i].getPosx(), rows[i].getPosy(),  rows[i].getWidth(),  rows[i].getHeight()) == True:
            rows[i].collision()
            score+=1

    #render -------------------
    screen.fill((0,0,0))
    
    theBall.draw()
    for i in range(len(rows)):
        rows[i].draw()


    pygame.draw.rect(screen,(175,165,165),(0,0,1210,900),30)
    pygame.draw.rect(screen,(255,255,255),(30,30,1150,840),2)
    if score == totalbricks:
        theBall.end(True)
    theBall.end(False)
    pygame.display.flip()