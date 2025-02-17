import pygame

pygame.mixer.init()

class Button:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft=(x, y))  # Lấy rect từ kích thước của hình ảnh
        self.image = image  # Lưu hình ảnh gốc

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


class NewPlayerScreen:
    def __init__(self, screen):
        self.screen = screen
        self.backgroundImage = pygame.image.load("assets/images/newplayer-background.png")

        self.volume = 1.0
        self.switchScreen = "newplayer"

        self.clickEffect = pygame.mixer.Sound("assets/sounds/button_clicked.mp3")

        
    def draw(self):
        #Draw background
        self.screen.blit(self.backgroundImage, (0, 0))

        yes_image = pygame.image.load("assets/images/button images/yes-button.png")
        no_image = pygame.image.load("assets/images/button images/no-button.png")

        self.yesButton = Button(275, 450, yes_image)
        self.noButton = Button(525, 450, no_image)


        self.yesButton.draw(self.screen)
        self.noButton.draw(self.screen)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clickEffect.set_volume(self.volume)
                    if self.yesButton.clicked(event.pos):
                        self.clickEffect.play()
                        self.handleYes()
                    if self.noButton.clicked(event.pos):
                        self.clickEffect.play()
                        self.handleNo()
                    
    def handleYes(self):
        self.switchScreen = "guide"
        
    def handleNo(self):
        self.switchScreen = "mode"
