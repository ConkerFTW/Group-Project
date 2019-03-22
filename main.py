import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Sprite import Sprite
from KeyBoard import KeyBoard
from Bullet import Bullet
from Player import Player
from Vector import Vector
from Interaction import Interaction
from Enemy import Enemy
import os

def spawnEnemies(walkers, shooters):
    enemies = []
    for i in range(0, walkers):
        enemies.append(Enemy(fman,fmanleft,4,1,"walker"))
    for i in range(0,shooters):
        enemies.append(Enemy(fwiz,fwizleft,7,6,"shooter"))
    enemies.append(Enemy(error,error,1,1,"missileLauncher"))


    enemiescopy = enemies
    for enemy in enemiescopy:
        for other in enemiescopy:
            if enemy.checkCollisionWith(other) and enemy.enemyType == "shooter" and other != enemy:
                other.pos = Vector(other.pos.getP()[0] + 20,other.pos.getP()[1] + 20)
                if enemy.checkCollisionWith(other):
                    enemies.remove(other)

    return enemies




__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
fcat = os.path.join(__location__, 'images/sprites/cat_ar_base.png')
fman = os.path.join(__location__, 'images/sprites/kramer_sprites.png')
fmanleft = os.path.join(__location__, 'images/sprites/kramer_sprites_left.png')
fwiz =  os.path.join(__location__, 'images/sprites/wizzardRight.png')
fwizleft = os.path.join(__location__, 'images/sprites/wizzardLeft.png')
error =  os.path.join(__location__, 'images/sprites/error.png')


WIDTH = 1000
HEIGHT = 600
player = Player(fcat,fcat,16,16)
keyboard = KeyBoard()
enemies = spawnEnemies(3,0)

interaction = Interaction(player,keyboard,enemies)
frame = simplegui.create_frame("Catmando", WIDTH, HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)
frame.start()



