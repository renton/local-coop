class Tile():

    def __init__(self,sprite_id):
        self.passable = False
        self.background = False
        self.sprite_id = sprite_id

        #hack
        if self.sprite_id == 4:
            self.passable = True
