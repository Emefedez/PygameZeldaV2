import pygame

def draw_health_bar(screen, player_health):
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, player_health, 30))

def draw_mana_bar(screen, player_mana):
    pygame.draw.rect(screen, (0, 0, 255), (20, 60, player_mana, 30))
