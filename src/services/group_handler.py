import pygame

class GroupHandler:
    """A class for handling group operations, specifically for pygame.sprite.Group()-objects
    """
    def group(self):
        """Produces a pygame.sprite.Group()

        Returns:
            pygame.sprite.Group(): the desired sprite group
        """
        return pygame.sprite.Group()

    def add(self,element, group):
        """A method for adding an element (a sprite) to a group

        Args:
            element (pygame.sprite.Sprite()): the element to be added
            group (pygame.sprite.Group()): the group the element is to be added to
        """
        group.add(element)

    def elements(self, group):
        """Returns a list of the elements of the given group

        Args:
            group (pygame.sprite.Group()): the group the elements of which are queried

        Returns:
            list: a list of the group's elements
        """
        return group.sprites()
