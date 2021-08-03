from Maze_generator import MazeGenerator
from henloEngine import Engine
from henloEngine import KeyboardInterface
from Maze import Maze


class GameScene(KeyboardInterface):
    """

    """

    def __init__(self):
        self.myMaze = Maze()
        self.eng = Engine()

    def load(self):
        x = int(input('высота:\t'))
        y = int(input('ширина:\t'))
        generator = MazeGenerator(x, y)

        maze = generator.generate()
        print(maze)

        self.myMaze.maze_save(maze)

    def inition(self):
        self.eng.load_game(self.myMaze.maze)
        self.eng.append_keyboard_listener(self)
        self.eng.append_game_object(self.myMaze.myHero.heroDrawer, set_win=True)

    def run_game(self):
        self.eng.start_game()

    def key_up(self, key):
        self.myMaze.hero_interaction(key)  # todo имя переменной от логики прописанной в в мэйз

    def key_down(self, key):
        pass
