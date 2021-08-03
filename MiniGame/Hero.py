from henloEngine import PlayerObject


class Hero(object):
    CONST_MAP_SCALE = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heroDrawer = PlayerObject()
        self.heroDrawer.z = 1
        self.heroDrawer.set_position(x*self.CONST_MAP_SCALE + 10, y*self.CONST_MAP_SCALE + 10)  # todo подумать тот ли это "x" и "y"
        self.heroDrawer.radius = 7
        self.heroDrawer.color = (50, 178, 255)

    def move_position(self, dx, dy):  # todo ТОЛЬКО изменение позиции
        self.x += dx
        self.y += dy
        self.heroDrawer.set_position(self.x * self.CONST_MAP_SCALE + 10, self.y * self.CONST_MAP_SCALE + 10)

