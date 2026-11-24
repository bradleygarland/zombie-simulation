import pygame

from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WORLD_WIDTH,
    WORLD_HEIGHT,
    CAMERA_SPEED,
    SHIFT_SPEED_MULTIPLIER
)

class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.dragging = False

    def handle_event(self, event):

        # Start camera dragging
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                self.dragging = True

        # Stop camera dragging
        elif event.type ==pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.dragging = False

        # Move camera while dragging
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.x -= event.rel[0]
                self.y -= event.rel[1]

                self.apply_bounds()

    def update(self, dt, keys):
        movement = pygame.Vector2(0, 0)

        # WASD movement
        if keys[pygame.K_w]:
            movement.y -= 1

        if keys[pygame.K_s]:
            movement.y += 1

        if keys[pygame.K_a]:
            movement.x -= 1

        if keys[pygame.K_d]:
            movement.x += 1

        # Normalize diagonal movement
        if movement.length_squared() > 0:
            movement = movement.normalize()

        # Shift speed multiplier
        speed_multiplier = SHIFT_SPEED_MULTIPLIER if (
            keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        ) else 1

        # Apply movement
        self.x += movement.x * CAMERA_SPEED * speed_multiplier * dt
        self.y += movement.y * CAMERA_SPEED * speed_multiplier * dt

        self.apply_bounds()

    def apply_bounds(self):
        max_x = WORLD_WIDTH - self.width
        max_y = WORLD_HEIGHT - self.height

        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))