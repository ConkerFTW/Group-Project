from Sprite import Sprite
import random
from Bullet import Bullet
import os


from Vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Enemy(Sprite):
    def __init__(self,image,image_alternate,columns,rows,enemyType):
        super().__init__(image,image_alternate,columns,rows)
        self.moving = False
        self.shooting = False
        self.dead = False
        self.idle = False
        self.enemyType = enemyType
        self.framestartshoot = 0
        self.bullets = []


        num = random.randrange(0, 2)

        # Spawn each enemy in different areas depending on their type
        if enemyType == "walker":
            if num == 1:
                self.pos = Vector(0,650)
            elif num == 0:
                self.pos = Vector(1280,650)
            self.health = 5
            self.vel = Vector(0,0)
            self.sizeDest = (self.sizeDest[0] /5,self.sizeDest[1]/5)

        elif enemyType == "shooter":
            if num == 1:
                self.pos = Vector(random.randrange(50,440),random.randrange(100,360))
                self.right = True
            elif num == 0:
                self.pos = Vector(random.randrange(840,1230),random.randrange(100,360))
                self.right = False
            self.health = 1
            self.vel = Vector(0,0)
            self.sizeDest = (self.sizeDest[0] / 2, self.sizeDest[1] / 2)
            self.idle = True

        # This enemy that fires the missiles is off screen and cannot be seen
        elif self.enemyType == "missileLauncher":
            self.pos = Vector(-2000,-2000)
            self.right = True
            self.health = 100
            self.vel = Vector(0,0)


    def randomSpeed(self, min, max):
        return random.randrange(min, max + 1)

    def update(self):
        self.updateState()
        #Update all the spritesheets depending on their type
        if self.frameCounter % 20 == 0:
            self.currentFrame[0] += 1
        if self.enemyType == "walker": # TODO Update with more Enemies
            if self.moving:
                if self.currentFrame[0] > 3:
                    self.currentFrame[0] = 0
            elif self.idle:
                self.currentFrame[0] = 1
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

        if self.enemyType == "missileLauncher":
            number1 = random.randrange(0, 200)
            number2 = random.randrange(0 ,200)

            # Randomly fires a Missile if the random numbers are equal
            if number1 == number2:
                self.bullets.append(self.horizontalShoot())

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
            num1 = random.randrange(0,100)
            num2 = random.randrange(0,100)

            #Randomly shoot a bullet
            if num1 == num2:
                self.shooting = True
                self.idle = False
                self.framestartshoot = 0

            if self.shooting:
                if self.framestartshoot >= 6:
                    self.shooting = False
                    self.idle = True






    def shoot(self,playerpos):
        #Targets the player
        x = -(self.pos.getP()[0] - playerpos.getP()[0]) / 100
        y = -(self.pos.getP()[1] - playerpos.getP()[1]) / 100
        vel = Vector(x,y)

        if  x > 0:
            right = True
        else:
            right = False

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        imagenormal = os.path.join(__location__, 'images/sprites/fireballRight.png')
        imagealternate = os.path.join(__location__, 'images/sprites/fireballLeft.png')

        return Bullet(self.pos,vel,True,"magic",right,imagenormal,imagealternate, 8,8) #Starting Pos, Starting Velocity(Direction Towards Player), if Hostile

    def horizontalShoot(self):
        #Fires across screen ar set speed, cannot be killed hence is a Bullet not Enemy
        yStart = random.randrange(20,670)
        xStart = random.choice([0,1280])
        startPos = Vector(xStart,yStart)
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        imagenormal = os.path.join(__location__, 'images/sprites/flyingRight.png')
        imagealternate = os.path.join(__location__, 'images/sprites/flyingLeft.png')

        if xStart == 0:
            vel = Vector(3,0)
            right = True
        else:
            vel = Vector(-3,0)
            right = False

        return Bullet(startPos,vel,True,"missile",right,imagenormal,imagealternate,5,1)
