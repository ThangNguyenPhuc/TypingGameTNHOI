import pygame 
import sys
from assets.components.Button import Button
from screens.Battle import BattleScreen

pygame.init()
pygame.key.set_repeat(300, 100)

#Initialize clock
clock = pygame.time.Clock()

#Initialize window
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("TYPING ARMADA")

#Battle Screen Customize Events
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2000)


#Initialize screens
BATTLE = BattleScreen(screen)


#Game run
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

        if event.type == ADDENEMY:
            BATTLE.spawnEnemy()

    curTime = pygame.time.get_ticks() / 1000

    BATTLE.draw()
    BATTLE.handleEvents(events)

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()