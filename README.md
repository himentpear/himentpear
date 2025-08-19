# 2D Meat Pigeon Game Architecture

This repository contains a basic, scalable architecture for a 2D "meat pigeon" (roguelike/roguelite) game, built using Python. The architecture is based on the Entity-Component-System (ECS) pattern.

## Architecture Overview

The project is structured as follows:

-   `game/`: The main game package.
    -   `main.py`: The entry point for the game.
    -   `settings.py`: Contains game settings like screen dimensions and FPS.
    -   `ecs/`: The core ECS implementation.
        -   `Entity`: A unique identifier for a game object.
        -   `Component`: A container for data.
        -   `System`: Contains the logic that operates on components.
        -   `World`: Manages all entities, components, and systems.
    -   `components/`: Data components that can be attached to entities (e.g., `Transform`, `Velocity`, `Sprite`).
    -   `systems/`: Systems that implement game logic (e.g., `MovementSystem`, `RenderSystem`).
    -   `core/`: Core game engine components.
        -   `state_manager.py`: A simple state machine for managing game states.
    -   `states/`: Different game states (e.g., `MenuState`, `GameplayState`).
    -   `world_gen/`: Contains code for procedural world generation.
        -   `map_generator.py`: A placeholder for map generation algorithms.
    -   `assets/`: A directory for game assets like sprites and sounds.

## How to Run

To run the game, you need to have Python and Pygame installed:

```bash
pip install pygame
python -m game.main
```

## Next Steps

This architecture provides a solid foundation for building a complete game. Here are some suggestions for how to extend it:

1.  **Enhance World Generation**: Implement a proper map generation algorithm in `MapGenerator` to create interesting levels. You could use techniques like Cellular Automata for caves or BSP trees for dungeons.
2.  **Expand the Rendering System**: Modify the `RenderSystem` and `Sprite` component to support animated sprites and image loading instead of just solid colors.
3.  **Implement Combat**: Create a `CombatSystem` that uses the `Health` component and a new `Weapon` component to handle combat between the player and enemies.
4.  **Add Enemies**: Create new entities for enemies with basic AI. You could add an `AIControlled` component and an `AISystem` to manage their behavior.
5.  **Develop Items and Power-ups**: A key feature of roguelikes. You could create an `Item` component and an `ItemSystem` to manage items that modify player stats or behavior.
6.  **Add a UI**: Implement a user interface for displaying health, score, inventory, etc. This could be handled within the `RenderSystem` or a dedicated `UISystem`.
7.  **Sound**: Add sound effects and music.
8.  **More States**: Flesh out the `MenuState` and `GameOverState` and add other states like a pause menu or inventory screen.
