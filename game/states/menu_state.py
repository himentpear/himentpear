import pygame
from .base_state import BaseState
from .gameplay_state import GameplayState

class MenuState(BaseState):
    """The state for the main menu."""
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Change to gameplay state when space is pressed
                self.state_manager.change_state(GameplayState(self.state_manager, self.screen))

    def update(self, dt):
        pass

    def draw(self, screen):
        # For now, just a black screen with some text
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Press SPACE to start", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(text, text_rect)
