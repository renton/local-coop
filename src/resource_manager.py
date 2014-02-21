from settings import *
import pygame

class ResourceManager():

    def __init__(self):
        self.tilesets = {}

    def load_tileset(self,filename):
        self.tilesets[filename] = {}

        image = pygame.image.load(SETTINGS['asset_tileset_path']+filename).convert()
        image_width,image_height = image.get_size()

        col = 0
        for tile_x in range(0,image_width/SETTINGS['tile_size']):
            for tile_y in range(0,image_height/SETTINGS['tile_size']):
                rect = (
                    tile_x*SETTINGS['tile_size'],
                    tile_y*SETTINGS['tile_size'],
                    SETTINGS['tile_size'],
                    SETTINGS['tile_size']
                )

                self.tilesets[filename][col] = pygame.transform.scale(
                                                                        image.subsurface(rect),
                                                                        (SETTINGS['tile_size']*SETTINGS['scale'],
                                                                        SETTINGS['tile_size']*SETTINGS['scale'])
                                                                    )
                col+=1
        print "tileset loaded"
 

    def unload_tileset(self,filename):
        if filename in self.tilesets:
            del self.tilesets[filename]
