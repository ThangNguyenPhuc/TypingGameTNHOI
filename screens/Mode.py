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
    def __init__(self, x, y, image, action):
        self.rect = image.get_rect(topleft = (x, y))
        self.image = image
        self.action = action
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.action()

class ModeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/start-background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))
        self.switchScreen = "mode"
        

    def draw(self):
        #Draw background 
        self.screen.blit(self.background_image, (0,0))

        #Load button images
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

        #Create buttons
        self.easy_button = Button(button_x, button_y, easy_image, easy_action)
        self.hard_button = Button(button_x, button_y + delta, hard_image, hard_action)
        self.insane_button = Button(button_x, button_y + 2*delta, insane_image, insane_action)
        self.medium_button = Button(button_x, button_y + 3*delta, medium_image, medium_action)

        #Draw button
        difficulties_box.draw(self.screen)
        self.easy_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.insane_button.draw(self.screen)
        self.medium_button.draw(self.screen)

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

    def easy_action():
        print("I am very sad")

    def hard_action():
        print("I don't want to go to school")

    def insane_action():
        print("i cry a lot")

    def medium_action():
        print("i don't want to do anything")