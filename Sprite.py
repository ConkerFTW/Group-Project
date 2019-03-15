import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector

class Sprite():
    def __init__(self, image, columns, rows):

        self.pos = Vector(500,500)

        self.image = simplegui.load_image(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.columns = columns
        self.rows = rows
        self.frameSize = (self.width // columns, self.height // rows)
        self.frameCentre = (self.frameSize[0] / 2, self.frameSize[1] / 2)
        self.sizeDest = (self.frameSize[0]*4, self.frameSize[0]*4)
        self.currentFrame = [0,0]


    def draw(self, canvas):
        centreDest = (self.pos.getP()[0], self.pos.getP()[1])
        centerSource = [self.frameSize[i] * self.currentFrame[i] + self.frameCentre[i] for i in [0, 1]]

        canvas.draw_image(self.image, centerSource, self.frameSize, centreDest, self.sizeDest)

    def distanceTo(self,other):
        return (self.pos - other.pos).length()

    def contains(self,other):
        return self.distanceTo(other.pos) <= self.sizeDest[0]

    def checkCollisionWith(self, other):
        if self.distanceTo(other.pos) <= self.sizeDest[0] + other.sizeDest[0]:
            return True

    def isStationary(self,vel):
        return vel.length() < 5
