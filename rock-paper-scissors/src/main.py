### Configs ###

SCREEN = 800
SPRITE = SCREEN // 20

import sys
from random import randint
import pygame
from pygame.locals import QUIT, DOUBLEBUF
from Entity import Entity

FLAGS = DOUBLEBUF
DISPLAYSURF = pygame.display.set_mode((SCREEN,SCREEN), FLAGS, 16)
pygame.event.set_allowed([QUIT])
IMG_ROCK = pygame.image.load('assets/rock.png')
IMG_PAPER = pygame.image.load('assets/paper.png')
IMG_SCISSORS = pygame.image.load('assets/scissors.png')

FPS = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_icon(pygame.image.load('./assets/rock.png'))
    pygame.display.set_caption('RPS simulator')

    rocks = pygame.sprite.Group()
    for _ in range(randint(10, 30)):
        r = Entity((SPRITE, SPRITE), (SCREEN, SCREEN))
        r.rock(IMG_ROCK)
        rocks.add(r)

    papers = pygame.sprite.Group()
    for _ in range(randint(10, 30)):
        p = Entity((SPRITE, SPRITE), (SCREEN, SCREEN))
        p.paper(IMG_PAPER)
        papers.add(p)

    scissors = pygame.sprite.Group()
    for _ in range(randint(10, 30)):
        s = Entity((SPRITE, SPRITE), (SCREEN, SCREEN))
        s.scissors(IMG_SCISSORS)
        scissors.add(s)

    while 1:
        DISPLAYSURF.fill((255,255,255))

        for r in rocks:
            r.update(attack=scissors, escape=papers)
            if pygame.sprite.spritecollideany(r, papers):
                rocks.remove(r)
                r.paper(IMG_PAPER)
                papers.add(r)
            r.draw(DISPLAYSURF)

        for p in papers:
            p.update(attack=rocks, escape=scissors)
            if pygame.sprite.spritecollideany(p, scissors):
                papers.remove(p)
                p.scissors(IMG_SCISSORS)
                scissors.add(p)
            p.draw(DISPLAYSURF)

        for s in scissors:
            s.update(attack=papers, escape=rocks)
            if pygame.sprite.spritecollideany(s, rocks):
                scissors.remove(s)
                s.rock(IMG_ROCK)
                rocks.add(s)
            s.draw(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()
        FPS.tick(60)
    pass
