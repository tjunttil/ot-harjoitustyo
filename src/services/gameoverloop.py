from .loop import Loop

class GameOverLoop(Loop):
    def __init__(self, renderer, event_handler, clock, points, space):
        super().__init__(renderer, event_handler, clock)
        self.__points = points
        self.__space = space

    def _get_rendering_params(self):
        return (self.__points, self.__space)
