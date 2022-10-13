import pygame
from pygame.locals import K_LEFT, K_RIGHT

class Player (pygame.sprite.Sprite):
    def __init__(self, CAR_DIMENSIONS, SCREEN_DIMENSION):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/kkarro.png'), (CAR_DIMENSIONS[0],CAR_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_DIMENSION[1] // 2, SCREEN_DIMENSION[0] - (CAR_DIMENSIONS[1] // 2))
        self.screen = SCREEN_DIMENSION

    def update(self):
        key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if key[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < self.screen[1]:
            if key[K_RIGHT]:
                self.rect.move_ip(5,0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
