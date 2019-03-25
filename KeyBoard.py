import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Class for keyboard inputs to be handled
class KeyBoard:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        # Down key input not used in final game
        # self.down = False
        self.space = False
        '''
        (Potential 2-Player controls)
        self.w = False
        self.a = False        
        self.s = False
        self.d = False
        self.shift = False
        '''

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        #if key == simplegui.KEY_MAP['down']:
        #    self.down = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

        '''
        (Potential 2-Player controls)
        if key == simplegui.KEY_MAP['w']:
            self.w = True
        if key == simplegui.KEY_MAP['a']:
            self.a = True
        if key == simplegui.KEY_MAP['s']:
            self.s = True
        if key == simplegui.KEY_MAP['d']:
            self.d = True
        if key == simplegui.KEY_MAP['shift']:
            self.shift = True
        '''

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        #if key == simplegui.KEY_MAP['down']:
        #    self.down = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False

        '''
        (Potential 2-Player controls)
        if key == simplegui.KEY_MAP['w']:
            self.w = False
        if key == simplegui.KEY_MAP['a']:
            self.a = False
        if key == simplegui.KEY_MAP['s']:
            self.s = False
        if key == simplegui.KEY_MAP['d']:
            self.d = False
        if key == simplegui.KEY_MAP['shift']:
            self.shift = False
        '''