import pygame
from entities.space import Space
from gameloop import GameLoop
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
        space = Space(1)
        renderer = Renderer(self.display, space)
        game = GameLoop(renderer, space, self.event_handler, self.event_queue, self.clock)
        pygame.init()
        game.start()
