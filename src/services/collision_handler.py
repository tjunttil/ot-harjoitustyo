import pygame

class CollisionHandler:
    """A class for handling object collisions
    """
    def check_ship_destruction(self, ship, asteroids):
        """A method for checking whether the given Ship-object has collided with
        an asteroid object in the given asteroids-group. The method uses the collide-points
        of the Ship-object.

        Args:
            ship (Ship): the Ship-object
            asteroids (pygame.sprite.Group()): the group of Asteroid-objects

        Returns:
            Boolean: True if the ship has collided with an asteroid, False otherwise.
        """
        for collide_point in ship.collide_points:
            for asteroid in asteroids:
                if pygame.Rect.collidepoint(asteroid.rect, tuple(collide_point)):
                    return True
        return False

    def handle_plasma_hits(self, plasmas, asteroids):
        """A method for determining the number of asteroids plasma-projectiles have hit,
        and eliminating both in such instances.

        Args:
            plasmas (pygame.sprite.Group()): the plasmas currently in transit
            asteroids ([type]): the asteroids floating around

        Returns:
            Int: the number of collisions of Plasma and Asteroid objects
        """
        points = 0
        for asteroid in asteroids:
            if len(pygame.sprite.spritecollide(asteroid, plasmas, True)) > 0:
                asteroid.get_hit()
                if asteroid.hits > 2:
                    points += 1
                    asteroid.kill()
        return points
