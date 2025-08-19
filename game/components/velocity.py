from game.ecs.component import Component

class Velocity(Component):
    """A component that stores the velocity of an entity."""
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
