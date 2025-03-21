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
room1 = [
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
rooms = [room1, room2]



while True:
    roomactual = 0
    for i in range(0,9):
        for j in range(0,12): 
            current_tile = rooms[roomactual][i][j]
            screen.blit(better_tileimages[current_tile], (j * TILE_WIDTH, i * TILE_HEIGHT))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
