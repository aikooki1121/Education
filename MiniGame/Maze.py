import json
from json import JSONEncoder
import numpy
import pygame as pg
from Hero import Hero

maze_path = 'C:/Education/MiniGame/Maze/Random/random.json'


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class Maze(object):
    """

    """

    def __init__(self):
        self.maze = []
        self.myHero = Hero(x=1, y=1)

    def maze_save(self, maze_random_value):
        print("all right")

        with open(maze_path, 'r') as f:
            template = json.load(f)
            template["Maze_random"] = maze_random_value

        with open(maze_path, 'w') as ff:

            ff.seek(0)
            ff.write(json.dumps(template, cls=NumpyArrayEncoder, indent=4, sort_keys=True))
        self.maze = maze_random_value

    def hero_interaction(self, key):  # todo ТОЛЬКО логика взаимодейтсвия
        """Логика взаимодейтсвия героя с объектами в лабиринте"""
        if key == pg.K_d:
            if self.maze[self.myHero.y][self.myHero.x + 1] != 1:
                self.myHero.move_position(dx=1, dy=0)
        if key == pg.K_a:
            if self.maze[self.myHero.y][self.myHero.x - 1] != 1:
                self.myHero.move_position(dx=-1, dy=0)
        if key == pg.K_s:
            if self.maze[self.myHero.y + 1][self.myHero.x] != 1:
                self.myHero.move_position(dx=0, dy=1)
        if key == pg.K_w:
            if self.maze[self.myHero.y - 1][self.myHero.x] != 1:
                self.myHero.move_position(dx=0, dy=-1)

















