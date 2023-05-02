import pygame
from .ui_service import UIService

class EventHandler(UIService):
    """A class for handling pygame events in the main gameloop

    Attributes:
        event_queue (EventQueue): the event queue for the pygame instance
        menu_view (Boolean): True if the current view is of the menu,
        False otherwise
        game_view (Boolean): True if the current view is of the game,
        False otherwise

    """
    def __init__(self, event_queue):
        """A constructor method for the class

        Args:
            event_queue (EventQueue): the event queue for the pygame instance

        """
        super().__init__()
        self.__event_queue = event_queue

    def __handle_movement(self, event):
        """A method for handling events leading to movement

        Args:
            event (pygame.event): the event to be handled

        Returns:
            Tuple representing the desired movement (with the first
            element corresponding to the change in velocity and the
            second to the direction) if the event corresponds pressing
            or releasing the arrow keys, False otherwise
        """
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
        """A method for handling events corresponding to firing the
        ship plasma cannon (i.e. pressing ths space key)

        Args:
            event (pygame.event): the event to be handled

        Returns:
            Boolean: True if the space key is pressed down, False otherwise
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return True
        return False

    def __handle_quitting(self, event):
        """Method for handling events leading to quitting (i.e. closing the application
        or pressing Escape key)

        Args:
            event (pygame.event): [description]

        Returns:
            Boolean: True if the event corresponds to quitting, False otherwise
        """
        # Exit the game by pressing Escape key or closing the application 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
        if event.type == pygame.QUIT:
            return True
        return False

    def __handle_starting_game(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return True
        return False

    def __handle_menu_event(self, event):
        """A method for handling events specific for the menu view,
        calls subroutines

        Args:
            event (pygame.event): the event to be handled

        Returns:
            dict: a dictionary of the commands for menu-specific events
        """
        commands = {}
        commands["start game"] = self.__handle_starting_game(event)
        return commands

    def __handle_game_event(self, event):
        """A method for handling game-events, calls subroutines

        Args:
            event (pygame.event): the event to be handled

        Returns:
            dictionary: contains the command-value pairs corresponding to the event
        """
        commands = {}
        commands["move"] = self.__handle_movement(event)
        commands["fire"] = self.__handle_firing(event)
        return commands

    def handle_event(self, event):
        """A general-purpose method for handling any event, calls the 
        specific event -handling subroutines based on the view
        """
        commands = {}
        commands["quit"] = self.__handle_quitting(event)
        if self.game_view:
            commands = dict(**(self.__handle_game_event(event)), **commands)
        if self.menu_view:
            commands = dict(**(self.__handle_menu_event(event)), **commands)
        return commands

    def handle_events(self):
        events = self.__event_queue.get()
        commands_list = []
        for event in events:
            commands_list.append(self.handle_event(event))
        return commands_list
   