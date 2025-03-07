import pygame
import sys
from menu import show_main_menu
from tutorial import start_tutorial


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Zelda-Inspired Game")

def main():
    while True:
        show_main_menu(screen)
        start_tutorial(screen)

if __name__ == "__main__":
    main()

    import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
        font = pygame.font.SysFont("Arial", 30)
        text_surf = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.rect.x + 20, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def show_main_menu(screen):
    buttons = [
        Button(300, 150, 200, 50, "Start Game", start_tutorial),
        Button(300, 250, 200, 50, "Game Info", show_game_info),
        Button(300, 350, 200, 50, "Exit", pygame.quit)
    ]
    
    running = True
    while running:
        screen.fill((0, 0, 0))  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            button.action(screen)

        for button in buttons:
            button.draw(screen)
        
        pygame.display.flip()

def show_game_info(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Game Info: Use WASD to move, E to attack, Q for shield.", True, (255, 255, 255))
    screen.blit(text, (100, 100))
    pygame.display.flip()
    pygame.time.wait(2000)
 import pygame
from character import Character

def start_tutorial(screen):
    player = Character(name="Player1")
    running = True
    while running:
        screen.fill((0, 0, 0))  
        handle_controls(player, screen)
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def handle_controls(player, screen):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  
        print("Moving Up")
    if keys[pygame.K_s]:  
        print("Moving Down")
    if keys[pygame.K_a]:  
        print("Moving Left")
    if keys[pygame.K_d]: 
        print("Moving Right")
    if keys[pygame.K_e]:  
        print("Attacking with sword!")


class Character:
    def __init__(self, name="Hero", health=100, mana=100, sword_damage=40, shield_block=0):
        self.name = name
        self.health = health
        self.mana = mana
        self.sword_damage = sword_damage
        self.shield_block = shield_block

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def use_sword(self, enemy):
        enemy.take_damage(self.sword_damage)
 import pygame
from random import randint

class Enemy:
    def __init__(self, health=50, damage=15):
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, player):
        player.take_damage(self.damage)

def create_dungeon_room():
    enemies = [Enemy() for _ in range(5)]  
    return enemies
import pygame

def draw_health_bar(screen, player_health):
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, player_health, 30))

def draw_mana_bar(screen, player_mana):
    pygame.draw.rect(screen, (0, 0, 255), (20, 60, player_mana, 30))
 player_image = pygame.image.load("path_to_player_sprite.png")
screen.blit(player_image, (x, y))  

