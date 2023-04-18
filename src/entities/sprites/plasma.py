from .entity import Entity

class Plasma(Entity):
    def __init__(self, coordinates, direction):
        super().__init__(coordinates, direction, 20, "plasma.png")
        