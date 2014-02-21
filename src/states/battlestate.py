import pygame
from pygame.locals import *
from state import State
from ..map import Map
from ..entities import ActionPlayer
from ..settings import *
from random import randint

class BattleState(State):

    # TODO - problem with float x,y values and camera

    def __init__(self,screen,rm):
        State.__init__(self,screen,rm)
        self._load_map()
        self.camera_x,self.camera_y = (0,0)
        self.camera_speed = 1
        self.bg = pygame.image.load(SETTINGS['asset_bg_path']+"sample_bg.jpg")

        self.p1 = ActionPlayer()

        self.fixed_camera = True

    def _step(self):
        self.p1._step(self.cur_map)

        if not self.fixed_camera:
            self.center_camera_on_target(self.p1)

    def _load_map(self):
        self.cur_map = Map()
        self.rm.load_tileset(self.cur_map.tileset_filename)

    # ======================================================================a
    #   INPUT
    # ======================================================================
    def _input(self):
        State._input(self)

        if self.fixed_camera:
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


        if self.keystate[K_f]:
            self.p1.dx = -2
        if self.keystate[K_h]:
            self.p1.dx = 2
        if self.keystate[K_t]:
            print self.p1.dy
            if self.p1.on_ground:
                self.p1.dy = -5

        # toggle fixed camera
        if self.keystate[K_z]:
            self.fixed_camera = True
        if self.keystate[K_x]:
            self.fixed_camera = False

    # ======================================================================a
    #   DRAWING
    # ======================================================================
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

        # TODO - only draw if in window frame

        pygame.draw.rect(
            self.screen,
            (100,0,0),
            (
                self.p1.x-self.camera_x,
                self.p1.y-self.camera_y,
                self.p1.width,
                self.p1.height
            ),
            0
        )

    # ======================================================================a
    #   CAMERA
    # ======================================================================

    def set_camera(self,x,y):
        self.camera_x,self.camera_y = (x,y)

    def center_camera_on_target(self,entity):

        target_x = entity.x
        target_y = entity.y

        # TODO camera as int and entities as float. does this cause problems?
        self.camera_x,self.camera_y = (
                                        int(target_x-(SETTINGS['map_window_x_size']/2)),
                                        int(target_y-(SETTINGS['map_window_y_size']/2))
                                    )

        if self.camera_x < 0:
            self.camera_x = 0

        if self.camera_y < 0:
            self.camera_y = 0

        if self.camera_x > ((self.cur_map.map_tile_width*SETTINGS['tile_size'])-SETTINGS['map_window_x_size']):
            self.camera_x = ((self.cur_map.map_tile_width*SETTINGS['tile_size'])-SETTINGS['map_window_x_size'])

        if self.camera_y > ((self.cur_map.map_tile_height*SETTINGS['tile_size'])-SETTINGS['map_window_y_size']):
            self.camera_y = ((self.cur_map.map_tile_height*SETTINGS['tile_size'])-SETTINGS['map_window_y_size'])
