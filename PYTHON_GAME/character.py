import pygame
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
