import pygame
from services.space import Space
from services.gameloop import GameLoop
from services.menuloop import MenuLoop
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem
from .renderer import Renderer
from .event_queue import EventQueue
from .event_handler import EventHandler
from .clock import Clock

class UI:
    def __init__(self):
        self.__display = pygame.display.set_mode((640, 480))
        self.__event_queue = EventQueue()
        self.__event_handler = EventHandler(self.__event_queue)
        self.__clock = Clock()
        self.__renderer = Renderer(self.__display)
        pygame.init()

    def switch_view(self, view = "menu"):
        services = [self.__event_handler, self.__renderer]
        for service in services:
            if view == "game":
                service.game_view = True
            else:
                service.menu_view = True

    def start_menu(self):
        menu = MenuLoop(self.__renderer, self.__event_handler, self.__clock)
        view = menu.start()
        if not view:
            return
        self.start(view)

    def start_game(self):
        collision_handler = CollisionHandler()
        group_handler = GroupHandler()
        coordinate_system = CoordinateSystem(640,480)
        space = Space(group_handler, collision_handler, coordinate_system)
        game = GameLoop(self.__renderer, space, self.__event_handler, self.__clock)
        stop = game.start()
        self.switch_view()
        return stop

    def start(self, view = "menu"):
        if view == "game":
            self.switch_view(view)
            self.start_game()
        pygame.display.set_caption("Asteroids")
        self.start_menu()
