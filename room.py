import pygame
import sys

#Escalar calidad y pantalla
COLUMNS = 12
ROWS = 9
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_WIDTH = SCREEN_WIDTH // COLUMNS  
TILE_HEIGHT = SCREEN_HEIGHT // ROWS  

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# metemos las imágenes en un diccionario para escalarlas en  una sola línea

tile_images = {
    'm': pygame.image.load("Sprites/Enviroment/Cocina/Madera2.png").convert_alpha(),
    'b': pygame.image.load("Sprites/Enviroment/Cocina/Baldosa.png").convert_alpha()
}

# escalamos las imagenes
better_tileimages = {}
for letter, image in tile_images.items():
    better_tileimages[letter] = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))

# Example tilemaps (each sub-list is a row) EMPIEZA EN 0
room0 = [
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b']
]

room1 = [
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b']
]
room2 = [
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b']
]

room2 = [
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b'],
    ['b','b','b','b','b','m','m','b','b','b','b','b']
]

# Room 3: Diagonal pattern – beginning with all 'm' on row 0 and then increasing 'b's on the left.
room3 = [
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','b','m','m','m','m','m','m'],
    ['b','b','b','b','b','b','b','m','m','m','m','m'],
    ['b','b','b','b','b','b','b','b','m','m','m','m']
]

# Room 4: Border room – outer border is 'm' and interior is 'b'
room4 = [
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','b','b','b','b','b','b','b','b','b','b','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','m']
]

# Room 5: Checkerboard pattern
room5 = [
    ['m','b','m','b','m','b','m','b','m','b','m','b'],
    ['b','m','b','m','b','m','b','m','b','m','b','m'],
    ['m','b','m','b','m','b','m','b','m','b','m','b'],
    ['b','m','b','m','b','m','b','m','b','m','b','m'],
    ['m','b','m','b','m','b','m','b','m','b','m','b'],
    ['b','m','b','m','b','m','b','m','b','m','b','m'],
    ['m','b','m','b','m','b','m','b','m','b','m','b'],
    ['b','m','b','m','b','m','b','m','b','m','b','m'],
    ['m','b','m','b','m','b','m','b','m','b','m','b']
]

# Room 6: Vertical stripes (each stripe 2 columns wide alternating 'm' and 'b')
room6 = [
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b'],
    ['m','m','b','b','m','m','b','b','m','m','b','b']
]

# Room 7: Horizontal stripes (each stripe 2 rows high alternating 'm' and 'b')
room7 = [
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['m','m','m','m','m','m','m','m','m','m','m','m']
]

# Room 8: Reverse diagonal pattern – from left 'm' tapering to 'b' on the right.
room8 = [
    ['m','m','m','m','m','m','m','m','m','m','m','m'],
    ['m','m','m','m','m','m','m','m','m','m','m','b'],
    ['m','m','m','m','m','m','m','m','m','m','b','b'],
    ['m','m','m','m','m','m','m','m','m','b','b','b'],
    ['m','m','m','m','m','m','m','m','b','b','b','b'],
    ['m','m','m','m','m','m','m','b','b','b','b','b'],
    ['m','m','m','m','m','m','b','b','b','b','b','b'],
    ['m','m','m','m','m','b','b','b','b','b','b','b'],
    ['m','m','m','m','b','b','b','b','b','b','b','b']
]

rooms = [room0, room1, room2, room3, room4, room5, room6, room7, room8]

while True:
    roomactual = 0
    for i in range(0,9):
        for j in range(0,12): 
            current_tile = rooms[roomactual][i][j]
            screen.blit(better_tileimages[current_tile], (j * TILE_WIDTH, i * TILE_HEIGHT))
    
    # ---- Minimapa ----
    # Dimensiones
    minimap_margin = 20
    mini_room_width = 30
    mini_room_height = 30
    gap = 5
    # Posición
    minimap_x = SCREEN_WIDTH - (5 * mini_room_width + 2 * gap) - minimap_margin
    minimap_y = minimap_margin

    # Dibujar cuartos
    for row in range(5):
        for column in range(5):
            index = row * 5 + column
            room_rect = pygame.Rect(minimap_x + column * (mini_room_width + gap),
                                     minimap_y + row * (mini_room_height + gap),
                                     mini_room_width,
                                     mini_room_height)
            
            pygame.draw.rect(screen, (100, 100, 100), room_rect, 2)
            # Colorear cuarto 
            if index == roomactual:
                pygame.draw.rect(screen, (255, 0, 0), room_rect)
                pygame.draw.rect(screen, (0, 0, 0), room_rect, 2)



    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


