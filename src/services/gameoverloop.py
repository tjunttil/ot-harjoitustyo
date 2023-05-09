from .loop import Loop

class GameOverLoop(Loop):
    def __init__(self, renderer, event_handler, clock, points, space, point_repository):
        super().__init__(renderer, event_handler, clock)
        self.__points = points
        self.__space = space
        self.__point_repository = point_repository
        self.__username = ""

    def _handle_commands(self, commands):
        character = commands["input"]
        if character:
            self.__username += character
        if commands["delete"]:
            self.__username = self.__username[:-1]
        if commands["save"]:
            self.__point_repository.add(self.__username, self.__points)
            return False
        return super()._handle_commands(commands)

    def _get_rendering_params(self):
        return (self.__points, self.__space, self.__username)
