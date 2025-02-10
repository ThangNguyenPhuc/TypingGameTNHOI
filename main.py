import pygame 
import sys
from screens.Start import StartScreen
from screens.Battle import BattleScreen
from screens.Mode import ModeScreen
from screens.end import EndScreen
from screens.Settings import SettingScreen

pygame.init()
pygame.mixer.init()
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
START = StartScreen(screen)
BATTLE = BattleScreen(screen)
MODE = ModeScreen(screen)
END = EndScreen(screen)
SETTING = SettingScreen(screen)

screenList = {
    "start" : START,
    "battle" : BATTLE,
    "mode" : MODE,
    "end" : END,
    "setting" :  SETTING
}


#Music Setup
START_THEME = "assets/sounds/start_theme.mp3"
BATTLE_THEME = "assets/sounds/battle_theme.mp3"

def play_music(theme):
    pygame.mixer.music.load(theme)
    pygame.mixer.music.play(-1)

play_music(START_THEME)


def switchScreen(curScreen, u, v):

    if u == v:
        return curScreen

    #Tracking mode chosen
    diff = None
    if u == "mode":
        diff = curScreen.modeChosen

    #Getting score
    score = None
    if u == "battle":
        score = curScreen.score

    curScreen.switchScreen = u

    #Switch screen
    curScreen = screenList[v]    

    if v == "battle":
        curScreen.modeChosen = diff
        curScreen.reset()
        play_music(BATTLE_THEME)

    if v == "start" and u == "battle":
        play_music(START_THEME)

    if v == "end":
        curScreen.score = score
        play_music(START_THEME)

    curScreen.switchScreen = v
    

    return curScreen

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


    u = curScreen.switchScreen
    curScreen.draw()
    curScreen.handleEvents(events)
    v = curScreen.switchScreen

    if v == 'quit':
        run = False
        break

    curScreen = switchScreen(curScreen, u, v)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()