from Vector import Vector
class Bullet:
    def __init__(self,pos,vel,hostile):
        self.pos = pos
        self.dx = vel
        self.radius = 4
        self.hostile = hostile


    def draw(self,canvas):
        canvas.draw_circle((self.pos.getP()[0], self.pos.getP()[1]), self.radius, 1, 'Cyan', 'Cyan')

    def update(self):
        self.pos = Vector(self.pos.getP()[0]+self.dx.getP()[0], self.pos.getP()[1]+self.dx.getP()[1])


