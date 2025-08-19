from game.ecs.component import Component

class Sprite(Component):
    """A component that stores rendering information."""
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
