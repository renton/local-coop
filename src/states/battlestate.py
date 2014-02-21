import pygame
from pygame.locals import *
from state import State
from ..map import Map
from ..entities import ActionPlayer
from ..settings import *
from random import randint

class BattleState(State):

    def __init__(self,screen,rm):
        State.__init__(self,screen,rm)
        self._load_map()
        self.camera_x,self.camera_y = (0,0)
        self.camera_speed = 1
        self.bg = pygame.image.load(SETTINGS['asset_bg_path']+"sample_bg.jpg")

        self.p1 = ActionPlayer()

        self.fixed_camera = False

    def _step(self):
        self.p1._step()
        #self.camera_x,self.camera_y = self.p1.x, self.p1.y

    def _draw(self):
        self._draw_map()
        self._draw_action_player()

    def _draw_map(self):

        start_x_tile = self.camera_x/SETTINGS['tile_size']
        start_y_tile = self.camera_y/SETTINGS['tile_size']

        self.screen.blit(self.bg,(0,0))

        for x in range((SETTINGS['map_window_x_size']/SETTINGS['tile_size'])+SETTINGS['tile_size']):
            if (x+start_x_tile) in self.cur_map.tiles:
                for y in range((SETTINGS['map_window_y_size']/SETTINGS['tile_size'])+SETTINGS['tile_size']):
                    if (y+start_y_tile) in self.cur_map.tiles[x+start_x_tile]:
                        self.screen.blit(
                            self.rm.tilesets[self.cur_map.tileset_filename][0],
                            ((x*SETTINGS['tile_size'])-self.camera_x%SETTINGS['tile_size'],
                            (y*SETTINGS['tile_size'])-self.camera_y%SETTINGS['tile_size'])
                        )

    def _draw_action_player(self):

        pygame.draw.rect(
            self.screen,
            (100,0,0),
            (
                self.p1.x,
                self.p1.y,
                self.p1.width,
                self.p1.height
            ),
            0
        )

    def _input(self):
        State._input(self)

        if self.keystate[K_a]:
            if self.camera_x > 0:
                self.set_camera(self.camera_x-self.camera_speed,self.camera_y)
        if self.keystate[K_s]:
            if self.camera_y < ((self.cur_map.map_tile_height*SETTINGS['tile_size'])-SETTINGS['map_window_y_size']):
                self.set_camera(self.camera_x,self.camera_y+self.camera_speed)
        if self.keystate[K_d]:
            if self.camera_x < ((self.cur_map.map_tile_width*SETTINGS['tile_size'])-SETTINGS['map_window_x_size']):
                self.set_camera(self.camera_x+self.camera_speed,self.camera_y)
        if self.keystate[K_w]:
            if self.camera_y > 0:
                self.set_camera(self.camera_x,self.camera_y-self.camera_speed)

        # toggle fixed camera
        if self.keystate[K_q]:
            self.fixed_camera = not self.fixed_camera


        if self.keystate[K_f]:
            self.p1.dx = -2
        if self.keystate[K_g]:
            self.p1.dy = 2
        if self.keystate[K_h]:
            self.p1.dx = 2
        if self.keystate[K_t]:
            self.p1.dy = -2

    def set_camera(self,x,y):
        self.camera_x,self.camera_y = (x,y)
        

    def _load_map(self):
        self.cur_map = Map()
        self.rm.load_tileset(self.cur_map.tileset_filename)
