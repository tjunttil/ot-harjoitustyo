import pygame
from .ui_service import UIService

class Renderer(UIService):
    """Class to render objects in space to pygame display

    Attributes:
        display: the display to render to
        title_font: the font object used for titles
        item_font: the font object used for menu items
        game_font: the font object used for the game user interface
    """
    def __init__(self, display):
        super().__init__()
        self.__display = display
        self.title_font = pygame.font.SysFont("Arial", 60)
        self.item_font = pygame.font.SysFont("Arial", 35)
        self.game_font = pygame.font.SysFont("Arial", 20)

    def __draw_game_view(self, points, space):
        space.all_entities.draw(self.__display)
        point_text = self.game_font.render(f"Points: {points}", True, (255,255,255))
        return [(point_text,(0,0))]

    def __draw_game_over_view(self, points, space, username):
        space.all_entities.draw(self.__display)
        texts = []
        contents = []
        texts.append(self.title_font.render("GAME OVER", True, (255, 0, 0)))
        texts.append(self.item_font.render(f"POINTS: {points}", True, (255, 0, 0)))
        texts.append(self.item_font.render(
            "Enter username to save score:", True, (255, 255, 255)))
        texts.append(self.item_font.render(f"{username}", True, (255,0,0)))
        for i in range(4):
            contents.append((texts[i], texts[i].get_rect(center = (320, 160 + 50*i))))
        # game_over_rect = game_over_text.get_rect(center = (320, 160))
        # points_rect = points_text.get_rect(center = (320, 210))
        # directions_rect = directions_text.get_rect(center = (320,260))
        # username_rect = username_text.get
        return contents

    def __draw_menu_view(self):
        title_text = self.title_font.render("ASTEROIDS", True, (255, 255, 255))
        start_new_game_text = self.item_font.render(
            "Press Return for new game", True, (255, 255, 255))
        title_rect = title_text.get_rect(center = (320, 200))
        start_rect = start_new_game_text.get_rect(center = (320, 260))
        return [(title_text,title_rect), (start_new_game_text,start_rect)]

    def draw(self, *args):
        self.__display.fill((0,0,0))
        view_handlers = [(self.game_view, self.__draw_game_view),
        (self.menu_view, self.__draw_menu_view),
        (self.game_over_view, self.__draw_game_over_view)]
        for view, handler in view_handlers:
            if view:
                contents = handler(*args)
        for content in contents:
            self.__display.blit(content[0], content[1])
        pygame.display.update()
