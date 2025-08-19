import pygame
from game.ecs.system import System
from game.components.player_controlled import PlayerControlled
from game.components.velocity import Velocity

class InputSystem(System):
    """Handles player input."""
    def update(self, world, dt):
        player_entities = world.get_entities_with_component(PlayerControlled)

        for entity_id in player_entities:
            velocity = world.get_component(entity_id, Velocity)
            if not velocity:
                continue

            # Reset velocity
            velocity.dx, velocity.dy = 0, 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                velocity.dx = -200
            if keys[pygame.K_RIGHT]:
                velocity.dx = 200
            if keys[pygame.K_UP]:
                velocity.dy = -200
            if keys[pygame.K_DOWN]:
                velocity.dy = 200
