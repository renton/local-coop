from entities.projectile import Projectile
from random import randint,randrange
import math

class Weapon():

    # TODO - knockback, player knockback

    def __init__(
                    self,
                    min_dmg,
                    max_dmg,
                    bullet_life,
                    speed,
                    accuracy,
                    num_projs,
                    firerate,
                    reload_time,
                    clip_size,
                    crit_chance,
                    etype
                ):

        self.damage = (min_dmg,max_dmg)    #min/max
        self.bullet_life = bullet_life
        self.speed = speed
        self.accuracy = accuracy
        self.num_projectiles = num_projs
        self.firerate = firerate
        self.reload_time = reload_time
        self.clip_size = clip_size
        self.crit_chance = crit_chance

        self.proj_width = 5
        self.proj_height = 5

        self.cur_clip = self.clip_size
        self.firerate_cooldown_timer = 0
        self.reload_cooldown_timer = 0
        self.etype = etype

    def _step(self):

        if self.firerate_cooldown_timer > 0:
            self.firerate_cooldown_timer -= 1

        if self.reload_cooldown_timer > 0:
            self.reload_cooldown_timer -= 1
            if self.reload_cooldown_timer <= 0:
                self.cur_clip = self.clip_size

    def can_shoot(self):
        return self.firerate_cooldown_timer == 0 and self.reload_cooldown_timer == 0 and self.cur_clip > 0

    def wshoot(self,x,y,target_x,target_y):

        projs = []

        if self.can_shoot():

            orig_target_x,orig_target_y = target_x,target_y

            for i in range(self.num_projectiles):
                dx,dy = 0,0

                if self.accuracy != 0:
                    target_x = randrange(int(orig_target_x-self.accuracy),int(orig_target_x+self.accuracy))
                    target_y = randrange(int(orig_target_y-self.accuracy),int(orig_target_y+self.accuracy))
                else:
                    target_x = orig_target_x
                    target_y = orig_target_y

                adj_large = target_x - x
                opp_large = target_y - y
                hyp_large = math.sqrt(math.pow(opp_large,2) + math.pow(adj_large,2))

                if hyp_large == 0:
                    dx = 0
                    dy = self.speed * -1
                else:
                    dx = (adj_large/hyp_large) * self.speed
                    dy = (opp_large/hyp_large) * self.speed

                print dx,dy

                #TODO if crit shot, change dmg
                projs.append(Projectile(x,y,dx,dy,self.proj_width,self.proj_height,self.bullet_life,randint(*self.damage),self.etype))

            self.cur_clip -= 1
            if self.cur_clip <= 0:
                self.reload_cooldown_timer = self.reload_time

            self.firerate_cooldown_timer = self.firerate

            return projs
        else:
            return projs
