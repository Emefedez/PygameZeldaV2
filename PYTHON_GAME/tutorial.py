import pygame
from .character import Character

def start_tutorial(screen):
    player = Character(name="Player1")
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen
        handle_controls(player, screen)
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def handle_controls(player, screen):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move up
        print("Moving Up")
    if keys[pygame.K_s]:  # Move down
        print("Moving Down")
    if keys[pygame.K_a]:  # Move left
        print("Moving Left")
    if keys[pygame.K_d]:  # Move right
        print("Moving Right")
    if keys[pygame.K_e]:  # Attack
        print("Attacking with sword!")
