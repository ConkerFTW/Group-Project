import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from KeyBoard import KeyBoard
from Sprite import Sprite
from Vector import Vector
from Bullet import Bullet
import os


class Player(Sprite):
    def __init__(self, image,image_alternate, columns, rows):
        super().__init__(image,image_alternate, columns, rows)
        self.lives = 3
        self.nonInterrupt = False
        self.moving = False
        self.dead = False
        self.shooting = False
        self.jumping = False
        self.rolling = False
        self.invincible = False
        self.bullets = []
        self.velocity = Vector(0, 0)
        self.pos = Vector(500,500)
        self.gravity = Vector(0, 0)
        self.frameCounter = 0

    def update(self):
        if self.frameCounter % 10 == 0:
            self.updateFrame()
        self.updateVel()
        self.updateAcceleration()
        self.pos += self.velocity
        if self.pos.getP()[1] > 500:
            self.pos = Vector(self.pos.getP()[0], 500)
        elif self.pos.getP()[1] < 0:
            self.pos = Vector(self.pos.getP()[0], 1)
            self.jumping = False
        if self.pos.getP()[0] > 975:
            self.pos = Vector(975, self.pos.getP()[1])
        elif self.pos.getP()[0] < 25:
            self.pos = Vector(25, self.pos.getP()[1])
        self.frameCounter += 1

    def draw(self, canvas):
        if self.right:
            centreDest = (self.pos.getP()[0], self.pos.getP()[1])
            centerSource = [self.frameSize[i] * self.currentFrame[i] + self.frameCentre[i] for i in [0, 1]]
            canvas.draw_image(self.image, centerSource, self.frameSize, centreDest, self.sizeDest)
        else:
            centreDest = (self.pos.getP()[0], self.pos.getP()[1])
            centerSource = [(self.width - (self.frameSize[0] * self.currentFrame[0] + self.frameCentre[0])), (self.frameSize[1] * self.currentFrame[1] + self.frameCentre[1])]
            canvas.draw_image(self.alternateimage, centerSource, self.frameSize, centreDest, self.sizeDest)


    # Updating the frame depending on the animation
    def updateFrame(self):
        self.currentFrame[0] += 1

        # Death animation
        if self.dead:
            self.currentFrame[1] = 8
            if self.currentFrame[0] >= 7:
                self.currentFrame[0] = 0
                # Run Game Over

        # Rolling
        #elif self.rolling:
        #    self.currentFrame[1] = 7
        #  # Run rolling animation
        #    if self.currentFrame[0] >= 4:
        #        self.currentFrame[0] = 0
        #        self.rolling = False

        # Jumping while not shooting
        elif self.jumping and not self.shooting:
            self.currentFrame[1] = 5
            if self.currentFrame[0] >= 6:
                self.currentFrame[0] = 4

        # Jumping while shooting
        elif self.jumping and self.shooting:
            if self.currentFrame[1] == 4 or self.currentFrame[1] == 5:
                self.currentFrame[0] = 6
            elif self.currentFrame[0] < 10:
                self.currentFrame[0] = 5
            else:
                self.currentFrame[0] = 0
                self.jumping = False
                self.nonInterrupt = False

        # Shooting while still
        elif self.shooting and not self.moving:
            self.currentFrame[1] = 2
            if self.currentFrame[0] >= 8:
                self.currentFrame[0] = 0

        # Shooting while moving
        elif self.moving and self.shooting:
            self.currentFrame[1] = 4
            if self.currentFrame[0] >= 8:
                self.currentFrame[0] = 0

        # Moving while not shooting
        elif self.moving and not self.shooting:
            self.currentFrame[1] = 3
            if self.currentFrame[0] >= 8:
                self.currentFrame[0] = 0

        # Doing nothing
        else:
            self.currentFrame[1] = 1
            if self.currentFrame[0] >= 8:
                self.currentFrame[0] = 0

    # Updating the velocity
    def updateVel(self):
        if self.moving:
            # Change horizontal velocity
            if self.right:
                self.velocity = Vector(5, self.velocity.getP()[1])
            else:
                self.velocity = Vector(-5, self.velocity.getP()[1])

        self.velocity = Vector(self.velocity.getP()[0] * 0.94, self.velocity.getP()[1])
        self.velocity += self.gravity

    # Updating the acceleration
    def updateAcceleration(self):
        if self.pos.getP()[1] < 500 and not self.jumping:
            self.gravity = Vector(0, 3)
        else:
            self.gravity = Vector(0, 0)

    # Method to spawn bullet
    def shoot(self):
        xStart, yStart = self.pos.getP()
        startPos = Vector(xStart, yStart + 30)
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        imagenormal = os.path.join(__location__, 'images/sprites/fireballRight.png')
        imagealternate = os.path.join(__location__, 'images/sprites/fireballLeft.png')

        if self.right:
            vel = Vector(3, 0)
            right = True
        else:
            vel = Vector(-3, 0)
            right = False

        return Bullet(startPos, vel, False, "missile", right, imagenormal, imagealternate, 8, 8)

    # Following methods to be called in interaction class after user inputs
    def startMoving(self):
        self.moving = True

    def startShooting(self):
        self.shooting = True
        self.bullets.append(self.shoot())

    def startRoll(self):
        self.rolling = True

    def startJump(self):
        self.jumping = True
        self.velocity = Vector(self.velocity.getP()[0], -10)

    def stopJump(self):
        self.jumping = False

    # Called from interaction class when user input ends
    def stopMoving(self):
        self.moving = False

    def stopShooting(self):
        self.shooting = False

    # Called from interaction class following collision
    def removeLife(self):
        if not self.invincible:
            self.lives -= 1
            if self.lives == 0:
                self.startDeath()

    # Called by self when lives.png = 0
    def startDeath(self):
        self.dead = True