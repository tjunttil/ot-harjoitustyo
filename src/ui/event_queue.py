import pygame

class EventQueue:
    def __init__(self):
        self.service = pygame.event

    def get(self):
        return self.service.get()
