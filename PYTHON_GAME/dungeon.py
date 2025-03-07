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
    enemies = [Enemy() for _ in range(5)]  # Create 5 enemies
    return enemies
