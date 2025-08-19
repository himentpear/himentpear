class Entity:
    """A simple class to represent a unique entity in the game."""
    def __init__(self, entity_id):
        self.id = entity_id

    def __repr__(self):
        return f"Entity({self.id})"
