import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.core.state_manager import StateManager
from game.states.menu_state import MenuState

def main():
    """Main function to run the game."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2D Meat Pigeon Game")
    clock = pygame.time.Clock()

    state_manager = StateManager()
    # Pass the screen to the menu state
    menu_state = MenuState(state_manager)
    menu_state.screen = screen  # Add screen to menu state
    state_manager.push_state(menu_state)


    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        state_manager.handle_events(events)
        state_manager.update(dt)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the current state
        state_manager.draw(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
