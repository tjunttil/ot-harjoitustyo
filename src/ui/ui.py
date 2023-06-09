import pygame
from services.space import Space
from services.gameloop import GameLoop
from services.menuloop import MenuLoop
from services.gameoverloop import GameOverLoop
from services.scorelistloop import ScoreListLoop
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem
from repositories.point_repository import PointRepository
from .renderer import Renderer
from .event_queue import EventQueue
from .event_handler import EventHandler
from .clock import Clock

class UI:
    def __init__(self):
        pygame.init()
        self.__display = pygame.display.set_mode((640, 480))
        self.__event_queue = EventQueue()
        self.__event_handler = EventHandler(self.__event_queue)
        self.__clock = Clock()
        self.__renderer = Renderer(self.__display)
        self.__point_repository = PointRepository()
        pygame.display.set_caption("Asteroids")

    def switch_view(self, view = 0):
        services = [self.__event_handler, self.__renderer]
        for service in services:
            if view == "game":
                service.game_view = True
            if view == "game over":
                service.game_over_view = True
            if view == "menu":
                service.menu_view = True
            if view == "score list":
                service.score_list_view = True

    def __start_menu(self):
        menu = MenuLoop(self.__renderer, self.__event_handler, self.__clock)
        return menu.start()

    def __start_game(self):
        collision_handler = CollisionHandler()
        group_handler = GroupHandler()
        coordinate_system = CoordinateSystem(640,480)
        space = Space(group_handler, collision_handler, coordinate_system)
        game = GameLoop(self.__renderer, space, self.__event_handler, self.__clock)
        return game.start()

    def __start_game_over(self, points, space):
        game_over = GameOverLoop(self.__renderer, self.__event_handler,
        self.__clock, points, space, self.__point_repository)
        return game_over.start()

    def __start_score_list(self):
        score_list = ScoreListLoop(self.__renderer, self.__point_repository,
        self.__event_handler, self.__clock)
        return score_list.start()

    def start(self, view, *args):
        """A master loop for starting and switching between loops

        Args:
            view ([type]): [description]
        """
        starters = [("game", self.__start_game), ("menu", self.__start_menu),
        ("game over", self.__start_game_over), ("score list", self.__start_score_list)]
        if isinstance(view, bool) and not view:
            return
        for starter in starters:
            key, value = starter
            if view == key:
                self.switch_view(view)
                params = value(*args)
                rest = []
                if len(params) > 1:
                    rest = params[1:]
                view = params[0]
                self.start(view, *rest)
                break
