import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Sprite import Sprite
from KeyBoard import KeyBoard
from Bullet import Bullet
from Player import Player
from Vector import Vector
from Interaction import Interaction
from Enemy import Enemy
from Gui import Gui
import os
class Game():
    def __init__(self):
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.fcat = os.path.join(self.__location__, 'images/sprites/catmandoRight.png')
        self.fcatleft = os.path.join(self.__location__, 'images/sprites/catmandoLeft.png')
        self.fman = os.path.join(self.__location__, 'images/sprites/kramer_sprites.png')
        self.fmanleft = os.path.join(self.__location__, 'images/sprites/kramer_sprites_left.png')
        self.fwiz = os.path.join(self.__location__, 'images/sprites/wizzardRight.png')
        self.fwizleft = os.path.join(self.__location__, 'images/sprites/wizzardLeft.png')
        self.lives = os.path.join(self.__location__, 'images/lives.png')
        self.error = os.path.join(self.__location__, 'images/sprites/error.png')
        self.level = 1
        self.WIDTH = 1000
        self.HEIGHT = 600
        self.player = Player(self.fcat, self.fcatleft, 16, 16)
        self.keyboard = KeyBoard()
        self.enemies = self.spawnEnemies(0, 0)
        self.gui = Gui(self.lives, self.lives, 1, 1, self.player)


        self.interaction = Interaction(self.player, self.keyboard, self.enemies,self.gui)
        self.frame = simplegui.create_frame("Catmando", self.WIDTH, self.HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)

    def spawnEnemies(self,walkers, shooters):
        enemies = []
        for i in range(0, walkers):
            enemies.append(Enemy(self.fman,self.fmanleft,4,1,"walker"))
        for i in range(0,shooters):
            enemies.append(Enemy(self.fwiz,self.fwizleft,7,6,"shooter"))
        enemies.append(Enemy(self.error,self.error,1,1,"missileLauncher"))


        enemiescopy = enemies
        for enemy in enemiescopy:
            for other in enemiescopy:
                if enemy.checkCollisionWith(other) and enemy.enemyType == "shooter" and other != enemy:
                    other.pos = Vector(other.pos.getP()[0] + 20,other.pos.getP()[1] + 20)
                    if enemy.checkCollisionWith(other):
                        enemies.remove(other)

        return enemies

    def draw(self,cavnas):
        self.interaction.draw(cavnas)
        if len(self.interaction.enemies) == 1:
            self.player.lives += 1
            self.level += 1
            self.player.bullets.clear()
            if self.level == 2:
                self.enemies = self.spawnEnemies(5, 0)
            elif self.level == 3:
                self.enemies = self.spawnEnemies(4, 3)
            elif self.level == 4:
                self.enemies = self.spawnEnemies(6, 6)
            elif self.level == 5:
                self.enemies.clear()
                print("Boss Time")
            self.interaction.enemies = self.enemies
        if self.player.dead:
            self.frame.stop()


    def startLevel(self):
        self.frame.start()


game = Game()
game.startLevel()

