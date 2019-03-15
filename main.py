import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Sprite import Sprite
from KeyBoard import KeyBoard
from Bullet import Bullet
from Player import Player
from Vector import Vector
from Interaction import Interaction
from Enemy import Enemy

WIDTH = 1000
HEIGHT = 600
player = Player("/home/conor/PycharmProjects/GroupProject/cat_ar_base.png",16,16)
keyboard = KeyBoard()
enemy1 = Enemy("/home/conor/PycharmProjects/GroupProject/kramer_sprites.png",1,7,"walker")

interaction = Interaction(player,keyboard,enemy1)
frame = simplegui.create_frame("Catmando", WIDTH, HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)

frame.start()


