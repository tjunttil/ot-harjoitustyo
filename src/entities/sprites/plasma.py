from .entity import Entity

class Plasma(Entity):
    def __init__(self, coordinates, direction):
        super().__init__(coordinates, direction, 20)
        super().load_image("plasma.png")
        self.radius = self.image.get_height()/2
        