import pygame
import sys
import Menu

pygame.init()


hpcurrent = 100
hpmax = 100
#al sufrir daño
offset = 5
x = 50
y = 50


# TEST HP BAR
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prueba de HP Bar")
#import imagenes
barbg = pygame.image.load("Sprites/HP bar/barbg.png").convert_alpha()
barhp = pygame.image.load("Sprites/HP bar/barhp.png").convert_alpha()
barfront = pygame.image.load("Sprites/HP bar/barfront.png").convert_alpha()

#transformar en Rect
rect_barbg = barbg.get_rect(topleft=(x, y))
rect_barhp = barhp.get_rect(topleft=(x, y))
rect_barfront = barfront.get_rect(topleft=(x, y))


def draw_hp_bar(screen, x, y, hpcurrent, hpmax, offset):
    screen.blit(barhp, (x, y))
    screen.blit(barbg, (x, y))
    screen.blit(new_barhp_rect, (x, y))
    
    new_barhp_rect = barhp_rect(x + offset, y)
    inter_rect = new_barhp_rect.clip(rect_barfront)
    
    if  hit:
        offset = offset + 5


    screen.blit(barfront, (x, y))
    
 
    
def move_hp_bar(hpcurrent):
    
    if hpcurrent < 80:
     barhp.pos = (barhp.pos[0], barhp.pos[1] - 1)
     
    if hpcurrent < 50:
     barhp.pos = (barhp.pos[0], barhp.pos[1] - 2)
    
    
    
    
