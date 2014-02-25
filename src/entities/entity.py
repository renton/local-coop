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

    def __init__(
                    self,
                    x,
                    y,
                    w,
                    h,
                    hb_off_x,
                    hb_off_y
                ):

        #debug
        self.debug_color = (100,0,0)

        # state
        self.active = True

        # position
        self.x = x
        self.y = y

        # size #24/34
        self.width = w
        self.height = h

        # hitbox
        self.hb_off_x = hb_off_x
        self.hb_off_y = hb_off_y

        self.hb_w = w - (hb_off_x*2)
        self.hb_h = h - hb_off_y

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
        self.in_air = True
        self.on_wall = False

        # entity type
        self.etype = None

    @property
    def hb_x(self):
        return self.x + self.hb_off_x

    @property
    def hb_y(self):
        return self.y + self.hb_off_y

    def _step(self,cur_map):
        #TODO check out of bounds - set active False if out of map area
        no_wall,new_entities = self._move(cur_map)
        self.ticks += 1
        return (no_wall,new_entities)

    def _move(self,room):

        #TODO - lots to do here. if entity is completey surrounded by blocks it should kill/crush it. also
        # i need to implement CCD for speeds > tile size

        self._feel_gravity()
        self.on_wall = False

        block_entities = []

        if abs(self.dx) < 0.1:
            self.dx = 0

        curx1 = int(self.hb_x / SETTINGS['tile_size'])
        curx2 = int((self.hb_x + self.hb_w - 1) / SETTINGS['tile_size'])

        cury1 = int(self.hb_y / SETTINGS['tile_size'])
        cury2 = int((self.hb_y + self.hb_h - 1) / SETTINGS['tile_size'])

        no_wall = True

        if (room.is_passable(curx1,cury1) == False and
            room.is_passable(curx1,cury2) == False and
            room.is_passable(curx2,cury1) == False and
            room.is_passable(curx2,cury2) == False):
            #TODO handle
            self.x = 100
            self.y = 100
            no_wall = False
        else:
            next_x1 = int((self.hb_x + self.dx) / SETTINGS['tile_size'])
            next_x2 = int((self.hb_x + self.dx + self.hb_w - 1) / SETTINGS['tile_size'])

            next_y1 = int((self.hb_y + self.dy) / SETTINGS['tile_size'])
            next_y2 = int((self.hb_y + self.dy + self.hb_h - 1) / SETTINGS['tile_size'])

            # RIGHT
            if (self.dx > 0):
                if (not room.is_passable(next_x2,cury1)) or (not room.is_passable(next_x2,cury2)):
                    new_hb_x = ((next_x2 * SETTINGS['tile_size']) - self.hb_w)
                    self.x = new_hb_x - self.hb_off_x
                    self.dx = 0
                    no_wall = False
                    self.on_wall = True

                    # damage tiles
                    if(not room.is_passable(next_x2,cury1)):
                        block_entities = room.damage_tile(next_x2,cury1,1)
                    if(not room.is_passable(next_x2,cury2)):
                        block_entities = room.damage_tile(next_x2,cury2,1)

            # LEFT
            elif (self.dx < 0):

                if (not room.is_passable(next_x1,cury1)) or (not room.is_passable(next_x1,cury2)):
                    new_hb_x = next_x2* SETTINGS['tile_size']
                    self.x = new_hb_x - self.hb_off_x
                    self.dx = 0
                    no_wall = False
                    self.on_wall = True

                    # damage tiles
                    if(not room.is_passable(next_x1,cury1)):
                        block_entities = room.damage_tile(next_x1,cury1,1)
                    if(not room.is_passable(next_x1,cury2)):
                        block_entities = room.damage_tile(next_x1,cury2,1)

            # DOWN
            if (self.dy > 0):
               
                if (not room.is_passable(curx1,next_y2)) or (not room.is_passable(curx2,next_y2)):
                    new_hb_y = (next_y2 * SETTINGS['tile_size']) - self.hb_h
                    self.y = new_hb_y - self.hb_off_y
                    self.dy = 0
                    no_wall = False

                    # only call hit ground on first fall - kinda hacky
                    if self.in_air == True:
                        self._hit_ground()

                    # damage tiles
                    if(not room.is_passable(curx1,next_y2)):
                        block_entities = room.damage_tile(curx1,next_y2,1)
                    if(not room.is_passable(curx2,next_y2)):
                        block_entities = room.damage_tile(curx2,next_y2,1)

            # UP
            elif (self.dy < 0):

                if (not room.is_passable(curx1,next_y1)) or (not room.is_passable(curx2,next_y1)):
                    new_hb_y = next_y2 * SETTINGS['tile_size']
                    self.y = new_hb_y - self.hb_off_y
                    self.dy = 0
                    no_wall = False

                    # damage tiles
                    if(not room.is_passable(curx1,next_y1)):
                        block_entities = room.damage_tile(curx1,next_y1,1)
                    if(not room.is_passable(curx2,next_y1)):
                        block_entities = room.damage_tile(curx2,next_y1,1)



        self.x += self.dx
        self.y += self.dy

        #self.dx = 0
        #self.dy = 0

        # TODO return effects and doodads?
        return no_wall, block_entities

    def _feel_gravity(self):
        if self.feels_gravity:
            self.dy += SETTINGS['default_gravity']
            if self.dy > SETTINGS['default_terminal_velocity']:
                self.dy = SETTINGS['default_terminal_velocity']
    

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

    def _hit_ground(self):
        self.in_air = False


class EntityUnit(Entity):
    
    def __init__(self,x,y,w,h,hb_off_x,hb_off_y):
        Entity.__init__(self,x,y,w,h,hb_off_x,hb_off_y)
        self.jump_speed = -10

        # TODO rethink jump cooldown - really we dont need it, we just have to make sure that 
        # player has released button
        # jump cooldowns
        self.jump_cooldown_timer = 0 
        self.jump_cooldown = 10
        self.cur_weapon = None

    def _step(self,cur_map):

        # jump cooldown timer - reset if player touches ground
        if self.in_air == False:
            self.jump_cooldown_timer = 0
        else:
            # decrement while in air
            if self.jump_cooldown_timer > 0:
                self.jump_cooldown_timer -= 1

        # TODO should really hold an array of weapons
        self.cur_weapon._step()

        return Entity._step(self,cur_map)

    def can_jump(self):
        return self.in_air == False and self.jump_cooldown_timer == 0

    def jump(self):
        if self.can_jump() == True:
            self.dy = self.jump_speed
            self._set_jump_cooldown_timer()

    def _set_jump_cooldown_timer(self):
        self.jump_cooldown_timer = self.jump_cooldown
        self.in_air = True

    def _hit_ground(self):
        Entity._hit_ground(self)
        self.jump_cooldown_timer = 0

    # SHOOT
    def shoot(self,target_x,target_y):
        if self.cur_weapon:
            return self.cur_weapon.wshoot(self.x,self.y,target_x,target_y,self.dx,self.dy)
        else:
            return []
