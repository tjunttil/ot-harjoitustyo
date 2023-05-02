import pygame
from services.space import Space
from services.gameloop import GameLoop
#from services.menuloop import MenuLoop
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

    def toggle_game_view(self):
        services = [self.__event_handler, self.__renderer]
        for service in services:
            service.game_view = not service.game_view

    def start_menu(self):
        #menu = MenuLoop(self.__renderer, self.__event_handler, self.__clock)
        #menu.start()
        running = True
        self.__renderer.draw()
        while running:
            commands_list = self.__event_handler.handle_events()
            for commands in commands_list:
                running = not commands["quit"]
                if commands["start game"]:
                    self.toggle_game_view()
                    self.start_game()
                    self.toggle_game_view()
                    running = False
                #if commands["score list"]:
                #    pass
                    #self.start_score_view()
            self.__clock.tick(60)

    def start_game(self):
        collision_handler = CollisionHandler()
        group_handler = GroupHandler()
        coordinate_system = CoordinateSystem(640,480)
        space = Space(group_handler, collision_handler, coordinate_system)
        game = GameLoop(self.__renderer, space, self.__event_handler, self.__clock)
        game.start()

    def start(self):
        pygame.display.set_caption("Asteroids")
        self.start_menu()
