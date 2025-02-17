import pygame
import sys


pygame.mixer.init()

class Button:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft=(x, y))  # Lấy rect từ kích thước của hình ảnh
        self.image = image  # Lưu hình ảnh gốc

    def draw(self, screen):
        # Vẽ hình ảnh lên màn hình tại vị trí nút
        screen.blit(self.image, self.rect)





class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/start-background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 800))
        self.switchScreen = "start"

        self.volume = 1.0
        self.clickEffect = pygame.mixer.Sound("assets/sounds/button_clicked.mp3")

    
    def draw(self):
        game_title_image = pygame.image.load("assets/images/name-game.png")
        
        #Draw background and game title
        self.screen.blit(self.background_image, (0, 0)) 
        self.screen.blit(game_title_image, ((1000 - game_title_image.get_width()) // 2, 50)) 

        #Load buttons images
        play_image = pygame.image.load("assets/images/button images/battle-button.png")  
        settings_image = pygame.image.load("assets/images/button images/settings-button.png") 
        guide_image = pygame.image.load("assets/images/button images/guide-button.png") 
        quit_image = pygame.image.load("assets/images/button images/quit-button.png") 


        #Sizing and positioning buttons
        button_width = play_image.get_width()
        button_height = play_image.get_height()

        button_x = (1000 - button_width) // 2  # Căn giữa theo chiều ngang
        button_y_start = 120 + (800 - (button_height * 4 + 30 * 3)) // 2

        #Create buttons
        self.play_button = Button(button_x, button_y_start, play_image)
        self.settings_button = Button(button_x, button_y_start + button_height + 30, settings_image)
        self.guide_button = Button(button_x, button_y_start + 2 * (button_height + 30), guide_image)
        self.quit_button = Button(button_x, button_y_start + 3 * (button_height + 30), quit_image)

        #Draw buttons
        self.play_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.guide_button.draw(self.screen)
        self.quit_button.draw(self.screen)

    def handleEvents(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clickEffect.set_volume(self.volume)
                    if self.clicked(self.play_button, event.pos):
                        self.clickEffect.play()
                        self.handlePlay()
                    if self.clicked(self.settings_button, event.pos):
                        self.clickEffect.play()
                        self.handleSettings()
                    if self.clicked(self.guide_button, event.pos):
                        self.clickEffect.play()                   
                        self.handleGuide()
                    if self.clicked(self.quit_button, event.pos):
                        self.clickEffect.play()
                        self.handleQuit()

    def clicked(self, button, pos):
        return button.rect.collidepoint(pos)
            


    def handlePlay(self):
        self.switchScreen = "newplayer"

    def handleSettings(self):
        self.switchScreen = "setting"

    def handleGuide(self):
        self.switchScreen = "guide"

    def handleQuit(self):
        self.switchScreen = "quit"