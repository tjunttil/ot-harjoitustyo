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
        pygame.display.set_caption("Asteroids")

    def switch_view(self, view = "menu"):
        services = [self.__event_handler, self.__renderer]
        for service in services:
            if view == "game":
                service.game_view = True
            if view == "game over":
                service.game_over_view = True
            if view == "menu":
                service.menu_view = True

    def __start_menu(self):
        menu = MenuLoop(self.__renderer, self.__event_handler, self.__clock)
        print("starting menu")
        return menu.start()

    def __start_game(self):
        collision_handler = CollisionHandler()
        group_handler = GroupHandler()
        coordinate_system = CoordinateSystem(640,480)
        space = Space(group_handler, collision_handler, coordinate_system)
        game = GameLoop(self.__renderer, space, self.__event_handler, self.__clock)
        print("starting game")
        return game.start()

    def __start_game_over(self):
        print("starting game over")
        return False

    def start(self, view = "menu"):
        print("starting...")
        starters = [("game", self.__start_game), ("menu", self.__start_menu),
        ("game over", self.__start_game_over)]
        if not view:
            print("goodbye!")
            return
        for starter in starters:
            key, value = starter
            if view == key:
                print(f"current view:{view}")
                self.switch_view(view)
                print(f"starting {view}")
                view = value()
                print(f"switching now to {view}")
                self.start(view)
        # if view == "game":
        #     self.switch_view(view)
        #     self.start_game()
        # if view == "game over":
        #     self.switch_view(view)
        #     self.start_game_over()
        # if view == "menu":         
        #     self.start_menu()
