import pygame 
import sys
from assets.components.Button import Button


pygame.init()

#Initialize screen
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("TYPING ARMADA")

#Set start background
background_img = pygame.image.load("assets\images\start-background.jpg")
background_img = pygame.transform.smoothscale(background_img, (screen.get_width(), screen.get_height()))

sample_button = Button(450, 250, 200, 100)

#Game run
run = True

while run:
    screen.blit(background_img, (0, 0))
    sample_button.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    pygame.display.flip()

pygame.quit()
sys.exit()