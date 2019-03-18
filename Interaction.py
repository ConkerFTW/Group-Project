import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import random

class Interaction():
    def __init__(self,player,keyboard,enemies):
        self.player = player
        self.keyboard = keyboard
        self.enemies = enemies

    def draw(self, canvas):
        self.update()
        self.player.update()
        self.player.draw(canvas)
        for enemy in self.enemies:
            enemy.update()
            enemy.draw(canvas)
            if len(enemy.bullets) > 0:
                for bullet in enemy.bullets:
                    bullet.update()
                    bullet.draw(canvas)


    def update(self):
        if self.keyboard.right:
            self.player.right = True
            self.player.startMoving()
        elif self.keyboard.left:
            self.player.right = False
            self.player.startMoving()
        else:
            self.player.stopMoving()

        # if self.keyboard.up:
        #     self.player.velocity += (Vector(0, -0.2))
        # if self.keyboard.down:
        #     self.player.velocity += (Vector(0, 0.2))

        for enemy in self.enemies:

            if enemy.shooting and enemy.framestartshoot == 3:
                enemy.bullets.append(enemy.shoot(self.player.pos))

            if enemy.frameCounter % 100 == 0:
                if enemy.enemyType == "walker":
                    if enemy.pos.getP()[0] < self.player.pos.getP()[0]:
                        enemy.vel = Vector(enemy.randomSpeed(0,2),enemy.vel.getP()[1])
                        enemy.right = True
                    elif enemy.pos.getP()[0] > self.player.pos.getP()[0]:
                        enemy.vel = Vector(-enemy.randomSpeed(0,2),enemy.vel.getP()[1])
                        enemy.right = False
            if len(enemy.bullets) > 0:
                for bullet in enemy.bullets:
                    if bullet.pos.getP()[0] > 1200 or bullet.pos.getP()[1] > 800 or bullet.pos.getP()[0] < -50 or bullet.pos.getP()[1] < -50:
                        enemy.bullets.remove(bullet)

