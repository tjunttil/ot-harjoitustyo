import pygame

class Renderer:
    def __init__(self, display, space):
        self.__display = display
        self.__space = space

    def draw(self):
        self.__display.fill((0, 0, 0))
        self.__space.all_sprites.draw(self.__display)
        #TESTING
        #for p in self.space.ship.collide_points:
        #    pygame.draw.circle(self.display, (255,0,0), (p[0], p[1]), 5)
        pygame.display.update()
