import pygame
from game.ecs.system import System
from game.components.transform import Transform
from game.components.sprite import Sprite

class RenderSystem(System):
    """Renders entities with sprites."""
    def __init__(self, screen):
        self.screen = screen

    def update(self, world, dt):
        entity_ids = world.get_entities_with_component(Sprite)

        for entity_id in entity_ids:
            sprite = world.get_component(entity_id, Sprite)
            transform = world.get_component(entity_id, Transform)

            if sprite and transform:
                # Create a rect for drawing
                rect = pygame.Rect(transform.x, transform.y, sprite.width, sprite.height)
                pygame.draw.rect(self.screen, sprite.color, rect)
