from .loop import Loop

class GameOverLoop(Loop):
    def __init__(self, renderer, event_handler, clock, points, space):
        super().__init__(renderer, event_handler, clock)
        self.__points = points
        self.__space = space
        self.__username = ""

    def _handle_commands(self, commands):
        character = commands["character"]
        if character:
            self.__username += character
        return super()._handle_commands(commands)

    def _get_rendering_params(self):
        return (self.__points, self.__space, self.__username)
