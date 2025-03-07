import pygame
import sys
import variables

# Import modules from the PYTHON GAME folder

from PYTHON_GAME import ui
from PYTHON_GAME import tutorial
from PYTHON_GAME import dungeon
from PYTHON_GAME import Untitled_1  
from PYTHON_GAME import character

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("cancionbase.ogg")
    pygame.mixer.music.play(-1, 0.0)
    
    # Set display dimensions and title
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Zelda-Inspired Game")
    clock = pygame.time.Clock()

    # Optionally, start the tutorial (this may block until finished)
    tutorial.start_tutorial(screen)
    
    # Create a player (from character.py) and dungeon enemies (from dungeon.py)
    player = character.Character(name="Hero")
    enemies = dungeon.create_dungeon_room()
    
    # For demonstration, set an initial player position.
    x, y = 100, 100
    
    running = True
    while running:
        # Process events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Update volume from variables.py (if you have volume buttons elsewhere, pass their rects)
            variables.update_volume(event, None, None)
             
        
        screen.fill((0, 0, 0))
        ui.draw_health_bar(screen, player.health)
        ui.draw_mana_bar(screen, player.mana)
        Untitled_1.draw_player(screen, x, y)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()