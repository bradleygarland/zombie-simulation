from entities.entity import Entity

class Zombie(Entity):
    def __init__(self, x, y):
        # Zombie properties
        self.size = 8
        self.zombie_color = (50, 200, 50)

        # Initialize inherited entity properties
        super().__init__(
            x=x,
            y=y,
            width=self.size,
            height=self.size,
            color=self.zombie_color
        )