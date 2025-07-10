

import random
import pygame
import sys

# Window dimensions and settings
WIDTH, HEIGHT = 1000, 400
FPS = 60
BLUE = (100, 100, 255)

class HorseRace:
    """Class that manages the horse race game."""
    def __init__(self):
        pygame.init()
        # Set up the main window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Horse Race")
        self.font = pygame.font.SysFont("Arial", 28)

        # Load background image
        try:
            self.bg_image = pygame.image.load('IMG/background.jpg').convert()
            self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))
        except Exception as e:
            print(f"[ERROR] Background image not found: {e}")
            sys.exit()

        # (Optional) Load victory sound
        try:
            self.victory_sound = pygame.mixer.Sound("victory.wav")
        except Exception as e:
            self.victory_sound = None

        # Initialize lanes and horses
        self.lane_height = HEIGHT / 4
        self.rect_width = 100
        self.rect_height = self.lane_height - 10

        self.horses = []
        names = ["Lightning", "Storm", "Bolt", "Flash"]
        horse_images = []
        # Load horse images
        for idx in range(1, 5):
            try:
                img = pygame.image.load(f"IMG/spirit-pixel.gif").convert_alpha()
                img = pygame.transform.scale(img, (int(self.rect_width), int(self.rect_height)))
                horse_images.append(img)
            except Exception as e:
                print(f"[ERROR] Horse image spirit-pixel.gif not found: {e}")
                sys.exit()

        # Create horse objects with image and position
        for i in range(4):
            rect = pygame.Rect(0, i * self.lane_height + 5, self.rect_width, self.rect_height)
            self.horses.append({
                "name": names[i],
                "image": horse_images[i],
                "rect": rect,
                "speed": 1 + i * 0.5
            })


    def draw_lines(self):
        """Draws the lanes and the horses as images."""
        for i in range(4):
            y = i * self.lane_height
            if i > 0:
                pygame.draw.line(self.screen, pygame.Color("WHITE"), (0, y), (WIDTH, y), 2)

        # Draw horses as images
        for horse in self.horses:
            self.screen.blit(horse["image"], horse["rect"])


    def move(self):
        """Moves the horses forward by a random amount. If a horse wins, shows the winner and resets the race."""
        for horse in self.horses:
            if horse["rect"].x < WIDTH - horse["rect"].width:
                horse["speed"] = random.randint(1, 5)
                horse["rect"].x += horse["speed"]
            else:
                self.show_winner(horse["name"])
                if self.victory_sound:
                    self.victory_sound.play()
                pygame.time.wait(3000)
                self.reset_race()
                return


    def show_winner(self, name):
        """Displays the winner on the screen with a custom message."""
        message = f"{name} is the fastest horse!"
        # Use a bright yellow color for high visibility
        text = self.font.render(message, True, (255, 255, 0))
        # Add a black border for even more contrast
        border = self.font.render(message, True, (0, 0, 0))
        x = WIDTH // 2 - text.get_width() // 2
        y = HEIGHT // 2 - text.get_height() // 2
        # Draw border by blitting black text slightly offset in 8 directions
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                if dx != 0 or dy != 0:
                    self.screen.blit(border, (x + dx, y + dy))
        self.screen.blit(text, (x, y))
        pygame.display.flip()


    def reset_race(self):
        """Resets the position of all horses to the start."""
        for horse in self.horses:
            horse["rect"].x = 0


    def initGUI(self):
        """Main game loop: handles events, updates the screen, and moves the horses."""
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))
            self.draw_lines()
            self.move()

            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()
        sys.exit()


    def startRace(self):
        """Prints a message when the race starts (can be expanded for more logic)."""
        print("The race has started!")

if __name__ == "__main__":
    race = HorseRace()
    race.startRace()
    race.initGUI()
