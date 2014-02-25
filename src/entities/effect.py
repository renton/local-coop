from entity import Entity

# effects act like normal entities, but do not experience collision detection
class Effect(Entity):

    def __init__(self,x,y,w,h,dx,dy):

        Entity.__init__(self,x,y,w,h,0,0)
        self.dx = dx
        self.dy = dy
        self.debug_color = (0,100,0)
        self.feels_gravity = False

    def _step(self,room):
        self._feel_gravity()
        self.x += self.dx
        self.y += self.dy
        return (True,[])
