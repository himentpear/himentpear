class BaseState:
    """Base class for all game states."""
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def handle_events(self, events):
        """Handle input and other events."""
        raise NotImplementedError

    def update(self, dt):
        """Update the state's logic."""
        raise NotImplementedError

    def draw(self, screen):
        """Draw the state to the screen."""
        raise NotImplementedError
