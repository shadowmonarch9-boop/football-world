import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions and the window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Test")

# Set up color (R, G, B)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white color
    screen.fill(WHITE)
    
    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (150, 100, 100, 50))
    
    # Update the screen display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
