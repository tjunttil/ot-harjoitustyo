from .entity import Entity

class Asteroid(Entity):
    def __init__(self, coordinates, direction):
        super().__init__(coordinates, direction, 0.2)
        super().load_image("asteroid.png")
