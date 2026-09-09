## Overview
A classic Snake game built with Python and Pygame. The player controls a snake that moves around a grid, eating food to grow longer while avoiding collisions with the walls or its own body. The game tracks score in real time and ends when a collision occurs, encouraging players to beat their previous high score. This project demonstrates core game development concepts like grid-based movement, collision detection, real-time input handling, and event-driven programming — making it a great hands-on learning exercise as well as a fun nostalgic game.

## Tech Stack
- Language: Python 3.8+
- Library: Pygame — handles window rendering, the game loop, keyboard input, and collision detection
- Data Storage: Local file (e.g. JSON/text) for saving high scores (if applicable)
- Version Control: Git & GitHub


## Key Concepts Used
- Grid-based coordinate movement
- Game loop and frame rate control (clock.tick())
- Event handling (pygame.event.get())
- Collision detection (self-collision and boundary collision)
- Basic 2D rendering with pygame.draw / pygame.image


## System Requirements
- Python 3.8 or higher
- Pygame library (pip install pygame)
- Works on Windows, macOS, and Linux
