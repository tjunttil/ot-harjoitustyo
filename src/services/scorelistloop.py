from .loop import Loop

class ScoreListLoop(Loop):
    """A loop for handling ui events in the scorelist view

    Args:
        Loop (Loop): the parent Loop class, provides core loop functionality

    Attributes:
        parent class attributes
        point_repository (PointRepository): the repository for points entries
    """
    def __init__(self, renderer, point_repository, event_handler, clock):
        super().__init__(renderer, event_handler, clock)
        self.__point_repository = point_repository

    # def _handle_commands(self, commands):
    #     return super()._handle_commands(commands)

    def _get_rendering_params(self):
        return [self.__point_repository.points_list()]
