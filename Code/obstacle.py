import pygame
from random import randint
import main

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly1 = pygame.image.load("../graphics/Fly/Fly1.png").convert_alpha()
            fly2 = pygame.image.load("../graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly1, fly2]
            y_pos = 120
        elif type == 'snail':
            snail1 = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
            snail2 = pygame.image.load("../graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail1, snail2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))

    def animation(self):
        self.animation_index += 0.15
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def movement(self):
        global game_active
        current_time = main.display_score()
        global obstacle_speed

        if not (current_time % 10):
            obstacle_speed += 0.02

        self.rect.x -= int(obstacle_speed)
        if self.rect.right < -100:
            self.kill()

    def update(self):
        self.animation()
        self.movement()