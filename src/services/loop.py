class Loop:
    def __init__(self, renderer, event_handler, clock):
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
        print("starting loop")
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
            self.__renderer.draw(*params)
            self.__clock.tick(60)
        return [False]
