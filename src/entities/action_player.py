from ..weapon import Weapon
from entity import EntityUnit

class ActionPlayer(EntityUnit):

    def __init__(self):
        EntityUnit.__init__(self)
        self.speed = 10
        self.djump_speed = -10
        self.wjump_speed = -10

        self.p_weapon = Weapon()
        self.s_weapon = Weapon()

        self.double_jump_ready = True
        self.air_ticks = 0

    def _step(self,cur_map):

        if self.in_air:
            self.air_ticks += 1
        else:
            self.air_ticks = 0

        EntityUnit._step(self,cur_map)

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
