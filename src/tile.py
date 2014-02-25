class Tile():

    def __init__(self,sprite_id):
        self.active = True
        self.passable = False
        self.background = False

        self.sprite_id = sprite_id
        self.hp = 100

        #hack
        if self.sprite_id == 4:
            self.passable = True

    def take_damage(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.active = False
