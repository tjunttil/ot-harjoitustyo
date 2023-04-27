import pygame

class GroupHandler:
    def group(self):
        return pygame.sprite.Group()

    def add(self,element, group):
        group.add(element)

    def elements(self, group):
        return group.sprites()
