from .entity import Entity

class Asteroid(Entity):
    def __init__(self, coordinates, direction, velocity, size):
        super().__init__(coordinates, direction, velocity)
        super().load_image("asteroid.png")
        self.size = size
        self.radius = self.image.get_height()/2
