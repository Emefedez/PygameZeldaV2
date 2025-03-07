import pygame

def draw_player(screen, x, y):
    # Draw a red rectangle as the player
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
