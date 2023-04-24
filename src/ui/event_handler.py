import pygame

class EventHandler:
    def __handle_movement(self, event):
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
                    return (direction, change)
                except KeyError:
                    return False
        return False

    def __handle_firing(self, event):
        # Pressing down the space-key fires the ship cannon
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return True
        return False

    def __handle_quitting(self, event):
        # Exit the game by pressing Escape key or closing the application 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
        if event.type == pygame.QUIT:
            return True
        return False

    def handle_event(self, event):
        commands = {}
        commands["move"] = self.__handle_movement(event)
        commands["fire"] = self.__handle_firing(event)
        commands["quit"] = self.__handle_quitting(event)
        return commands
                