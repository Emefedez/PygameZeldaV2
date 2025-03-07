import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
COLORVOLUME = (255, 255, 20)
volume = 1.0

## funcion volumen
def update_volume(event, rect_plus, rect_minus):
    global volume
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if rect_plus.collidepoint(mouse_pos):
            volume = min(1.0, volume + 0.1)
        elif rect_minus.collidepoint(mouse_pos):
            volume = max(0.0, volume - 0.1)
    if volume > 1.0:
        volume = 1.0
    
    if volume <= 0.5:
        COLORVOLUME = GREEN
    if volume > 0.5:
        COLORVOLUME = RED

