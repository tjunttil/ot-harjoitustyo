class Loop:
    """A parent class for all ui-logic loops

    Attributes:
        renderer (Renderer): a renderer that draws ui-elements on the display
        event_handler (EventHandler): an object that returns commands
        corresponding to events
        clock (Clock): a clock object

    """
    def __init__(self, renderer, event_handler, clock):
        """A constructor for the class

        Args:
            renderer (Renderer): a renderer that draws ui-elements on the display
            event_handler (EventHandler): an object that returns commands
            clock (Clock): a clock object
        """
        self.__renderer = renderer
        self.__event_handler = event_handler
        self.__clock = clock

    def _handle_commands(self, commands):
        return not commands["quit"]

    def _get_rendering_params(self):
        return []

    def _logic_call(self):
        return True

    def start(self):
        """The method for handling the logic of the loop. Calls event_handler for
        commands and a logic-method, determines if these result in a view switch,
        then finally renders the view for this cycle if reachable.

        Returns:
            List: returns a list containing the name of the view to be switched to, and
            the required parameters for rendering the view, if applicable. If quitting,
            returns a list with False.
        """
        running = True
        while running:
            commands_list = self.__event_handler.handle_events()
            for commands in commands_list:
                return_value = self._handle_commands(commands)
                if isinstance(return_value, bool):
                    running = return_value
                else:
                    return [return_value]
            view = self._logic_call()
            params = self._get_rendering_params()
            if not isinstance(view, bool):
                return [view] + params
            self.__renderer.service_operation(*params)
            self.__clock.tick(60)
        return [False]
