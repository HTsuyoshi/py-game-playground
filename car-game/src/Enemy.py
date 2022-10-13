import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, CAR_DIMENSION, SCREEN_DIMENSION):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/enemy.png'), (CAR_DIMENSION[0],CAR_DIMENSION[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(CAR_DIMENSION[0], SCREEN_DIMENSION[1] - CAR_DIMENSION[0]), - CAR_DIMENSION[1] // 2)
        self.dimension = CAR_DIMENSION
        self.screen = SCREEN_DIMENSION
        self.score = 0

    def update(self):
        self.rect.move_ip(0,10)
        if self.rect.top > self.screen[0]:
            self.rect.center = (random.randint(self.dimension[0], self.screen[1]- self.dimension[0]), - self.dimension[1] // 2)
            self.score += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
