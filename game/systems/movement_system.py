from game.ecs.system import System
from game.components.transform import Transform
from game.components.velocity import Velocity

class MovementSystem(System):
    """Updates entity positions based on their velocity."""
    def update(self, world, dt):
        entity_ids = world.get_entities_with_component(Velocity)

        for entity_id in entity_ids:
            velocity = world.get_component(entity_id, Velocity)
            transform = world.get_component(entity_id, Transform)

            if velocity and transform:
                transform.x += velocity.dx * dt
                transform.y += velocity.dy * dt
