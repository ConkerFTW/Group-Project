from Sprite import Sprite

from Vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Enemy(Sprite):
    def __init__(self,image,columns,rows,enemyType):
        super().__init__(image,columns,rows)
        self.moving = False
        self.shooting = False
        self.dead = False
        self.idle = False
        self.frameCounter = 0 # How many frames the Enemy has been alive
        self.enemyType = enemyType
        if enemyType == "walker":
            self.health = 5
            self.vel = Vector(2,0)
            self.pos = Vector(300,500)
            self.sizeDest = (self.sizeDest[0] /3,self.sizeDest[1]/3)

        else:
            self.health = 1
            self.vel = Vector()


    def update(self):
        if self.frameCounter % 20 == 0:
            self.currentFrame[0] += 1
        if self.enemyType == "walker": # TODO Update with more Enemies
            self.moving = True
            if self.moving:
                if self.currentFrame[0] > 3:
                    self.currentFrame[0] = 0
            if self.shooting:
                pass
            if self.dead:
                pass
            if self.idle:
                pass
        self.pos.add(self.vel)
        self.frameCounter += 1


    def updateState(self):
        if self.health == 0:
            self.dead = True
        if not self.isStationary():
            self.moving = True
        if self.enemyType == "shooter":
            if self.frameCounter % 60 == 0:
                self.shooting = True
                self.idle = False
            else:
                self.shooting = False
                self.idle = True



    def shoot(self):
        if self.pos < 500: #Centre of the Screen
            vel = Vector(10,0)
        else:
            vel = Vector(-10,0)
        return Bullet(self.pos,vel,True) #Starting Pos, Starting Velocity(Direction Towards Player), if Hostile




