import pygame
import symtable

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
        self.background_image = pygame.image.load("assets/images/end-background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 800))
        self.switchScreen = "end"
        #self.score = score
    
    def draw(self, score):
        game_title_image = pygame.image.load("assets/images/name-game.png")
        font = pygame.font.Font("assets/fonts/Montserrat-ExtraBold.ttf", 45)
        SCORE = font.render(str(score), True, (17, 98, 132))
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
                if self.clicked(self.menu_button, event.pos):
                    self.handleMenu()
                if self.clicked(self.restart_button, event.pos):
                    self.handleBattle() 
    
    def clicked(self, button, pos):
        return button.rect.collidepoint(pos)
    
    def handleMenu(self):
        self.switchScreen = "start"
    
    def handleBattle(self):
        self.switchScreen = "battle"
    