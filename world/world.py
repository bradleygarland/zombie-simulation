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

        # Calculate zoomed grid spacing
        grid_spacing = GRID_SIZE * camera.zoom

        # Determine adaptive grid spacing
        grid_multiplier = 1
        min_screen_spacing = 24

        while GRID_SIZE * grid_multiplier * camera.zoom < min_screen_spacing:
            grid_multiplier *= 2

        # Calculate grid spacing in world and screen coordinates
        world_grid_spacing = GRID_SIZE * grid_multiplier
        screen_grid_spacing = world_grid_spacing * camera.zoom

        # Calculate visible grid starting positions
        start_x = -(camera.x % world_grid_spacing) * camera.zoom
        start_y = -(camera.y % world_grid_spacing) * camera.zoom

        # Draw vertical grid lines
        x = start_x

        while x <= surface.get_width():
            pygame.draw.line(
                surface,
                GRID_COLOR,
                (round(x), 0),
                (round(x), surface.get_height())
            )

            x += screen_grid_spacing

        # Draw horizontal grid lines
        y = start_y

        while y <= surface.get_height():
            pygame.draw.line(
                surface,
                GRID_COLOR,
                (0, round(y)),
                (surface.get_width(), round(y))
            )

            y += screen_grid_spacing

        # Calculate world border relative to camera and zoom
        world_rect = pygame.Rect(
            round(-camera.x * camera.zoom),
            round(-camera.y * camera.zoom),
            round(self.width * camera.zoom),
            round(self.height * camera.zoom)
        )

        # Draw world boundaries
        pygame.draw.rect(
            surface,
            WORLD_BORDER_COLOR,
            world_rect,
            4
        )