import pygame

from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WORLD_BACKGROUND
)

class World:
    def __init__(self):
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

    def update(self, dt):
        """
        Updates world logic.

        dt represents elapsed time
        since the previous frame.
        """
        pass

    def draw(self, surface):
        """
        Renders the world onto the screen.
        """

        surface.fill(WORLD_BACKGROUND)