from Vector import Vector
from Sprite import Sprite
class Bullet(Sprite):
    def __init__(self,pos,vel,hostile,bulletType,right, image, image_alternate, columns, rows):
        super().__init__(image,image_alternate,columns,rows)
        self.pos = pos
        self.dx = vel
        self.radius = 4
        self.hostile = hostile
        self.type = bulletType
        self.right = right
        if self.type == "magic":
            self.sizeDest = [50,50]
        if self.type == "missile":
            self.sizeDest = [self.sizeDest[0]/30,self.sizeDest[1]/30]
        if self.type == "bullet":
            self.sizeDest = [self.sizeDest[0]/4,self.sizeDest[1]/4]


    def update(self):
        self.pos = Vector(self.pos.getP()[0]+self.dx.getP()[0], self.pos.getP()[1]+self.dx.getP()[1])

        if self.type == "missile":
            if self.frameCounter % 20 == 0:
                self.currentFrame[0] += 1
                if self.currentFrame[0] > 4:
                    self.currentFrame[0] = 0


        if self.type == "magic":
            if self.currentFrame[0] > 4:
                self.currentFrame[0] = 0
            else:
                self.currentFrame[0] += 1

        if self.type == "bullet":
            if self.currentFrame[0] > 7:
                self.currentFrame[0] = 0
            elif self.frameCounter % 2 == 0:
                self.currentFrame[0] += 1


        self.frameCounter += 1


    def checkCollisionWith(self, other):
        if self.type == "missile":
            if self.distanceTo(other.pos) <= self.sizeDest[0]/2: #Changes the Value to account for larger hitboxes
                return True
        elif self.type == "magic":
            if self.distanceTo(other.pos) <= self.sizeDest[0]:
                return True


        else:
            if self.distanceTo(other.pos) <= other.sizeDest[0]/3 or self.distanceTo(other.pos) <= other.sizeDest[1]/2:
                return True




