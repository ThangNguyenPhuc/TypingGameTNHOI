import pygame
import sys

class Frame:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft =(x, y))
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, self.rect)



class Button:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft =(x, y))
        self.image = image
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class PauseScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/start-background.jpg")
        self.background_image = pygame.transform.scale(self.background_image,(1000, 800))

    def draw(self):
        #Draw background
        self.screen.blit(self.background_image, (0,0))

        #Load images
        pause_frame_image = pygame.image.load("assets/images/pause-frame.png")
        resume_image = pygame.image.load("assets/images/button images/resume-button.png")
        restart_image = pygame.image.load("assets/images/button images/restart-button.png")
        quit_image = pygame.image.load("assets/images/button images/quit-button.png")

        #Sizing
        button_width, button_height = resume_image.get_width(), resume_image.get_height() 
        button_x, button_y = (1000 - button_width) // 2  , (800 - button_height) // 2 - 60

        #Create buttons
        pause_x, pause_y = (1000 - pause_frame_image.get_width()) // 2, (800 - pause_frame_image.get_height()) // 2
        pause_frame = Frame(pause_x, pause_y, pause_frame_image)
        delta = 100
        self.resume_button = Button(button_x, button_y, resume_image)
        self.restart_button = Button(button_x, (button_y) + delta, restart_image)
        self.quit_button = Button(button_x, button_y + 2*delta, quit_image)

        #Draw buttons
        pause_frame.draw(self.screen)

        self.resume_button.draw(self.screen)
        self.restart_button.draw(self.screen)
        self.quit_button.draw(self.screen)
 
    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.clicked(self.resume_button, event.pos):
                        self.handleResume()
                    if self.clicked(self.restart_button, event.pos):
                        self.handleRestart()
                    if self.clicked(self.quit_button, event.pos):
                        self.handleQuit()

    def clicked(self, button, pos):
        return button.rect.collidepoint(pos)
    
    def handleResume(self):
        pass
    
    def handleRestart(self):
        pass

    def handleQuit(self):
        self.switchScreen = "start"