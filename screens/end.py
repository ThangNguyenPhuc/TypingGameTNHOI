import pygame

pygame.mixer.init()

class Button: 
    def __init__(self, x, y, image): 
        self.rect = image.get_rect(topleft = (x,y)) 
        self.image = image # Lưu hình ảnh gốc

    def draw(self, screen): 
        #Vẽ hình ảnh lên màn hình tại vì trí nút
        screen.blit(self.image, self.rect)

class EndScreen: 
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/end-background.png")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 800))
        self.switchScreen = "end"
        self.score = None

        self.volume = 1.0
        self.clickEffect = pygame.mixer.Sound("assets/sounds/button_clicked.mp3")

    
    def draw(self):
        font = pygame.font.Font("assets/fonts/Montserrat-ExtraBold.ttf", 40)
        SCORE = font.render(str(self.score), True, (17, 98, 132))

        #Draw background and game title
        self.screen.blit(self.background_image, (0, 0)) 
        
        #Load buttons images
        menu_image = pygame.image.load("assets/images/button images/menu-button.png")  
        restart_image = pygame.image.load("assets/images/button images/restart-button.png") 
        
        #Sizing 
        button_width = menu_image.get_width() 
        button_height = menu_image.get_height() 

        #Create buttons 
        self.menu_button = Button(150, 800 - button_height - 220, menu_image)
        self.restart_button = Button(535, 800 - button_height - 220, restart_image)

        #Draw buttons
        self.menu_button.draw(self.screen) 
        self.restart_button.draw(self.screen) 
        #Draw Score 
        self.screen.blit(SCORE,(525, 373)) 

    def handleEvents(self, events):
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clickEffect.set_volume(self.volume)
                    if self.clicked(self.menu_button, event.pos):
                        self.clickEffect.play()
                        self.handleMenu()
                    if self.clicked(self.restart_button, event.pos):
                        self.clickEffect.play()
                        self.handleRestart() 
    
    def clicked(self, button, pos):
        return button.rect.collidepoint(pos)
    
    def handleMenu(self):
        self.switchScreen = "start"
    
    def handleRestart(self):
        self.switchScreen = "mode"
    