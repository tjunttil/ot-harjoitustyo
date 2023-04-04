import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,0,10,10)
        #self.rect.x = 0
        #self.rect.y = 0
        self.angle = 0
        self.velocity = 0
        self.angular_velocity = 0
    
    def change_velocity(self, direction, change):
        v,a = direction
        self.velocity += change*v
        self.angular_velocity += change*a

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self._angle = value


        

        