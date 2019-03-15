import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from KeyBoard import KeyBoard
from Sprite import Sprite
from Vector import Vector

class Player(Sprite):
    def __init__(self, image,image_alternate, columns, rows):
        super().__init__(image,image_alternate, columns, rows)
        self.lives = 3
        self.left = True  # Default spritesheet goes left
        self.nonInterupt = False
        self.moving = False
        self.dead = False
        self.shooting = False
        self.jumping = False
        self.rolling = False
        self.velocity = Vector(0, 0)
        self.pos = Vector(500,500)

    def update(self):
        self.updateFrame()
        #self.updateVel()
        self.pos += self.velocity
        self.velocity.multiply(0.94)
        self.updateVel()

    # Updating the frame depending on the animation
    def updateFrame(self):
        self.currentFrame[0] += 1

        # Death animation
        if self.dead:
            self.currentFrame[0] = 8
            if self.currentFrame[1] >= 7:
                pass
                # Run Game Over

        # # Rolling
        # elif self.rolling:
        #     self.currentFrame[0] = 7
        #     # Run rolling animation
        #     if self.currentFrame >= 4:
        #         self.currentFrame = 0
        #         self.rolling = False
        #         self.nonInterrupt = False
        #
        # # Jumping while not shooting
        # elif self.jumping and not self.shooting:
        #     self.currentFrame[0] = 5
        #     if self.currentFrame[1] >= 10:
        #         self.currentFrame[1] = 0
        #         self.jumping = False
        #         self.nonInterrupt = False
        #
        # # Jumping while shooting
        # elif self.jumping and self.shooting:
        #     if self.currentFrame[1] == 4 or self.currentFrame[1] == 5:
        #         self.currentFrame[0] = 6
        #     elif self.currentFrame < 10:
        #         self.currentFrame[0] = 5
        #     else:
        #         self.currentFrame = 0
        #         self.jumping = False
        #         self.nonInterrupt = False
        #
        # # Shooting while still
        # elif self.shooting and not self.moving:
        #     self.currentFrame[0] = 2
        #     if self.currentFrame >= 8:
        #         self.currentFrame = 0
        #
        # # Shooting while moving
        # elif self.moving and self.shooting:
        #     self.currentFrame[0] = 4
        #     if self.currentFrame[1] >= 8:
        #         self.currentFrame[1] = 0

        # Moving while not shooting
        elif self.moving and not self.shooting:
            self.currentFrame[1] = 3
            if self.currentFrame[0] >= 8:
                self.currentFrame[0] = 0

        # Doing nothing
        else:
            self.currentFrame[0] = 1
            if self.currentFrame[1] >= 8:
                self.currentFrame[1] = 0

    # Updating the velocity
    def updateVel(self):
        if self.moving:
            # Change horizontal velocity
            if self.right:
                self.velocity = Vector(5, 0)
            else:
                self.velocity = Vector(-5, 0)
        if self.jumping:
            self.velocity += Vector(2, 0)
            # Change vertical velocity

    # Following methods to be called in interaction class after user inputs
    def startMoving(self):
        self.moving = True

    def startShooting(self):
        self.shooting = True

    def startRoll(self):
        if not self.nonInterrupt:
            self.currentFrame[1] = 0
            self.rolling = True
            self.nonInterupt = True

    def startJump(self):
        if not self.nonInterrupt:
            self.currentFrame[1] = 0
            self.jumping = True
            self.nonInterupt = True

    # Called from interaction class when user input ends
    def stopMoving(self):
        self.moving = False

    def stopShooting(self):
        self.shooting = False

    # Called from interaction class following collision
    def removeLife(self):
        self.lives -= 1
        if self.lives == 0:
            self.startDeath()

    # Called by self when lives = 0
    def startDeath(self):
        self.currentFrame[1] = 0
        self.dead = True