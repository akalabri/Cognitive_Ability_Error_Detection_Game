# Cognitive_Ability_Error_Detection_Game
# Error Detection 

## Overview

"Error Detection IQ Test" is a game that challenges players to identify differences between two sets of items. The differences could be in terms of shape, color, or written character. Players need to count the number of differences and provide their answer.
![game_window](https://raw.githubusercontent.com/akalabri/Cognitive_Ability_Error_Detection_Game/main/game_window.png)
## Requirements

- Python
- Pygame

## Setup

1. Clone the repository.
2. Navigate to the game's directory.
3. Install the required packages:
\```bash
pip install pygame
\```

## How to Play

1. Run the game using:
\```bash
python main.py
\```
2. The game window will display two sets of items. Your task is to count the differences between the two sets.
3. Differences can be in shape, color, or the written character of the items.
4. Provide your answer and progress through the rounds.
5. At the end of the game, you'll have the option to save your answers to a CSV file.

## Game Components

- **Set 1 and Set 2**: These are the main areas where items are displayed for players to compare.
- **Keys**: This area might be used to provide input or show options to the player (based on the observed code structure).
- **Timer**: Players have a set amount of time to identify the differences in each round.

## Saving Game Data

Player responses can be saved to a CSV file named `game_data.csv` in the `data` directory. This file captures the player's name, round number, the correct answer, the player's answer, and the date/time of the game session.
![data_csv](https://raw.githubusercontent.com/akalabri/Cognitive_Ability_Error_Detection_Game/main/game_data.png)
## Development

- **main.py**: This is the main entry point for the game. It sets up the game loop and renders the game window.
- **components.py**: Defines game components, including the representation of individual items.
- **config.py**: Contains configurations and constants used throughout the game.
- **utils.py**: Provides utility functions, including the capability to save game data to a CSV file.

## Feedback and Contributions

Feel free to open issues or pull requests if you have suggestions, improvements, or fixes. We appreciate your feedback!
