# Horse Race App

A simple horse racing game built with Python and Pygame. Four horses race across the screen, and the winner is displayed with a visible message.

## Features
- Animated or static horse images
- Customizable horse names and images
- Victory sound and visible winner message
- Easy to modify and expand

## Requirements
- Python 3.x
- Pygame

## Setup
1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Pygame:
   ```sh
   pip install pygame
   ```
3. Place your horse images in the `IMG` folder. You can use a single image (e.g., `spirit-pixel.gif`) or a sequence of PNG frames (e.g., `spirit-pixel-0.png`, `spirit-pixel-1.png`, ...).
4. Place a background image as `IMG/background.jpg`.
5. (Optional) Add a victory sound as `victory.wav` in the project root.

## How to Run
From the project directory, run:
```sh
python main.py
```

## Customization
- Change horse names in the `names` list in `main.py`.
- Replace horse images or animation frames in the `IMG` folder.
- Edit the victory message and its color in the `show_winner` method.

## Credits
- Pygame: https://www.pygame.org/
- Horse images: Your own or free sprite resources

## License
Copyright (c) 2025, Created by F3rren - Samuele Alessandro Di Silvestri

This project is for educational and personal use. Replace images and sounds with your own or those you have rights to use.
