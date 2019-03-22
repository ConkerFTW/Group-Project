import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import random

class Interaction():
    def __init__(self,player,keyboard,enemies,gui):
        self.player = player
        self.keyboard = keyboard
        self.enemies = enemies
        self.takingDamage = False
        self.counter = 0
        self.gui = gui

    def draw(self, canvas):
        self.update()
        self.player.update()
        self.player.draw(canvas)
        self.gui.draw(canvas)
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
                    if bullet.checkCollisionWith(self.player):
                        enemy.bullets.remove(bullet)
                        if not self.takingDamage:
                            self.player.removeLife()
                            self.takingDamage = True
                            self.counter = 1
                    if bullet.pos.getP()[0] > 1200 or bullet.pos.getP()[1] > 800 or bullet.pos.getP()[0] < -50 or bullet.pos.getP()[1] < -50:
                        enemy.bullets.remove(bullet)

            if enemy.checkCollisionWith(self.player):
                if not self.takingDamage:
                    self.player.removeLife()
                    self.takingDamage = True
                    self.counter = 1

            if self.counter % 120 == 0:
                self.takingDamage = False

        if self.player.lives <= 0:
            self.player.startDeath()
            print("Game Over")
        print(self.player.lives)

        self.counter += 1

        if len(self.enemies) == 0:
            #simplegui.Frame.stop()
            pass


