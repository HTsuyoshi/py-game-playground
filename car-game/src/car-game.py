import sys, time

import pygame
from pygame.locals import QUIT

import Player, Enemy

FPS = pygame.time.Clock()
ICON = pygame.image.load("./assets/icon.png")

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 800
SCREEN_DIMENSION = (SCREEN_HEIGHT, SCREEN_WIDTH)
SPEED = 5

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('assets/background.png')

CAR_DIMENSIONS = (50,100)

if __name__ == '__main__':
    pygame.init()

    FONT = pygame.font.SysFont("Source Code Variable", 30)
    FONT_SMALL = pygame.font.SysFont("Source Code Variable", 20)
    GAME_OVER = FONT.render("Game Over", True, BLACK)

    pygame.display.set_icon(ICON)
    pygame.display.set_caption("Car game")

    P = Player.Player(CAR_DIMENSIONS, SCREEN_DIMENSION)
    E = Enemy.Enemy(CAR_DIMENSIONS, SCREEN_DIMENSION)

    ALL_E = pygame.sprite.Group()
    ALL_E.add(E)
    ALL = pygame.sprite.Group()
    ALL.add(P)
    ALL.add(E)

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    while True:
        #P.update(SCREEN_WIDTH)
        #E.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        #DISPLAYSURF.fill(WHITE)
        #P.draw(DISPLAYSURF)
        #E.draw(DISPLAYSURF)

        DISPLAYSURF.blit(BACKGROUND, (0,0))

        SCORE = 0
        for E in ALL_E:
            SCORE += E.score
        scores = FONT_SMALL.render(str(SCORE), True, BLACK)
        DISPLAYSURF.blit(scores, (SCREEN_WIDTH // 2, 20))

        for A in ALL:
            DISPLAYSURF.blit(A.image, A.rect)
            A.update()

        if pygame.sprite.spritecollideany(P, ALL_E):
            DISPLAYSURF.blit(GAME_OVER, (70, SCREEN_HEIGHT // 2))
            pygame.display.update()
            for A in ALL:
                A.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit(0)

        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 2

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()
        FPS.tick(60)
