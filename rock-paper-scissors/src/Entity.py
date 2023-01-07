import pygame
from random import randint

class Entity(pygame.sprite.Sprite):
    def __init__(self, d, screen_d):
        super().__init__()
        offset = randint(-10,10)
        self.dimension = (d[0] + offset, d[1] + offset)
        self.image = pygame.transform.scale(pygame.image.load('assets/rock.png'), (self.dimension[0], self.dimension[1])).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (randint(1 + self.dimension[0], screen_d[0] - 1 - self.dimension[0]), randint(1 + self.dimension[1], screen_d[1] - 1 - self.dimension[1]))
        self.screen = screen_d

    def paper(self):
        self.image = pygame.transform.scale(pygame.image.load('assets/paper.png'), (self.dimension[0], self.dimension[1])).convert_alpha()

    def rock(self):
        self.image = pygame.transform.scale(pygame.image.load('assets/rock.png'), (self.dimension[0], self.dimension[1])).convert_alpha()

    def scissors(self):
        self.image = pygame.transform.scale(pygame.image.load('assets/scissors.png'), (self.dimension[0], self.dimension[1])).convert_alpha()

    def update(self, attack, escape):
        distance = randint(1, 3)
        follow = randint(0,99)
        if follow < 64:
            self.random_walk(follow,distance)
        else:
            self.walk(attack, escape, distance)

    def fix_move(self, axis: tuple[int, int]):
        y = axis[1]
        x = axis[0]
        if y + self.rect.centery + (self.dimension[1] / 2) >= self.screen[1] or y + self.rect.centery - (self.dimension[1] / 2) <= 0:
            y = - y
        if x + self.rect.centerx + (self.dimension[0] / 2) >= self.screen[0] or x + self.rect.centerx - (self.dimension[0] / 2) <= 0:
            x = - x
        return (x, y)

    def random_walk(self, follow: int, distance: int):
        from itertools import product
        prod = [*product((-1,0,1), (-1,0,1))]
        move = prod[follow % len(prod)]
        move = self.fix_move(move)
        self.rect.move_ip(move[0] * distance, move[1] * distance)

    def walk(self, attack_list, escape_list, distance: int):
        import numpy as np
        attack = None
        attack_dist = 1000000
        for a in attack_list:
            p1 = np.array(self.rect.center)
            p2 = np.array(a.rect.center)
            dist = np.linalg.norm(p1 - p2)
            if dist < attack_dist:
                attack_dist = dist
                attack = a

        escape = None
        escape_dist = 1000000
        for e in escape_list:
            p1 = np.array(self.rect.center)
            p2 = np.array(e.rect.center)
            dist = np.linalg.norm(p1 - p2)
            if dist < escape_dist:
                escape_dist = dist
                escape = e

        x, y = 0, 0
        if attack != None:
            y += distance * np.sign(attack.rect.centery - self.rect.centery)
            x += distance * np.sign(attack.rect.centerx - self.rect.centerx)

        if escape != None:
            y -= distance * np.sign(escape.rect.centery - self.rect.centery)
            x -= distance * np.sign(escape.rect.centerx - self.rect.centerx)

        x, y = self.fix_move((x, y))
        self.rect.move_ip(x, y)



    def draw(self, surface):
        surface.blit(self.image, self.rect)
