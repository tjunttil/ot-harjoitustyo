import pygame

class Renderer:
    """Class to render objects in space to pygame display

    Attributes:
        display: the display to render to
        space: the space holding the objects to render
    """
    def __init__(self, display, space):
        self.__display = display
        self.__space = space

    def draw(self, points, game_over = False):
        self.__display.fill((0, 0, 0))
        self.__space.all_entities.draw(self.__display)
        if not game_over:
            font = pygame.font.SysFont("Arial", 20)
            point_text = font.render(f"Points: {points}", True, (255,255,255))
            self.__display.blit(point_text, (0,0))
        else:
            font = pygame.font.SysFont("Arial", 40)
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            points_text = font.render(f"POINTS: {points}", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center = (320, 200))
            points_rect = points_text.get_rect(center = (320, 240))
            self.__display.blit(game_over_text, game_over_rect)
            self.__display.blit(points_text, points_rect)
        pygame.display.update()
