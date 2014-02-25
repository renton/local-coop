from settings import *
from tile import Tile
from random import randint
from entities import Effect

class Map():

    def __init__(self):
        self.map_tile_width = SETTINGS['map_tile_width']
        self.map_tile_height = SETTINGS['map_tile_height']

        self.tiles = {}
        self.bg_tiles = {}
        #self.fg_tiles = {}

        self.tileset_filename = "sample_sprites.png"

        self._gen_sample()

    def _gen_sample(self):
        for i in range(self.map_tile_width):

            if i not in self.tiles:
                self.tiles[i] = {}
                for count in range(10):
                    if count == 9:
                        self.tiles[i][self.map_tile_height-1-count] = Tile(1)
                    else:
                        self.tiles[i][self.map_tile_height-1-count] = Tile(0)

        b_x = 50
        b_y = 11
        b_w = 30
        b_h = 100
        for i in range(b_w):
            for j in range(b_h):
                if i == 0 or i==1 or i == b_w-1 or i == b_w-2:
                    self.tiles[i+b_x][(self.map_tile_height-j)-b_y] = Tile(2)
                else:
                    if randint(0,20) == 0:
                        self.tiles[i+b_x][(self.map_tile_height-j)-b_y] = Tile(2)
                    else:
                        self.tiles[i+b_x][(self.map_tile_height-j)-b_y] = Tile(4)


    def is_passable(self,x,y):
        # handle bg tiles
        return not (x in self.tiles and y in self.tiles[x] and not self.tiles[x][y].passable)

    def damage_tile(self,x,y,damage):
        self.tiles[x][y].take_damage(damage)

        debris_effect = []
        for i in range(randint(1,5)):
            debris_effect.append(
                Effect(
                        x*SETTINGS['tile_size'],
                        y*SETTINGS['tile_size'],
                        20,
                        20,
                        0,
                        0
                        ))

        return debris_effect
