class StateManager:
    """Manages a stack of game states."""
    def __init__(self):
        self._states = []

    def is_empty(self):
        return len(self._states) == 0

    def push_state(self, state):
        self._states.append(state)

    def pop_state(self):
        if not self.is_empty():
            self._states.pop()

    def change_state(self, state):
        self.pop_state()
        self.push_state(state)

    def get_current_state(self):
        if not self.is_empty():
            return self._states[-1]
        return None

    def handle_events(self, events):
        state = self.get_current_state()
        if state:
            state.handle_events(events)

    def update(self, dt):
        state = self.get_current_state()
        if state:
            state.update(dt)

    def draw(self, screen):
        state = self.get_current_state()
        if state:
            state.draw(screen)
