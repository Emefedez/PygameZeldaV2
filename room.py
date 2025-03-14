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
    'b': pygame.image.load("/Users/mateo/Documents/Dev/Gamedev/Pygame/PygameZelda2/PygameZeldaV2/Sprites/Enviroment/Cocina/Baldosa.png").convert_alpha(),
    'E': pygame.image.load("/Users/mateo/Documents/Dev/Gamedev/Pygame/PygameZelda2/PygameZeldaV2/Sprites/zanahoria2.png").convert_alpha()
}

# escalamos las imagenes
better_tileimages = {}
for letter, image in tile_images.items():
    better_tileimages[letter] = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))

# Example tilemaps (each sub-list is a row)
room1 = [
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','E','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','E','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','b','b','b','b','b','b','b','b','b','b','b']
]

roomactual = 0

for i in range(0,9):
    for j in range(0,12):
        if room1[i][j]== "b":
            screen.blit(better_tileimages['b'], (j*TILE_WIDTH, i*TILE_HEIGHT))
        if room1[i][j]== "E":
            screen.blit(better_tileimages['E'], (j*TILE_WIDTH, i*TILE_HEIGHT))
            
            
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
