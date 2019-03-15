import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Bullet:
    def __init__(self,x,y,dx):
        self.x = x
        self.y = y
        self.dx = dx
        self.radius = 4


    def draw(self,canvas):
        canvas.draw_circle((self.x, self.y), self.radius, 1, 'Cyan', 'Cyan')
        self.x = self.x + self.dx
