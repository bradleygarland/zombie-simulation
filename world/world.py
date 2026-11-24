import pygame
from pygame import camera

from settings import (
    WORLD_WIDTH,
    WORLD_HEIGHT,
    GRID_SIZE,
    WORLD_BACKGROUND,
    GRID_COLOR,
    WORLD_BORDER_COLOR
)

class World:
    def __init__(self):
        self.width = WORLD_WIDTH
        self.height = WORLD_HEIGHT

    def update(self, dt):
        """
        Updates world logic.

        dt represents elapsed time
        since the previous frame.
        """
        pass

    def draw(self, surface, camera):
        """
        Renders the world onto the screen.
        """

        surface.fill(WORLD_BACKGROUND)

        # Calculate visible grid starting positions
        start_x = -(camera.x % GRID_SIZE)
        start_y = -(camera.y % GRID_SIZE)

        # Draw vertical grid lines
        x = start_x

        while x <= surface.get_width():
            pygame.draw.line(
                surface,
                GRID_COLOR,
                (int(x), 0),
                (int(x), surface.get_height())
            )

            x += GRID_SIZE

        # Draw horizontal grid lines
        y = start_y

        while y <= surface.get_height():
            pygame.draw.line(
                surface,
                GRID_COLOR,
                (0, int(y)),
                (surface.get_width(), int(y))
            )

            y += GRID_SIZE

        # Draw world boundaries
        border_x =  -int(camera.x)
        border_y = -int(camera.y)

        world_rect = pygame.Rect(
            border_x,
            border_y,
            self.width,
            self.height
        )

        pygame.draw.rect(
            surface,
            WORLD_BORDER_COLOR,
            world_rect,
            4
        )