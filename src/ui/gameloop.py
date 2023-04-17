import pygame
from entities.space import Space


class GameLoop:
    def __init__(self, scale):
        self.display = pygame.display.set_mode((640*scale, 480*scale))
        self.clock = pygame.time.Clock()
        self.space = Space(scale)
        self.points = 0

    def start(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if not self.event_handler(event):
                    exit()
            self.space.move_objects()
            self.draw()
            self.clock.tick(60)

    def event_handler(self, event):
        movement = {pygame.KEYDOWN: 5, pygame.KEYUP: -5}
        # The keys are mapped to a velocity space
        # where the x-coordinate corresponds to velocity
        # and y-coordinate to angular velocity
        directions = {pygame.K_LEFT: (0, 1), pygame.K_RIGHT: (0, -1),
                      pygame.K_UP: (1, 0), pygame.K_DOWN: (-1, 0)}
        event_type = event.type
        for k in movement:
            if event_type == k:
                try:
                    change = movement[event_type]
                    direction = directions[event.key]
                    self.space.change_ship_velocity(direction, change)
                except KeyError:
                    pass
        if event_type == pygame.QUIT:
            return False
        return True

    def draw(self):
        self.display.fill((0, 0, 0))
        self.space.all_sprites.draw(self.display)
        pygame.display.update()
