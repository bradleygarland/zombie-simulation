import pygame

from settings import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS
)

from world.world import World

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

    # Initialize world
    world = World()

    # Main application loop
    running = True

    while running:

        #Calculate delta time
        dt = clock.tick(FPS) / 1000.0

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update simulation
        world.update(dt)

        # Render world
        world.draw(screen)

        # Update display
        pygame.display.flip()

    # Shutdown
    pygame.quit()

if __name__ == "__main__":
    main()