import sys,pygame
from pygame.locals import *
from settings import *
from resource_manager import ResourceManager

from states import BattleState

class Game():

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = SETTINGS['default_fps']

        # fullscreen on/off
        if SETTINGS['fullscreen_mode']:
            self.screen = pygame.display.set_mode((
                                                    SETTINGS['window_x_size'],
                                                    SETTINGS['window_y_size']
                                                    ),
                                                    pygame.FULLSCREEN
                                                )
        else:
            self.screen = pygame.display.set_mode((
                                                    SETTINGS['window_x_size'],
                                                    SETTINGS['window_y_size']
                                                ))

        # load resource manager
        self.rm = ResourceManager()

        # state setup
        self.cur_state = BattleState(self.screen,self.rm)
            

    def _step(self):
        # let state handle step
        self.cur_state._step()

    def _draw(self):
        self.screen.fill((0,0,0))

        # let state handle drawing
        self.cur_state._draw()

    def mainloop(self):
        while(1):
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()

            # let state handle input
            self.cur_state._input()

            # draw frame
            self._draw()
            self.clock.tick(self.fps)
            pygame.display.flip()

            # step frame
            self._step()
