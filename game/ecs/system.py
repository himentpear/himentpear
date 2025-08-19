class System:
    """A base class for all systems."""
    def __init__(self):
        pass

    def update(self, world, dt):
        """
        Update the system, processing entities.
        'world' is the game world, containing all entities and components.
        'dt' is the time delta since the last frame.
        """
        raise NotImplementedError
