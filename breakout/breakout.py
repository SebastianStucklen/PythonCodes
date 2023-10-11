#import ============================================
import random
import pygame
import time
from pygame.math import Vector2
from winsound import Beep

#pygame ============================================
pygame.init()
pygame.display.set_caption("SUPER BREAKOUT ESCAPE WAHOOO YIPEEE")
screen = pygame.display.set_mode((1210,900))

#variables =========================================
x = random.randint(400,800)
ballpos = Vector2(x,700)
radius = 12

padpos = Vector2(500,800)
padwidth = 160
padheight = 18

itsGoverBroski = False

rows = list()

time = pygame.time.Clock()
ticks = 0
score = 0
totalbricks = 32

brickwidth = 120
brickheight = 40
#class =============================================

#paddle -----------------------
class Paddle:
    def __init__(self,startpos,width,height):
        self.pos = Vector2(startpos)
        self.width = width
        self.height = height
        self.xVel = 0
        self.vel = 9
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.pos.x > 32+self.vel:
                self.xVel = self.vel
            else:
                self.xVel = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.pos.x+self.width < 1178-self.vel:
                self.xVel = -self.vel
            else:
                self.xVel = 0
        if keys[pygame.K_RIGHT] == False and keys[pygame.K_LEFT] == False and keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            self.xVel = 0
        
    def update(self):
        self.pos.x -= self.xVel
    
    def getPosX(self):
        return self.pos.x
    def getPosY(self):
        return self.pos.y
    def getVel(self):
        return self.xVel

    def draw(self):
        pygame.draw.rect(screen, (255,255,255),(self.pos.x,self.pos.y,self.width,self.height))

#ball -------------------------
class Ball:
    def __init__(self,startpos,radius):
        self.pos = Vector2(startpos)
        self.choices = [-1.5,1.5]
        self.choice = random.choice(self.choices)
        self.yVel = 7
        self.xVel = self.choice
        self.radius = radius
        self.gover = False

    def getPos(self):
        return self.pos

    def update(self):
        self.pos.x -= self.xVel
        self.pos.y -= self.yVel
        #right
        if self.pos.x+self.radius >= 1178 and self.pos.y > 32+self.radius and self.pos.y < 868-self.radius:
            self.xVel= -self.xVel
            Beep(400,20)

        #top
        if self.pos.y-self.radius <= 32 and self.pos.x >= 30+self.radius and self.pos.x <= 1180-self.radius:
            self.yVel*=1.01
            self.yVel= -self.yVel
            Beep(400,20)
        #left
        if self.pos.x-self.radius <= 32 and self.pos.y > 32+self.radius and self.pos.y < 868-self.radius:
            self.xVel= -self.xVel 
            Beep(400,20)


        #bottom
        if self.pos.y+self.radius >= 868 and self.pos.x > 32+self.radius and self.pos.x < 1178-self.radius:
            self.yVel= -self.yVel
            self.gover = True
        
        #corner
        #if self.pos.x < 30 or self.pos.x > 1180 or self.pos.y < 30 or self.pos.y > 870:
        #    self.pos.x = 600
        #    self.pos.y = 800
        #    if self.yVel < 0:
        #        self.yVel = -self.yVel
        #    my_font = pygame.font.SysFont('Comic Sans MS', 30)
        #    text1 = my_font.render(str("oops. fixing"),1,(255,255,255))
        #    screen.blit(text1,(600,450))
        #    pygame.display.flip()
        #    pygame.time.wait(1200)

    #x: 32 1178
    #y: 32 868 

    def draw(self):
        pygame.draw.circle(screen, (255,255,255),self.pos,self.radius)

    def collision(self,isbroken,brickposx,brickposy,brickwidth,brickheight):
        if isbroken < 2:
            if self.pos.y+self.radius >= brickposy and self.pos.y-self.radius <= brickposy+brickheight:
                if self.pos.x > brickposx and self.pos.x < brickposx+brickwidth:
                    self.yVel*=1.02
                    self.yVel = -self.yVel
                    Beep(500,26)
                    return True
            if self.pos.y > brickposy and self.pos.y < brickposy+brickheight:
                if self.pos.x+self.radius >= brickposx and self.pos.x-self.radius <= brickposx+brickwidth:
                    self.xVel = -self.xVel
                    Beep(500,26)
                    return True
    
    def paddleCollision(self,padPosX,padPosY,padW,padV):
        if self.pos.y+self.radius >= padPosY:
            if self.pos.x+self.radius >= padPosX and self.pos.x-self.radius <= padPosX+padW:
                self.yVel = -self.yVel
                Beep(300,20)
                self.xVel*=1.04

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
    def __init__(self,xpos,ypos,width,height):
        self.pos = Vector2(xpos,ypos)
        self.colorpal = [(191, 28, 45),(217, 122, 54),(230, 198, 80),(91, 166, 16),(6, 115, 70),(16, 129, 166),(54, 149, 217),(115, 6, 70),(242, 133, 178)]
        self.colors = random.choice(self.colorpal)
        self.broken = 0
        self.width = width
        self.height = height
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
        if self.broken == 0:
            pygame.draw.rect(screen, self.colors, (self.pos.x,self.pos.y, self.width, self.height))
            screen.blit(self.brickimg,self.pos)
        if self.broken == 1:
            pygame.draw.rect(screen, self.colors, (self.pos.x,self.pos.y, self.width, self.height))
            screen.blit(self.crack,self.pos)
        if self.broken == 2:
            if self.animTimer<=81:
                self.animTimer += 1
            if self.animTimer <= 6:
                screen.blit(self.plode1,self.pos)
            elif self.animTimer <= 40:
                screen.blit(self.plode2,self.pos)
            elif self.animTimer <= 80:
                screen.blit(self.plode3,self.pos)


    
    def collision(self):
        self.broken += 1

#CREATE ==========================================
theBall = Ball(ballpos,radius)

thePaddle = Paddle(padpos,padwidth,padheight)
x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,70,brickwidth,brickheight))
    x+=130

x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,120,brickwidth,brickheight))
    x+=130

x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,170,brickwidth,brickheight))
    x+=130

x = 90
for i in range(totalbricks//4):
    rows.append(Brick(x,220,brickwidth,brickheight))
    x+=130

tim = 0
#game loop ========================================
while itsGoverBroski == False:
    #foundation ---------------
    time.tick(70)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            itsGoverBroski = True


    #update -------------------
    thePaddle.move()
    thePaddle.update()
    theBall.paddleCollision(thePaddle.getPosX(),thePaddle.getPosY(),padwidth,thePaddle.getVel())
    for i in range(len(rows)):
        if theBall.collision(rows[i].getBroken(), rows[i].getPosx(), rows[i].getPosy(),  brickwidth,  brickheight) == True:
            rows[i].collision()
            if rows[i].getBroken() >= 2:
                score+=1
    theBall.update()
    #render -------------------
    screen.fill((0,0,0))
    
    theBall.draw()
    for i in range(len(rows)):
        rows[i].draw()
    thePaddle.draw()

    pygame.draw.rect(screen,(175,165,165),(0,0,1210,900),30)
    pygame.draw.rect(screen,(255,255,255),(30,30,1150,840),2)
    if score == totalbricks:
        theBall.end(True)
    theBall.end(False)
    pygame.display.flip()
    tim+=1
    print(tim)