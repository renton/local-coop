from settings import *
from tile import Tile
from random import randint

class Map():

    def __init__(self):
        self.map_tile_width = SETTINGS['map_tile_width']
        self.map_tile_height = SETTINGS['map_tile_height']

        self.tiles = {}
        self.bg_tiles = {}
        #self.fg_tiles = {}

        self.tileset_filename = "sample.png"

        self._gen_sample()

    def _gen_sample(self):
        for i in range(self.map_tile_width):

            if i not in self.tiles:
                self.tiles[i] = {}
                self.tiles[i][0] = Tile()
                for count in range(10):
                    self.tiles[i][self.map_tile_height-1-count] = Tile()

                for j in range(self.map_tile_height):
                    if randint(0,100) == 0:
                        self.tiles[i][j] = Tile()

                if i == 0 or i == (self.map_tile_width-1):
                    for j in range(self.map_tile_height):
                        self.tiles[i][j] = Tile()

    def is_passable(self,x,y):
        # handle bg tiles
        return not (x in self.tiles and y in self.tiles[x])
