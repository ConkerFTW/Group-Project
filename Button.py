import pygame, sys

pygame.init ()

WHITE = (255, 255, 255)
GREY = (111, 114, 119)
BLACK = (0, 0, 0)
pygame.display.set_caption ('Catmando')


startGame = False
class Button ():
    def __init__(self, txt, location, action, bg=GREY, fg=BLACK, size=(200, 50), font_name="Segoe Print",
                 font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont (font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render (self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect (center = [s // 2 for s in self.size])

        self.surface = pygame.surface.Surface (size)
        self.rect = self.surface.get_rect (center = location)

        self.call_back_ = action

    def draw(self):
        self.mouseover ()

        self.surface.fill (self.bg)
        self.surface.blit (self.txt_surf, self.txt_rect)
        screen.blit (self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos ()
        if self.rect.collidepoint (pos):
            self.bg = GREY  # mouseover color

    def call_back(self):
        self.call_back_ ()


def my_start_function():
    global startGame
    startGame = True


#def my_options_function():
   # print ("OPTIONS " * 5)


def my_exit_function():
    pygame.quit ()
    sys.exit()


def mousebuttondown():
    pos = pygame.mouse.get_pos ()
    for button in buttons:
        if button.rect.collidepoint (pos):
            button.call_back ()


screen = pygame.display.set_mode ((1000, 800))
RED = (255, 0, 0)
BLUE = (0, 0, 255)

button_01 = Button ("START", (540, 310), my_start_function)
#button_02 = Button ("OPTIONS", (540, 390), my_options_function, bg = (111, 114, 119))
button_03 = Button ("EXIT", (540, 460), my_exit_function, bg = (111, 114, 119))
buttons = [button_01, button_03]
background_image = pygame.image.load ("images/city14.png").convert ()


def menu():
    while True:
        screen.blit (background_image, [0, 0])
        for button in buttons:
            button.draw ()
        pygame.display.flip ()
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit ()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousebuttondown ()
        global startGame
        if startGame == True:
            return True




pygame.time.wait (40)

# pygame.quit()