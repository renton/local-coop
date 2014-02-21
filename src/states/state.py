import sys,pygame
from pygame.locals import *

class State():

    def __init__(self,screen,rm):
        self.screen = screen
        self.rm = rm

        # initialize input buffers
        self.mouse_x,self.mouse_y = (0,0)
        self.mousestate = {}
        self.keystate = {}

    def _draw(self):
        pass

    def _step(self):
        pass

    def _input(self):
        self._fetch_inputs()

        # key input handling
        if self.keystate[K_ESCAPE]:
            pygame.display.quit()
            sys.exit()

    def _fetch_inputs(self):
        self.keystate = pygame.key.get_pressed()
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.mousestate = pygame.mouse.get_pressed()
