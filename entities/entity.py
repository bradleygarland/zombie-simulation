
# =================================
# BASE ENTITY
# =================================
#
# Responsibilities
# - Store world coordinates
# - Store entity dimensions
# - Store color
# - Handle rendering
# - Provide a foundation for future movement and collision mechanics

import pygame

class Entity:
    def __init__(self, x, y, width, height, color):
        # World position
        self.x = float(x)
        self.y = float(y)

        # Entity dimensions
        self.width = width
        self.height = height

        # Visual properties
        self.color = color

        # Collision properties
        self.collision_radius = max(width, height) / 2

    def update(self, dt):
        """
        Updates entity logic.
        Individual entity class will override this.
        """
        pass

    def draw(self, surface, camera):
        """
        Draws the entity relative to the camera.
        Entity coordinates remain in world space.
        """

        # Convert world coordinates to screen coordinates
        screen_x = (self.x - camera.x) * camera.zoom
        screen_y = (self.y - camera.y) * camera.zoom

        # Scale dimemsions according to camera zoom
        scaled_width = max(1, round(self.width, * camera.zoom))
        scaled_height = max(1, round(self.height * camera.zoom))

        # Center the entity around its position
        rect = pygame.Rect(
            round(screen_x - scaled_width / 2),
            round(screen_y - scaled_height / 2),
            scaled_width,
            scaled_height
        )

        pygame.draw.rect(surface, self.color, rect)

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = float(x)
        self.y = float(y)