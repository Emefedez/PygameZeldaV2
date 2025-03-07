import pygame
import sys
import random
import variables

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("cancionbase.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(variables.volume)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colores
BLACK = (0, 0, 0)
GREEN = (120, 255, 95)
RED = (255, 0, 0)
BLUE = (173, 216, 230)
YELLOW = (255, 255, 20)
GREY = (128, 128, 128)
LIGHTGREY = (200, 200, 200)

# FUENTE
font = pygame.font.SysFont(None, 50, bold=True)

# Botón PLAY 
button_text = font.render("PLAY", True, BLACK)
button_rect = pygame.Rect(0, 0, 200, 50)
button_rect.right = width - 160  
button_rect.centery = height // 2 - 60

# Botón QUIT 
button_text2 = font.render("QUIT", True, BLACK)
button_rect2 = pygame.Rect(0, 0, 200, 50)
button_rect2.right = width - 160
button_rect2.centery = height // 2 + 0

# Botones de VOLUMEN 
volumebutton_rectminus = pygame.Rect(0, 0, 40, 40)
volumebutton_rectminus.center = (width // 1 - 340, height - 180)

volumebutton_rectplus  = pygame.Rect(0, 0, 40, 40)
volumebutton_rectplus.center  = (width // 1 - 180, height - 180)

# Cargar imagen de FONDO y escalarla
FONDO = pygame.image.load("Sprites/cocinacorrompida.png").convert()
FONDO = pygame.transform.scale(FONDO, (width, height))

# Cargar logo
title_sprite = pygame.image.load("Sprites/carrotscooking.png").convert_alpha()
title_rect = title_sprite.get_rect(center=(width // 2, height // 4 - 50))

# cargar zanahoria
zanahoria = pygame.image.load("Sprites/zanahoria2.png").convert_alpha()
zanahoriascaled = pygame.image.load("Sprites/zanahoria2.png").convert_alpha()
zanahoriascaled = pygame.transform.scale(zanahoriascaled, (256, 256))



# escalar icono y aplicar zanahoria
pygame.display.set_caption("Carrots Cooking")
pygame.display.set_icon(zanahoriascaled)

# Oscilación de la zanahoria
OSCILLATIONOFFSET =  5       # Posición inicial
OSCILLATIONVELOCITY = 0.3 
SPRINGSTRENGTH = 0.01      # efecto rebote

clock = pygame.time.Clock()

# FLICKER FUERA
FLICKERUPDATE = 140 
last_flicker_time = pygame.time.get_ticks()
ALPHAFONDO = random.randint(120, 180)

COLORPLAY = RED 
COLORQUIT = YELLOW

while True:
    volume = variables.volume

    # RESETS PARA COLORES
    COLORVOLUMEMINUS = GREY
    COLORVOLUMEPLUS = GREY

    if variables.volume > 0.8:
        COLORVOLUMENUMBER = RED
    elif variables.volume < 0.5:
        COLORVOLUMENUMBER = GREEN
    else:
        COLORVOLUMENUMBER = YELLOW

    # Dibujar imagen de FONDO
    screen.blit(FONDO, (0, 0))

    # OSCILACIÓN ZANAHORIA
    OSCILLATIONVELOCITY += -SPRINGSTRENGTH * OSCILLATIONOFFSET
    OSCILLATIONOFFSET += OSCILLATIONVELOCITY

    # FLICKER
    TICK = pygame.time.get_ticks()
    if TICK - last_flicker_time >= FLICKERUPDATE:
        ALPHAFONDO = random.randint(120, 230)
        last_flicker_time = TICK

    overlay = pygame.Surface((width, height))
    overlay.fill(BLACK)
    overlay.set_alpha(ALPHAFONDO)
    screen.blit(overlay, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # click play?
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            COLORPLAY = RED
            if event.type == pygame.MOUSEBUTTONDOWN:
                import Juego
        else:
            COLORPLAY = GREEN

        # click quit?
        if button_rect2.collidepoint(pygame.mouse.get_pos()):
            COLORQUIT = BLUE
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        else:
            COLORQUIT = YELLOW

        # modificar volumen
        variables.update_volume(event, volumebutton_rectplus, volumebutton_rectminus)
    
    # Actualizar variables volumen
    pygame.mixer.music.set_volume(variables.volume)
    
    # Dibujar
    pygame.draw.rect(screen, COLORPLAY, button_rect)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    pygame.draw.rect(screen, COLORQUIT, button_rect2)
    text_rect2 = button_text2.get_rect(center=button_rect2.center)
    screen.blit(button_text2, text_rect2)
    
    # color botones 
    if volumebutton_rectplus.collidepoint(pygame.mouse.get_pos()):
        COLORVOLUMEPLUS = LIGHTGREY
    if volumebutton_rectminus.collidepoint(pygame.mouse.get_pos()):
        COLORVOLUMEMINUS = LIGHTGREY

    # Dibujar botones de volumen
    pygame.draw.rect(screen, COLORVOLUMEPLUS, volumebutton_rectplus)
    pygame.draw.rect(screen, COLORVOLUMEMINUS, volumebutton_rectminus)
    
    plus_symbol = font.render("+", True, BLACK)
    minus_symbol = font.render("-", True, BLACK)
    screen.blit(plus_symbol, plus_symbol.get_rect(center=volumebutton_rectplus.center))
    screen.blit(minus_symbol, minus_symbol.get_rect(center=volumebutton_rectminus.center))
    
    # porcentaje de volumen
    vol_percentage = font.render(f"{int(volume * 100)}%", True, COLORVOLUMENUMBER)
    center_x = (volumebutton_rectplus.centerx + volumebutton_rectminus.centerx) // 2
    center_y = min(volumebutton_rectplus.top, volumebutton_rectminus.top) + 25
    vol_rect = vol_percentage.get_rect(center=(center_x, center_y))
    screen.blit(vol_percentage, vol_rect)
    
    # Posicion zanahoria
    ZANAHORIAPOSITION = (100, 200 + OSCILLATIONOFFSET)
    screen.blit(zanahoriascaled, ZANAHORIAPOSITION)
    
    # Dibujar el logo encima de todo
    screen.blit(title_sprite, title_rect)
    
    pygame.display.flip()
    clock.tick(60)