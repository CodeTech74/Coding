import pygame
import sys

def game_screen():
    """
    Initializes Pygame, creates a game window, and displays it.
    This is the basic setup for a Pygame application.
    """
    # Initialize Pygame
    pygame.init()

    # Define the dimensions of the game window
    screen_width = 800
    screen_height = 600

    # Create the game window (surface)
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the title of the window
    pygame.display.set_caption("My First Pygame Screen")

    # Fill the screen with a background color (e.g., light blue)
    background_color = (200, 200, 255)  # RGB tuple for light blue
    screen.fill(background_color)

    # Main game loop
    running = True
    while running:
        # Event handling loop:  This is where you process user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the loop

        # Update the display:  This makes the changes visible
        pygame.display.flip()

    # Quit Pygame:  This cleans up resources
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_screen()
