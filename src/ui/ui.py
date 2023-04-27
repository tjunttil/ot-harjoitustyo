import pygame
from entities.space import Space
from gameloop import GameLoop
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem
from .renderer import Renderer
from .event_queue import EventQueue
from .event_handler import EventHandler
from .clock import Clock

class UI:
    def __init__(self):
        self.display = pygame.display.set_mode((640, 480))
        self.event_queue = EventQueue()
        self.event_handler = EventHandler()
        self.clock = Clock()

    def start(self):
        collision_handler = CollisionHandler()
        group_handler = GroupHandler()
        coordinate_system = CoordinateSystem(640,480)
        space = Space(1, group_handler, collision_handler, coordinate_system)
        renderer = Renderer(self.display, space)
        game = GameLoop(renderer, space, self.event_handler, self.event_queue, self.clock)
        pygame.init()
        pygame.display.set_caption("Asteroids")
        game.start()
