import pygame
import sys

pygame.init()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TYPING ARMADA")

class Frame:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft =(x, y))
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Button:
    def __init__(self, x, y, image, action):
        self.rect = image.get_rect(topleft = (x, y))
        self.image = image
        self.action = action
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.action()

def easy_action():
    print("I am very sad")

def hard_action():
    print("I don't want to go to school")

def insane_action():
    print("i cry a lot")

def medium_action():
    print("i don't want to do anything")

background_image = pygame.image.load("assets/images/start-background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
difficulties_box_image = pygame.image.load("assets/images/difficulties images/difficulties-box.png")
easy_image = pygame.image.load("assets/images/difficulties images/easy-button.png")
hard_image = pygame.image.load("assets/images/difficulties images/hard-button.png")
insane_image = pygame.image.load("assets/images/difficulties images/insane-button.png")
medium_image = pygame.image.load("assets/images/difficulties images/medium-button.png")

frame_width, frame_height = difficulties_box_image.get_width(), difficulties_box_image.get_height()
frame_x, frame_y = (screen_width - frame_width) // 2, (screen_height - frame_height) // 2 
difficulties_box = Frame(frame_x, frame_y, difficulties_box_image)

button_width, button_height = easy_image.get_width(), easy_image.get_height()
button_x, button_y = (screen_width - button_width) // 2, (screen_height - button_height) // 2 - 80

delta = 90

easy_button = Button(button_x, button_y, easy_image, easy_action)
hard_button = Button(button_x, button_y + delta, hard_image, hard_action)
insane_button = Button(button_x, button_y + 2*delta, insane_image, insane_action)
medium_button = Button(button_x, button_y + 3*delta, medium_image, medium_action)




running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):
                easy_button.click(event.pos)
                hard_button.click(event.pos)
                insane_button.click(event.pos)
                medium_button.click(event.pos)

    

    screen.blit(background_image, (0,0))
    difficulties_box.draw(screen)
    easy_button.draw(screen)
    hard_button.draw(screen)
    insane_button.draw(screen)
    medium_button.draw(screen)

    pygame.display.flip() 

pygame.quit()
sys.exit()