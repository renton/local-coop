from ..settings import *
# effects
# debris
# collision debris
# projectiles
# titans
# player
# ai units
# enemy units

class Entity():

    def __init__(self):

        # state
        self.active = True

        # position
        self.x = 10
        self.y = 10

        # size
        self.width = 10
        self.height = 10

        # hitbox
        self.hb_off_x = 0
        self.hb_off_y = 0

        self.hb_width = self.width
        self.hb_height = self.height

        # weight
        self.weight = 10

        # speed
        self.dx = 0
        self.dy = 0
        self.ddx = 0
        self.ddy = 0

        # ticks
        self.ticks = 0

        # gravity
        self.feels_gravity = True

    @property
    def hb_x(self):
        return self.x + self.hb_off_x

    @property
    def hb_y(self):
        return self.y + self.hb_off_y

    def _step(self):
        self._move()
        self.ticks += 1

    def _move(self):

        '''
        curx1 = int(self.hb_x / SETTINGS['tile_size'])
        curx2 = int((self.hb_x + self.hb_w - 1) / SETTINGS['tile_size'])

        cury1 = int(self.hb_y / SETTINGS['tile_size'])
        cury2 = int((self.hb_y + self.hb_h - 1) / SETTINGS['tile_size'])

        no_wall = True

        if (room.tiles[cury1][curx1].walkable == False and
            room.tiles[cury1][curx2].walkable == False and
            room.tiles[cury2][curx1].walkable == False and
            room.tiles[cury2][curx2].walkable == False):
            #TODO handle
            no_wall = False
        else:

            next_x1 = int((self.hb_x + self.dx) / SETTINGS['t_tile_size'])
            next_x2 = int((self.hb_x + self.dx + self.hb_w - 1) / SETTINGS['t_tile_size'])

            next_y1 = int((self.hb_y + self.dy) / SETTINGS['t_tile_size'])
            next_y2 = int((self.hb_y + self.dy + self.hb_h - 1) / SETTINGS['t_tile_size'])

            # RIGHT
            if (self.dx > 0):

                if ((room.tiles[cury1][next_x2].walkable == False) or (room.tiles[cury2][next_x2].walkable == False)):

                    new_hb_x = ((next_x2 * SETTINGS['t_tile_size']) - self.hb_w)
                    self.x = new_hb_x - self.hb_off_x
                    self.dx = 0
                    no_wall = False

            # LEFT
            elif (self.dx < 0):

                if ((room.tiles[cury1][next_x1].walkable == False) or (room.tiles[cury2][next_x1].walkable == False)):

                    new_hb_x = next_x2* SETTINGS['t_tile_size']
                    self.x = new_hb_x - self.hb_off_x
                    self.dx = 0
                    no_wall = False

            # DOWN
            if (self.dy > 0):
               
                if ((room.tiles[next_y2][curx1].walkable == False) or (room.tiles[next_y2][curx2].walkable == False)):

                    new_hb_y = (next_y2 * SETTINGS['t_tile_size']) - self.hb_h
                    self.y = new_hb_y - self.hb_off_y
                    self.dy = 0
                    no_wall = False

            # UP
            elif (self.dy < 0):

                if ((room.tiles[next_y1][curx1].walkable == False) or (room.tiles[next_y1][curx2].walkable == False)):

                    new_hb_y = next_y2 * SETTINGS['t_tile_size']
                    self.y = new_hb_y - self.hb_off_y
                    self.dy = 0
                    no_wall = False
        '''
        self.x += self.dx
        self.y += self.dy
        #self.dx *= 0.9
        #self.dy *= 0.9
        self.dx = 0
        self.dy = 0
        #return no_wall

    def check_collision_crude(self,entity):

        if (self.active and entity.active):
            b1_topleft_x = self.hb_x;
            b1_topleft_y = self.hb_y;

            b1_bottomright_x = self.hb_x + self.hb_w;
            b1_bottomright_y = self.hb_y - self.hb_h;

            b2_topleft_x = entity.hb_x;
            b2_topleft_y = entity.hb_y;

            b2_bottomright_x = entity.hb_x + entity.hb_w;
            b2_bottomright_y = entity.hb_y - entity.hb_h; 

            if (
                ((
                    (b1_topleft_x < b2_topleft_x and b1_bottomright_x > b2_topleft_x) or
                    (b1_topleft_x < b2_bottomright_x and b1_bottomright_x > b2_bottomright_x)
                ) and
                (
                    (b1_topleft_y > b2_topleft_y and b1_bottomright_y < b2_topleft_y) or
                    (b1_topleft_y > b2_bottomright_y and b1_bottomright_y < b2_bottomright_y)
                )) or
                ((
                    (b2_topleft_x < b1_topleft_x and b2_bottomright_x > b1_topleft_x) or
                    (b2_topleft_x < b1_bottomright_x and b2_bottomright_x > b1_bottomright_x)
                ) and
                (
                    (b2_topleft_y > b1_topleft_y and b2_bottomright_y < b1_topleft_y) or
                    (b2_topleft_y > b1_bottomright_y and b2_bottomright_y < b1_bottomright_y)
                ))
            ):
                return True
            else:
                return False


class EntityUnit(Entity):
    
    def __init__(self):
        Entity.__init__(self)
