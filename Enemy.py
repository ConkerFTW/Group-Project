from Sprite import Sprite
import random
from Bullet import Bullet

from Vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Enemy(Sprite):
    def __init__(self,image,image_alternate,columns,rows,enemyType):
        super().__init__(image,image_alternate,columns,rows)
        self.moving = False
        self.shooting = False
        self.dead = False
        self.idle = False
        self.frameCounter = 0 # How many frames the Enemy has been alive
        self.enemyType = enemyType
        self.framestartshoot = 0
        self.bullets = []

        num = random.randrange(0, 2)


        if enemyType == "walker":
            if num == 1:
                self.pos = Vector(0,530)
            elif num == 0:
                self.pos = Vector(1000,530)
            self.health = 5
            self.vel = Vector(0,0)
            self.sizeDest = (self.sizeDest[0] /5,self.sizeDest[1]/5)

        elif enemyType == "shooter":
            if num == 1:
                self.pos = Vector(random.randrange(50,300),random.randrange(100,300))
                self.right = True
            elif num == 0:
                self.pos = Vector(random.randrange(700,950),random.randrange(100,300))
                self.right = False
            self.health = 1
            self.vel = Vector(0,0)
            self.sizeDest = (self.sizeDest[0] / 2, self.sizeDest[1] / 2)
            self.idle = True

    def randomSpeed(self, min, max):
        return random.randrange(min, max + 1)

    def update(self):
        self.updateState()
        if self.frameCounter % 20 == 0:
            self.currentFrame[0] += 1
        if self.enemyType == "walker": # TODO Update with more Enemies
            if self.moving:
                if self.currentFrame[0] > 3:
                    self.currentFrame[0] = 0
            elif self.idle:
                self.currentFrame[0] = 1

            if self.shooting:
                pass
            if self.dead:
                pass
            if self.idle:
                pass

        if self.enemyType == "shooter":
            if self.moving:
                pass
            if self.idle:
                self.currentFrame[1] = 0
                if self.right:
                    if self.currentFrame[0] > 2:
                        self.currentFrame[0] = 0
                else:
                    if self.currentFrame[0] > 6:
                        self.currentFrame[0] = 4
                    elif self.currentFrame[0] < 4:
                        self.currentFrame[0] = 4
            if self.shooting:
                self.framestartshoot += 1
                self.currentFrame[1] = 1
                if self.currentFrame[0] > 6:
                    self.currentFrame[0] = 0


        self.pos.add(self.vel)
        self.frameCounter += 1


    def updateState(self):
        if self.health == 0:
            self.dead = True


        if self.isStationary(self.vel):
            self.moving = False
            self.idle = True

        else:
            self.moving = True
            self.idle = False


        if self.enemyType == "shooter":
            if self.frameCounter % 120 == 0:
                self.shooting = True
                self.idle = False
                self.framestartshoot = 0

        if self.shooting:
            if self.framestartshoot >= 6:
                self.shooting = False
                self.idle = True






    def shoot(self,playerpos):
        x = -(self.pos.getP()[0] - playerpos.getP()[0]) / 100
        y = -(self.pos.getP()[1] - playerpos.getP()[1]) / 100
        vel = Vector(x,y)
        return Bullet(self.pos,vel,True) #Starting Pos, Starting Velocity(Direction Towards Player), if Hostile




