import pygame as pg
from abc import abstractmethod


class GameObject:
    window = None

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def set_window(self, surface: pg.Surface):
        self.window = surface

    @abstractmethod
    def draw(self):
        pass


class UpdatableObjectInterface(object):
    @abstractmethod
    def update(self, time: float):
        pass


class KeyboardInterface(object):
    def key_up(self, key):
        pass

    def key_down(self, key):
        pass


class UpdatableObject(GameObject, UpdatableObjectInterface):
    def __init__(self):
        super().__init__()

    def draw(self):
        pass

    def update(self, time: float):
        pass


class PlayerObject(UpdatableObject, KeyboardInterface):
    def __init__(self):
        super().__init__()
        self.animating = False
        self.color = (255, 255, 255)
        self.radius = 10
        self.herodraw = MobSprite(x_sprite=self.x, y_sprite=self.y, filename='v1.1 dungeon crawler 16x16 pixel pack/heroes/knight/knight_idle_anim_f0.png')
        self.anim_vector_x = 0.0
        self.anim_vector_y = 0.0
        self.xf = 0.0
        self.yf = 0.0
        self.anim_timer = 0.0
        self.move_anim_time = 0.3

    def move_to_new_position(self, x, y):
        self.animating = True
        self.anim_timer = 0.0
        self.xf = float(self.x)
        self.yf = float(self.y)
        self.anim_vector_x = (x - self.x) / self.move_anim_time
        self.anim_vector_y = (y - self.y) / self.move_anim_time
        self.set_position(self.x, self.y)

    def update(self, time: float):
        if self.animating:
            self.anim_timer += time
            if self.anim_timer >= self.move_anim_time:
                self.anim_timer = 0.0
                self.animating = False
            else:
                self.xf += self.anim_vector_x * time
                self.yf += self.anim_vector_y * time
                self.set_position(int(self.xf), int(self.yf))

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.herodraw.rect.x = self.x
        self.herodraw.rect.y = self.y

    def move_position(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        self.window.blit(self.herodraw.image, self.herodraw.rect)
        # temp_surf = self.window.copy()
        # self.window.fill((0, 0, 0))
        # pg.draw.circle(self.window, self.color, (self.x, self.y), self.radius)

        # self.window.blit(temp_surf, (-self.herodraw.rect.x+240, -self.herodraw.rect.y+240))

class MapTile(GameObject):
    width = height = 80  # default size of tile
    __color = (255, 255, 255)

    def __init__(self, surface: pg.Surface, a_id, a_type):
        super().__init__()
        self.set_window(surface)
        self.tileId = a_id
        self.tileType = a_type
        if a_type == 1:
            self.__color = (90, 90, 90)
        elif a_type == 2:
            self.__color = (200, 120, 120)

    def set_coord(self, x, y):
        self.x = x * self.width
        self.y = y * self.height

    def draw(self):
        pg.draw.rect(self.window, self.__color, (self.x, self.y, self.width, self.height))


class GameMap(GameObject):

    def __init__(self, surface: pg.Surface):
        super().__init__()
        self.set_window(surface)
        self.tilesMap = []

    def load_maze(self, game_map):
        i = 0
        ix = iy = 0
        self.tilesMap.clear()
        for a in game_map:
            ix = 0
            for tile_type in a:
                tmp_tile = MapTile(self.window, i, tile_type)
                tmp_tile.set_coord(ix, iy)
                self.tilesMap.append(tmp_tile)
                i += 1
                ix += 1
            iy += 1

    def draw(self):  # todo отрисовка карты, старый вариант
        for tile in self.tilesMap:
            tile.draw()


class Game:
    objects = []  # list of  'GameObject's
    keyboardListeners = []

    def __init__(self):
        self.objects.clear()
        self.keyboardListeners.clear()
        pass


class MobSprite(pg.sprite.Sprite):  # todo класс отрисовки спрайтов
    def __init__(self, x_sprite: int, y_sprite: int, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(
            filename).convert_alpha(), (pg.image.load(
            filename).convert_alpha().get_width()*5, pg.image.load(
            filename).convert_alpha().get_height()*5))
        print(self.image.get_height(), self.image.get_width())
        self.rect = self.image.get_rect(
            center=(x_sprite, y_sprite))

    # def update(self):  # todo изменить движение спрайта
    #     if self.rect.y < H:
    #         self.rect.y += 2
    #     else:
    #         self.rect.y = 0


class Engine(object):
    __GAME_WIN_WIDTH = 560
    __GAME_WIN_HEIGHT = 560
    __FPS = 60

    def __init__(self, game_width=560, game_height=560):
        pg.init()
        self.__GAME_WIN_WIDTH = game_width
        self.__GAME_WIN_HEIGHT = game_height
        self.win = pg.display.set_mode((self.__GAME_WIN_WIDTH, self.__GAME_WIN_HEIGHT))
        pg.display.set_caption("Название игры")
        self.framePerSec = pg.time.Clock()

        self.game_client = Game()
        self.game_client.objects.clear()

    def start_game(self):
        run = True
        while (run):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.KEYDOWN:
                    for obj in self.game_client.keyboardListeners:
                        if isinstance(obj, KeyboardInterface):
                            obj.key_down(event.key)
                if event.type == pg.KEYUP:
                    for obj in self.game_client.keyboardListeners:
                        if isinstance(obj, KeyboardInterface):
                            obj.key_up(event.key)
                # key up keyboard

            self.win.fill((0, 0, 0))

            for obj in self.game_client.objects:
                if isinstance(obj, UpdatableObjectInterface):
                    obj.update(self.framePerSec.get_time() / 1000.0)
            for obj in self.game_client.objects:
                if isinstance(obj, GameObject):
                    obj.draw()

            pg.display.update()
            self.framePerSec.tick(self.__FPS)

        pg.quit()

    def append_game_object(self, obj: GameObject, set_win=False, to_sort=True):
        if set_win:
            obj.set_window(self.win)
        self.game_client.objects.append(obj)
        if to_sort:
            self.game_client.objects.sort(key=lambda o: o.z, reverse=False)

    def append_keyboard_listener(self, obj: KeyboardInterface):
        self.game_client.keyboardListeners.append(obj)

    def load_game(self, maze_map):
        g_map = GameMap(self.win)
        g_map.load_maze(maze_map)
        self.append_game_object(g_map)

