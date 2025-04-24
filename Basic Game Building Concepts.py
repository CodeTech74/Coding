import pygame
import sys

def game_screen_with_elements():
    """
    Initializes Pygame, creates a game window, and adds a rectangle and text.
    """
    # Initialize Pygame
    pygame.init()

    # Define screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Screen with Elements")

    # Define colors
    background_color = (200, 200, 255)  # Light blue
    red = (255, 0, 0)
    white = (255, 255, 255)

    # Fill the screen
    screen.fill(background_color)

    # --- Draw a Rectangle ---
    # pygame.draw.rect(surface, color, rect, width=0)
    # surface: The surface to draw on (our screen)
    # color: The color of the rectangle (red)
    # rect: A tuple (x, y, width, height) defining the rectangle's position and size
    # width: The thickness of the rectangle's border (0 for filled)
    rectangle_x = 350
    rectangle_y = 250
    rectangle_width = 100
    rectangle_height = 100
    pygame.draw.rect(screen, red, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

    # --- Draw a second, outlined rectangle ---
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50), 2) # Green outline, 2 pixels thick

    # --- Add Text ---
    # 1. Create a Font object
    # pygame.font.Font(fontname, size, bold=False, italic=False)
    # fontname:  None for system default, or a string for a specific font file
    # size: The size of the font in points
    font_size = 32
    font = pygame.font.Font(None, font_size)  # Use the default system font

    # 2. Render the text (create a Surface with the text on it)
    # Font.render(text, antialias, color, background=None)
    # text: The string to render
    # antialias:  True for smooth edges, False for pixelated edges
    # color: The color of the text (white)
    # background:  Optional background color for the text
    text = font.render("Hello, Pygame!", True, white)

    # 3. Get the rectangular area of the text surface
    text_rect = text.get_rect()

    # 4. Center the text on the screen
    text_rect.center = (screen_width // 2, screen_height // 2)  # Integer division for the center

    # 5. Blit (draw) the text surface onto the main screen
    # Surface.blit(source, dest, area=None, special_flags=0)
    # source: The Surface to draw (our text)
    # dest:  A tuple (x, y) for the top-left corner of where to draw, or a Rect
    screen.blit(text, text_rect)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_screen_with_elements()
