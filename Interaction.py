import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector

class Interaction():
    def __init__(self,player,keyboard,enemy):
        self.player = player
        self.keyboard = keyboard
        self.enemy = enemy

    def draw(self, canvas):
        self.update()
        self.player.update()
        self.player.draw(canvas)
        self.enemy.update()
        self.enemy.draw(canvas)


    def update(self):
        if self.keyboard.right:
            self.player.velocity += (Vector(0.2, 0))
            self.player.startMoving()
        if self.keyboard.left:
            self.player.velocity += (Vector(-0.2, 0))
            self.player.startMoving()
        if self.keyboard.up:
            self.player.velocity += (Vector(0, -0.2))
        if self.keyboard.down:
            self.player.velocity += (Vector(0, 0.2))

        if self.enemy.frameCounter % 100 == 0:
            if self.enemy.enemyType == "walker":
                if self.enemy.pos.getP()[0] < self.player.pos.getP()[0]:
                    self.enemy.vel = Vector(1,self.enemy.vel.getP()[1])
                    self.enemy.right = True
                elif self.enemy.pos.getP()[0] > self.player.pos.getP()[0]:
                    self.enemy.vel = Vector(-1,self.enemy.vel.getP()[1])
                    self.enemy.right = False

