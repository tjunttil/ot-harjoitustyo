from .entity import Entity

class Plasma(Entity):
    def __init__(self, coordinates, direction):
        super().__init__(coordinates, direction, 10)
        super()._load_image("plasma.png")
        