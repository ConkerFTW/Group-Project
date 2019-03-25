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
from FinalBoss import start

WIDTH = 1280
HEIGHT = 720
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
        self.load = os.path.join(self.__location__, 'images/loading.png')
        self.loading = simplegui._load_local_image(self.load)
        self.back = os.path.join(self.__location__, 'images/1280x720GameBackground.png')
        self.background = simplegui._load_local_image(self.back)
        self.level = 0
        self.player = Player(self.fcat, self.fcatleft, 16, 16)
        self.keyboard = KeyBoard()
        self.enemies = []
        self.gui = Gui(self.lives, self.lives, 1, 1, self.player)
        self.counter = 0
        self.gameOver = False

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        soundeffect = os.path.join(__location__, 'Sounds/bensound-jazzyfrenchy.ogg')
        self.music1 = simplegui._load_local_sound(soundeffect)

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        soundeffect = os.path.join(__location__, 'Sounds/bensound-theelevatorbossanova.ogg')
        self.music2 = simplegui._load_local_sound(soundeffect)

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        soundeffect = os.path.join(__location__, 'Sounds/Captive_Portal_-_03_-_An_Example_For.ogg')
        self.music3 = simplegui._load_local_sound(soundeffect)


        self.interaction = Interaction(self.player, self.keyboard, self.enemies,self.gui)
        self.frame = simplegui.create_frame("Catmando", WIDTH, HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)

    def spawnEnemies(self,walkers, shooters, missile = 1):
        enemies = []
        for i in range(0, walkers):
            enemies.append(Enemy(self.fman,self.fmanleft,4,1,"walker"))
        for i in range(0,shooters):
            enemies.append(Enemy(self.fwiz,self.fwizleft,7,6,"shooter"))
        for i in range(0,missile):
            enemies.append(Enemy(self.error,self.error,1,1,"missileLauncher"))


        enemiescopy = enemies
        for enemy in enemiescopy:
            for other in enemiescopy:
                if enemy.checkCollisionWith(other) and enemy.enemyType == "shooter" and other != enemy:
                    other.pos = Vector(other.pos.getP()[0] + 20,other.pos.getP()[1] + 20)
                    if enemy.checkCollisionWith(other):
                        enemies.remove(other)

        return enemies

    def draw(self, canvas):
        self.interaction.draw(canvas)
        if self.level == 0 and self.counter < 300:
            intro_text1 = "Our story begins with a special operations unit known as..."
            intro_text2 = "THE CATMANDO!"
            intro_text3 = "Today he has been sent on a high stakes diplomacy mission!"
            intro_text4 = "Well sort of..."
            canvas.draw_text(intro_text1, (200, 50), 44, "Black")
            canvas.draw_text(intro_text2, (200, 100), 44, "Black")
            canvas.draw_text(intro_text3, (200, 150), 44, "Black")
            canvas.draw_text(intro_text4, (200, 200), 44, "Black")
            self.counter += 1

        elif len(self.interaction.enemies) <= 1:
            self.counter += 1
            canvas.draw_image(self.loading,(256,256),(512,512),(WIDTH/2,HEIGHT/2),(512,512))
            if self.counter % 120 == 0:
                self.player.lives += 1
                self.level += 1
                self.player.bullets.clear()
                if self.level == 1:
                    self.enemies = self.spawnEnemies(2, 0)
                    self.music1.play()

                elif self.level == 2:
                    self.enemies = self.spawnEnemies(10, 1)

                elif self.level == 3:
                    self.enemies = self.spawnEnemies(5, 3)

                elif self.level == 4:
                    self.enemies = self.spawnEnemies(8,4)

                elif self.level == 5:
                    self.enemies = self.spawnEnemies(8,5)
                    self.music1.pause()
                    self.music3.play()

                elif self.level == 6:
                    self.enemies = self.spawnEnemies(10,7)

                elif self.level == 7:
                    self.enemies.clear()
                    self.enemies = self.spawnEnemies(0,0,50)
                    self.music2.play()
                    self.music3.pause()
                    self.gameOver = True

                self.interaction.enemies = self.enemies
                self.counter = 0
        if self.player.dead:
            self.frame.stop()
        if self.gameOver == True:
            self.counter += 1
            canvas.draw_text("Game Over",(320,HEIGHT/2),124,"Black")
            if self.counter == 200:
                #start()
                self.frame.stop()




    def startLevel(self):
        self.frame._set_canvas_background_image(self.background)
        self.frame.start()



game = Game()
game.startLevel()

