from services.loop import Loop
class GameLoop(Loop):
    """A class for handling the game logic loop

    Args:
        Loop (Loop): the parent Loop class, provides core loop functionality

    Attributes:
        difficulty: the difficulty level of the game
        space: the Space object associated with the game, contains entities and
        methods for interacting with them
        points: the current point score of the game
    """
    def __init__(self, renderer, space, event_handler, clock):
        super().__init__(renderer, event_handler, clock)
        self.__difficulty = 3
        self.__space = space
        self.__points = 0

    def _get_rendering_params(self):
        return [self.__points, self.__space]

    def _logic_call(self):
        update = self.__space.update(self.__difficulty)
        if isinstance(update, bool):
            return "game over"
        self.__points += update
        return True

    def _handle_commands(self, commands):
        movement = commands["move"]
        if movement:
            self.__space.change_ship_velocity(movement[0], movement[1])
        if commands["fire"]:
            self.__space.fire_ship_cannon()
        return super()._handle_commands(commands)
