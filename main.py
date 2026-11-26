import pygame

from settings import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS
)

from world.world import World
from world.camera import Camera

def main():

    # Initialize Pygame
    pygame.init()

    # Create application window
    pygame.display.set_caption(WINDOW_TITLE)

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    # Initialize clock
    clock = pygame.time.Clock()

    # Initialize world and camera
    world = World()
    camera = Camera()

    # Main application loop
    running = True

    while running:

        # Calculate delta time
        dt = clock.tick(FPS) / 1000.0

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

            camera.handle_event(event)

        # Get keyboard input
        keys = pygame.key.get_pressed()

        # Update simulation and camera
        world.update(dt)
        camera.update(dt, keys)

        # Render world
        world.draw(screen, camera)

        # Update display
        pygame.display.flip()

    # Shutdown
    pygame.quit()

if __name__ == "__main__":
    main()