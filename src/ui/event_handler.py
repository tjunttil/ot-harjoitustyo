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
        return event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN

    def __handle_starting_score_list(self, event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_l

    def _menu_operation(self, *args):
        event = args[0]
        commands = {}
        commands["start game"] = self.__handle_starting_game(event)
        commands["start score list"] = self.__handle_starting_score_list(event)
        return commands

    def _game_operation(self, *args):
        event = args[0]
        commands = {}
        commands["move"] = self.__handle_movement(event)
        commands["fire"] = self.__handle_firing(event)
        return commands

    def _game_over_operation(self, *args):
        event = args[0]
        commands = {"input": False, "save": False, "delete": False}
        if event.type == pygame.TEXTINPUT:
            commands["input"] = event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                commands["save"] = True
            if event.key == pygame.K_BACKSPACE:
                commands["delete"] = True
        return commands

    def _scorelist_operation(self, *args):
        event = args[0]
        commands = {"all": False, "month":False, "week":False}
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                commands["month"] = True
            if event.key == pygame.K_w:
                commands["week"] = True
            if event.key == pygame.K_a:
                commands["all"] = True
        return commands

    def _basic_operations(self):
        return {}

    def _final_operations(self, data, *args):
        event = args[0]
        data["quit"] = self.__handle_quitting(event)
        return data

    def _combine(self, data1, data2):
        return {**data1, **data2}

    def handle_events(self):
        events = self.__event_queue.get()
        commands_list = []
        for event in events:
            commands_list.append(self.service_operation(event))
        return commands_list
   