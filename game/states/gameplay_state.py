from .base_state import BaseState
from game.ecs.world import World
from game.systems.input_system import InputSystem
from game.systems.movement_system import MovementSystem
from game.systems.render_system import RenderSystem
from game.components.transform import Transform
from game.components.velocity import Velocity
from game.components.sprite import Sprite
from game.components.player_controlled import PlayerControlled

class GameplayState(BaseState):
    """The state for the main game loop."""
    def __init__(self, state_manager, screen):
        super().__init__(state_manager)
        self.screen = screen
        self.world = World()

        # Create systems
        self.world.add_system(InputSystem())
        self.world.add_system(MovementSystem())
        self.world.add_system(RenderSystem(self.screen))

        # Create player entity
        player = self.world.create_entity()
        self.world.add_component(player, Transform(100, 100))
        self.world.add_component(player, Velocity())
        self.world.add_component(player, Sprite((255, 0, 0), 50, 50))
        self.world.add_component(player, PlayerControlled())


    def handle_events(self, events):
        # The input system will handle events via pygame.key.get_pressed(),
        # but we could also handle single-press events here.
        pass

    def update(self, dt):
        self.world.update(dt)

    def draw(self, screen):
        # The render system will draw everything.
        # We could draw UI elements here if needed.
        pass
