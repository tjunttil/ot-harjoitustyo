import pygame
from entities.space import Space
from gameloop import GameLoop
from ui.renderer import Renderer
from ui.event_queue import EventQueue
from ui.event_handler import EventHandler
from ui.clock import Clock

def main():
    display = pygame.display.set_mode((640, 480))
    space = Space(1)
    renderer = Renderer(display, space)
    event_queue = EventQueue()
    event_handler = EventHandler()
    clock = Clock()
    pygame.init()
    game = GameLoop(renderer, space, event_handler, event_queue, clock)
    game.start()

if __name__ == "__main__":
    main()
