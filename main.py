import pygame 
import sys
from screens.Start import StartScreen
from screens.Battle import BattleScreen
from screens.Pause import PauseScreen


pygame.init()
pygame.key.set_repeat(300, 100)

#Initialize clock
clock = pygame.time.Clock()

#Initialize window
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("TYPING ARMADA")

#Battle Screen Customize Events
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 4000)


#Initialize screens
START = StartScreen(screen)
BATTLE = BattleScreen(screen)
PAUSE = PauseScreen(screen)

screenList = {
    "start" : START,
    "battle" : BATTLE,
    "pause" : PAUSE
}

curScreen = START

#Game run
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

        if curScreen == BATTLE and event.type == ADDENEMY:
            curScreen.spawnEnemy()

    curTime = pygame.time.get_ticks() / 1000

    #Switch screen
    if curScreen.switchScreen == "quit":
        run = False

    curScreen = screenList[curScreen.switchScreen]
    

    curScreen.draw()
    curScreen.handleEvents(events)

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()