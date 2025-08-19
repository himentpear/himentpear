from game.ecs.component import Component

class Health(Component):
    """A component that stores the health of an entity."""
    def __init__(self, current_hp, max_hp):
        self.current_hp = current_hp
        self.max_hp = max_hp
