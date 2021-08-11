from henloEngine import PlayerObject
import pygame as pg

hero_sprite = 'v1.1 dungeon crawler 16x16 pixel pack/heroes/knight/knight_idle_anim_f0.png'


class Hero(object):
    CONST_MAP_SCALE = 80

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heroDrawer = PlayerObject()
        self.heroDrawer.z = 1
        self.heroDrawer.set_position(x*self.CONST_MAP_SCALE, y*self.CONST_MAP_SCALE)  # todo подумать тот ли это "x" и "y"
        self.heroDrawer.radius = 7
        self.heroDrawer.color = (50, 178, 255)

    def move_position(self, dx, dy):  # todo ТОЛЬКО изменение позиции
        self.x += dx
        self.y += dy
        self.heroDrawer.move_to_new_position(self.x * self.CONST_MAP_SCALE, self.y * self.CONST_MAP_SCALE)

    def can_move(self):
        return not self.heroDrawer.animating
