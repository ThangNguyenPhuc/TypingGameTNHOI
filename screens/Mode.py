import pygame
import sys

screen_width, screen_height = 1000, 800

class Frame:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft =(x, y))
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Button:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft = (x, y))
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class ModeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/start-background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))
        self.switchScreen = "mode"
        self.modeChosen = None
        

    def draw(self):
        #Draw background 
        self.screen.blit(self.background_image, (0,0))

        #Load button images
        difficulties_box_image = pygame.image.load("assets/images/difficulties images/difficulties-box.png")
        easy_image = pygame.image.load("assets/images/difficulties images/easy-button.png")
        medium_image = pygame.image.load("assets/images/difficulties images/medium-button.png")
        hard_image = pygame.image.load("assets/images/difficulties images/hard-button.png")
        insane_image = pygame.image.load("assets/images/difficulties images/insane-button.png")
        
        frame_width, frame_height = difficulties_box_image.get_width(), difficulties_box_image.get_height()
        frame_x, frame_y = (screen_width - frame_width) // 2, (screen_height - frame_height) // 2 
        difficulties_box = Frame(frame_x, frame_y, difficulties_box_image)

        button_width, button_height = easy_image.get_width(), easy_image.get_height()
        button_x, button_y = (screen_width - button_width) // 2, (screen_height - button_height) // 2 - 80

        delta = 90

        #Create buttons
        self.easy_button = Button(button_x, button_y, easy_image)
        self.medium_button = Button(button_x, button_y + delta, medium_image)
        self.hard_button = Button(button_x, button_y + 2 * delta, hard_image)
        self.insane_button = Button(button_x, button_y + 3 * delta, insane_image)

        #Draw button
        difficulties_box.draw(self.screen)
        self.easy_button.draw(self.screen)
        self.medium_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.insane_button.draw(self.screen)

    def handleEvents(self, events):
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    if self.clicked(self.easy_button, event.pos):
                        self.easy_action()
                    if self.clicked(self.medium_button, event.pos):
                        self.medium_action()
                    if self.clicked(self.hard_button, event.pos):
                        self.hard_action()
                    if self.clicked(self.insane_button, event.pos):
                        self.insane_action()

    def clicked(self, button, pos):
        return button.rect.collidepoint(pos)

    def easy_action(self):
        self.switchScreen = "battle"
        self.modeChosen = 0

    def medium_action(self):
        self.switchScreen = "battle"
        self.modeChosen = 1
        
    def hard_action(self):
        self.switchScreen = "battle"
        self.modeChosen = 2

    def insane_action(self):
        self.switchScreen = "battle"
        self.modeChosen = 3
    