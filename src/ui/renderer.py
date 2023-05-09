import pygame
from .ui_service import UIService

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

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
        point_text = self.game_font.render(f"Points: {points}", True, WHITE)
        return [(point_text,(0,0))]

    def __draw_game_over_view(self, points, space, username):
        space.all_entities.draw(self.__display)
        texts = []
        contents = []
        texts.append(self.title_font.render("GAME OVER", True, RED))
        texts.append(self.item_font.render(f"POINTS: {points}", True, RED))
        texts.append(self.item_font.render(
            "Enter username to save score:", True, WHITE))
        texts.append(self.item_font.render(f"{username}", True, RED))
        for i in range(4):
            contents.append((texts[i], texts[i].get_rect(center = (320, 160 + 50*i))))
        return contents

    def __draw_menu_view(self):
        title_text = self.title_font.render("ASTEROIDS", True, WHITE)
        start_new_game_text = self.item_font.render(
            "Press Return for new game", True, WHITE)
        view_score_list_text = self.item_font.render(
            "Press the l-key to view scores", True, WHITE)
        title_rect = title_text.get_rect(center = (320, 180))
        start_rect = start_new_game_text.get_rect(center = (320, 250))
        score_rect = view_score_list_text.get_rect(center = (320, 300))
        return [(title_text,title_rect), (start_new_game_text,start_rect),
        (view_score_list_text, score_rect)]

    def __draw_score_list_view(self, points_list):
        contents = []
        title_text = self.item_font.render("High scores", True, WHITE)
        title_rect = title_text.get_rect(center = (320, 50))
        contents.append((title_text, title_rect))
        for index, entry in enumerate(points_list):
            username, points, time = entry
            entry_text = self.game_font.render(
                f"{index+1:2}{username:>30}:{points:3}{time:>20}", True, WHITE)
            entry_rect = entry_text.get_rect(center = (120, 100 + 10*index))
            contents.append((entry_text, entry_rect))
        return contents

    def draw(self, *args):
        self.__display.fill(BLACK)
        view_handlers = [(self.game_view, self.__draw_game_view),
        (self.menu_view, self.__draw_menu_view),
        (self.game_over_view, self.__draw_game_over_view),
        (self.score_list_view, self.__draw_score_list_view)]
        for view, handler in view_handlers:
            if view:
                contents = handler(*args)
        for content in contents:
            self.__display.blit(content[0], content[1])
        pygame.display.update()
