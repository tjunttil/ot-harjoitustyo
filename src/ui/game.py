import pygame
from entities.space import Space

class GameLoop:
    def __init__(self, scale):
        self.display = pygame.display.set_mode(640*scale,480*scale)
        self.clock = pygame.time.Clock()
        self.space = Space(scale)
        self.points = 0

    def start(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if self.event_handler(event) == False:
                    break
            self.draw()
            self.clock.tick(60)

    def event_handler(self, event):
        movement = {pygame.KEYDOWN: 1, pygame.KEYUP: -1}
        # The keys are mapped to a velocity space where the x-coordinate corresponds to velocity and y-coordinate to angular velocity
        directions = {pygame.K_LEFT: (0,1), pygame.K_RIGHT: (0,-1), pygame.K_UP: (1,0), pygame.K_DOWN: (-1,0)}
        t = event.type
        if t in movement.keys():
            change = movement[t]
            direction = directions[event.key]
            self.space.change_ship_velocity(direction, change)
            self.space.move_ship
        if t == pygame.QUIT:
            return False

    def draw(self):
        pass


            



