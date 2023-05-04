import pygame
from .ui_service import UIService

class Renderer(UIService):
    """Class to render objects in space to pygame display

    Attributes:
        display: the display to render to
    """
    def __init__(self, display):
        super().__init__()
        self.__display = display

    def draw_game_view(self, points, space):
        space.all_entities.draw(self.__display)
        font = pygame.font.SysFont("Arial", 20)
        point_text = font.render(f"Points: {points}", True, (255,255,255))
        self.__display.blit(point_text, (0,0))

    def draw_game_over_view(self, points, space):
        space.all_entities.draw(self.__display)
        font = pygame.font.SysFont("Arial", 40)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        points_text = font.render(f"POINTS: {points}", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center = (320, 200))
        points_rect = points_text.get_rect(center = (320, 240))
        self.__display.blit(game_over_text, game_over_rect)
        self.__display.blit(points_text, points_rect)

    def draw_menu_view(self):
        title_font = pygame.font.SysFont("Arial", 60)
        title_text = title_font.render("ASTEROIDS", True, (255, 255, 255))
        item_font = pygame.font.SysFont("Arial", 35)
        start_new_game_text = item_font.render("Press Return for new game", True, (255, 255, 255))
        title_rect = title_text.get_rect(center = (320, 200))
        start_rect = start_new_game_text.get_rect(center = (320, 260))
        self.__display.blit(title_text, title_rect)
        self.__display.blit(start_new_game_text, start_rect)

    def draw(self, points = 0, space = None):
        self.__display.fill((0,0,0))
        if self.game_view:
            self.draw_game_view(points, space)
        if self.game_over_view:
            self.draw_game_over_view(points, space)
        if self.menu_view:
            self.draw_menu_view()
        pygame.display.update()
