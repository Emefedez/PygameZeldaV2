import pygame
import sys

pygame.init()

# TEST HP BAR
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prueba de HP Bar")
#import imagenes
barbg = pygame.image.load("Sprites/HP bar/barbg.png").convert_alpha()
barhp = pygame.image.load("Sprites/HP bar/barhp.png").convert_alpha()
barfront = pygame.image.load("Sprites/HP bar/barfront.png").convert_alpha()

hpcurrent = 100
hpmax = 100

def draw_hp_bar(screen, x, y, hpcurrent, hpmax):
    screen.blit(barbg, (x, y))
    screen.blit(barhp, (x, y))
    screen.blit(barfront, (x, y))
    
def move_hp_bar(hpcurrent):
    if hpcurrent < 80:
     barhp.pos = (barhp.pos[0], barhp.pos[1] - 1)
     
    if hpcurrent < 50:
     barhp.pos = (barhp.pos[0], barhp.pos[1] - 2)
    
    
    
    
