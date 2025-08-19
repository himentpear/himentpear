import pygame
from .base_state import BaseState

class GameOverState(BaseState):
    """The state for the game over screen."""
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Quit the game
                pygame.quit()
                exit()

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over. Press ESC to quit.", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(text, text_rect)
