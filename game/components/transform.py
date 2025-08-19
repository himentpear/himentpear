from game.ecs.component import Component

class Transform(Component):
    """A component that stores the position of an entity."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
