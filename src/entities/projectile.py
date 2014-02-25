from entity import Entity

class Projectile(Entity):

    # if crit is decided before shooting, then maybe the projectile can look different if its a critical shot

    def __init__(
                    self,
                    x,
                    y,
                    dx,
                    dy,
                    h,
                    w,
                    bullet_life,
                    damage,
                    etype
                ):

        Entity.__init__(self,x,y,w,h,0,0)

        self.dx = dx
        self.dy = dy
        self.bullet_life = bullet_life
        self.damage = damage
        self.etype = etype

        self.is_bouncy = False

        # TODO for all types?
        self.feels_gravity = False

    def _step(self,room):
        (is_active,new_entities) = Entity._step(self,room)

        if self.ticks > self.bullet_life:
            self.impact()
            is_active = False

        if not is_active:
            self.is_active = False

        return (is_active,new_entities)

    def impact(self):
        #TODO handle bouncing
        self.active = False
