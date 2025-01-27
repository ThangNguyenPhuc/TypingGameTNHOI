import pygame 
import sys
from assets.components.Button import Button
from screens.Battle import BattleScreen

pygame.init()
pygame.key.set_repeat(200, 10)

#Initialize clock
clock = pygame.time.Clock()

#Initialize window
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("TYPING ARMADA")


#Initialize screens
BATTLE = BattleScreen(screen)



#Game run
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    BATTLE.draw()
    BATTLE.handleKeyType()

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()