import pygame
from entities.space import Space


class GameLoop:
    def __init__(self, scale):
        self.display = pygame.display.set_mode((640*scale, 480*scale))
        self.clock = pygame.time.Clock()
        self.space = Space(scale)
        self.points = 0

    def game_over(self):
        exit()

    def start(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if not self.event_handler(event):
                    exit()
            self.space.create_asteroid()
            self.space.move_objects()
            if self.space.handle_collisions():
                self.game_over()
            self.draw()
            self.clock.tick(60)

    def handle_movement(self, event):
        # The keys are mapped to a velocity space
        # where the x-coordinate corresponds to velocity
        # and y-coordinate to angular velocity
        movement = {pygame.KEYDOWN: 5, pygame.KEYUP: -5}
        directions = {pygame.K_LEFT: (0, 1), pygame.K_RIGHT: (0, -1),
                      pygame.K_UP: (1, 0), pygame.K_DOWN: (-1, 0)}
        event_type = event.type
        for k in movement:
            if event_type == k:
                try:
                    change = movement[event_type]
                    direction = directions[event.key]
                    self.space.ship.change_velocity(direction, change)
                except KeyError:
                    pass

    def handle_firing(self, event):
        # Pressing down the space-key fires the ship cannon
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.space.fire_ship_cannon()

    def handle_quitting(self, event):
        # Exit the game by pressing Escape key or closing the application 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
        elif event.type == pygame.QUIT:
            return False
        return True

    def event_handler(self, event):
        self.handle_movement(event)
        self.handle_firing(event)
        return self.handle_quitting(event)

    def draw(self):
        self.display.fill((0, 0, 0))
        self.space.all_sprites.draw(self.display)
        pygame.display.update()
