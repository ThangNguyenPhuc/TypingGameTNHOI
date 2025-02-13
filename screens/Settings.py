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


class SettingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.backgroundImage = pygame.image.load("assets/images/setting-background.png")

        self.volume = 1.0
        self.switchScreen = "setting"

        self.clickEffect = pygame.mixer.Sound("assets/sounds/button_clicked.mp3")

        
    def draw(self):
        #Draw background
        self.screen.blit(self.backgroundImage, (0, 0))

        plus_image = pygame.image.load("assets/images/button images/increase-button.png")
        minus_image = pygame.image.load("assets/images/button images/decrease-button.png")
        ok_image = pygame.image.load("assets/images/button images/ok-button.png")

        self.plusButton = Button(650, 365, plus_image)
        self.minusButton = Button(450, 365, minus_image)
        self.OKButton = Button(400, 550, ok_image)

        self.plusButton.draw(self.screen)
        self.minusButton.draw(self.screen)
        self.OKButton.draw(self.screen)

        font = pygame.font.Font("assets/fonts/Montserrat-ExtraBold.ttf", 45)
        volumeText = font.render(str(int(self.volume * 100)) + "%", True, (0, 0, 0))

        self.screen.blit(volumeText, (525, 365)) 


    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clickEffect.set_volume(self.volume)
                    if self.plusButton.clicked(event.pos):
                        self.clickEffect.play()
                        self.increaseVolume()
                    if self.minusButton.clicked(event.pos):
                        self.clickEffect.play()
                        self.decreaseVolume()
                    if self.OKButton.clicked(event.pos):
                        self.clickEffect.play()
                        self.quitSetting()

    def increaseVolume(self):
        if self.volume < 1:
            self.volume += 0.2
        
    def decreaseVolume(self):
        if self.volume > 0:
            self.volume -= 0.2
        
    def quitSetting(self):
        self.switchScreen = "start"