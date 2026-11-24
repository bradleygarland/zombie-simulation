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

        self.zoom = 1.0

        self.min_zoom = max(
            self.width / WORLD_WIDTH,
            self.height / WORLD_HEIGHT
        )

        self.max_zoom = 3.0
        self.zoom_step = 1.1

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

        elif event.type == pygame.MOUSEWHEEL:
            center_x = self.x + self.width / (2 * self.zoom)
            center_y = self.y + self.height / (2 * self.zoom)

            if event.y > 0:
                self.zoom *= self.zoom_step

            elif event.y < 0:
                self.zoom /= self.zoom_step

                self.zoom = max(
                    self.min_zoom,
                    min(self.zoom, self.max_zoom)
                )

                # Recalculate camera position
                self.x = center_x - self.width / (2 * self.zoom)
                self.y = center_y - self.height / (2 * self.zoom)

                self.apply_bounds()

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
        visible_width = self.width / self.zoom
        visible_height = self.height / self.zoom

        max_x = max(0, WORLD_WIDTH - visible_width)
        max_y = max(0, WORLD_HEIGHT - visible_height)

        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))