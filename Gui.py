from Sprite import Sprite
import random
from Bullet import Bullet
import os
from Vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Gui(Sprite):
    def __init__(self, image, image_alternate, columns, rows,playerLives):
        super().__init__(image, image_alternate, columns, rows)
        self.pos = Vector(60,50)
        self.playerLives = playerLives

    def draw(self,canvas):
        newpos = self.pos.copy()
        self.centerSource = [self.frameSize[i] * self.currentFrame[i] + self.frameCentre[i] for i in [0, 1]]
        self.sizeDest = (self.frameSize[0] / 10, self.frameSize[0] / 10)
        for i in range(self.playerLives.lives):
            self.centreDest = (newpos.getP()[0], newpos.getP()[1])
            canvas.draw_image(self.image, self.centerSource, self.frameSize, self.centreDest, self.sizeDest)
            newpos = Vector(newpos.getP()[0] + self.sizeDest[0],newpos.getP()[1])


