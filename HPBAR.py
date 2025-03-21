import pygame
import sys

pygame.init()

hpcurrent = 100
hpmax = 100

# posiciones con offset
x = 50
y = 50

xtruco = 50
ytruco = 50



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prueba de HP Bar")

# imágenes barra hp
barbg = pygame.image.load("Sprites/HP bar/barbg.png").convert_alpha()
barhp = pygame.image.load("Sprites/HP bar/barhp.png").convert_alpha()
barfront = pygame.image.load("Sprites/HP bar/barfront.png").convert_alpha()
bardamagemark = pygame.image.load("Sprites/HP bar/bardamagemark.png").convert_alpha()
 # Pasar bardamage a rect para hacer cálculos posteriores
rect_barfront = barfront.get_rect()
mark_rect = bardamagemark.get_rect()

#para hacer mark desaparecer
truco_rect = pygame.Rect(xtruco -50, ytruco, 30, 40)  # width and height of 40px


clock = pygame.time.Clock()

#función de daño
def reduce_hp(hpless):
    global hpcurrent
    hpcurrent -= hpless
    if hpcurrent < 0:
        hpcurrent = 0



def draw_hp_bar(screen, x, y, hpcurrent, hpmax):
    screen.blit(barbg, (x, y))
      
    # Cuanta vida queda
    hp_percent = hpcurrent / hpmax
    # Saber cómo dibujar la barra 
    barhp_full = barhp.get_width()
    cropped_width = int(barhp_full * hp_percent)
    barhp_cropped = barhp.subsurface((0, 0, cropped_width, 40))
    
    #dibujo barhp
    screen.blit(barhp_cropped, (x, y))
        
    # posicion de la marca de daño
    mark_x = x + cropped_width - mark_rect.width
    mark_rect.topleft = (mark_x, y) 
    
    # Solo dibuja bardamagemark si NO intersecta con truco_rect
    if not mark_rect.colliderect(truco_rect):
        screen.blit(bardamagemark, (mark_x, y))
    
    # barfront delante para que siempre se vea
    screen.blit(barfront, (x, y))


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if hit_button.collidepoint(mouse_pos):
                reduce_hp(10) 
    
    # Dibujo hpbar 
    draw_hp_bar(screen, x, y, hpcurrent, hpmax)
    
    #RECT TRUCO VISIBLE PARA TESTEAR
    #pygame.draw.rect(screen, (255, 0, 0), truco_rect, 1)

    
    # TESTBUTTON
    hit_button = pygame.Rect(50, 550, 100, 40)
    font = pygame.font.SysFont(None, 24)

    pygame.draw.rect(screen, (0, 255, 0), hit_button)
    hit_text = font.render("Hit", True, (255, 255, 255))
    text_rect = hit_text.get_rect(center=hit_button.center)
    screen.blit(hit_text, text_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



