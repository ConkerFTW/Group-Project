import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Sprite import Sprite
from KeyBoard import KeyBoard
from Bullet import Bullet
from Player import Player
from Vector import Vector
from Interaction import Interaction
from Enemy import Enemy
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
fcat = os.path.join(__location__, 'cat_ar_base.png');
fman = os.path.join(__location__, 'kramer_sprites.png');

WIDTH = 1000
HEIGHT = 600
player = Player(fcat,16,16)
keyboard = KeyBoard()
enemy1 = Enemy(fman,4,1,"walker")

interaction = Interaction(player,keyboard,enemy1)
frame = simplegui.create_frame("Catmando", WIDTH, HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)

frame.start()


