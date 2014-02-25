from ..weapon import Weapon
from ..settings import *
from entity import EntityUnit

class ActionPlayer(EntityUnit):

    def __init__(
                    self,
                    primary_w='revolver',
                    secondary_w='sniper'
                    ):

        EntityUnit.__init__(self,100,100,14,15,0,0)

        self.etype = "p1"
        self.speed = 10
        self.djump_speed = -16
        self.wjump_speed = -16
        self.jump_speed = -16

        p_weapon_params = []
        s_weapon_params = []
        for param in SETTINGS['w_param_order']:
            p_weapon_params.append(SETTINGS['primary_weapons'][primary_w][param])
            s_weapon_params.append(SETTINGS['secondary_weapons'][secondary_w][param])

        self.p_weapon = Weapon(*p_weapon_params)
        self.s_weapon = Weapon(*s_weapon_params)

        self.cur_weapon = self.p_weapon

        self.double_jump_ready = True
        self.air_ticks = 0

    def _step(self,cur_map):

        if self.in_air:
            self.air_ticks += 1
        else:
            self.air_ticks = 0

        #TODO should really be an array of weapons handled by entityunit
        self.p_weapon._step()
        self.s_weapon._step()

        # TODO
        if self.dx < 20:
            self.dx *= 0.8

        (no_wall,new_entities) = EntityUnit._step(self,cur_map)

        return (True,new_entities)

    def fire_primary(self,target_x,target_y):
        # takes in raw input from analog, so needs multiplier and cur x,y
        self.cur_weapon = self.p_weapon

        # get vector of length 1
        projs = self.shoot(
                            self.x+(target_x/abs(target_x+target_y))*100,
                            self.y+(target_y/abs(target_x+target_y))*100
                        )

        return projs

    def fire_secondary(self,target_x,target_y):
        # takes in raw input from analog, so needs multiplier and cur x,y
        self.cur_weapon = self.s_weapon

        # get vector of length 1
        projs = self.shoot(
                            self.x+(target_x/(target_x+target_y))*100,
                            self.y+(target_y/(target_x+target_y))*100
                        )

        # TODO this should be based off fixed speed, not variable
        if projs:
            self.dx = (target_x*100)*-1
            self.dy = (target_y*100)*-1

        return projs

    # JUMPING

    def can_wall_jump(self):
        return (self.in_air and self.on_wall and self.jump_cooldown_timer == 0)

    def can_double_jump(self):
        return (self.in_air and self.double_jump_ready and self.jump_cooldown_timer == 0)

    def jump(self):
        EntityUnit.jump(self)

        if self.can_wall_jump() == True:
            self.dy = self.wjump_speed
            self.double_jump_ready = True
            self._set_jump_cooldown_timer()

        if self.can_double_jump() == True:
            self.dy = self.djump_speed
            self.double_jump_ready = False
            self._set_jump_cooldown_timer()

    def _hit_ground(self):
        EntityUnit._hit_ground(self)
        self.double_jump_ready = True
