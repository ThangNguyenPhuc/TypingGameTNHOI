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

class GuideScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/guide-background.png")
        
        self.volume = 1.0
        self.switchScreen = "guide"

        self.clickEffect = pygame.mixer.Sound("assets/sounds/button_clicked.mp3")

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        ok_image = pygame.image.load("assets/images/button images/ok-button.png")
        self.OKButton = Button(400, 650, ok_image)

        self.OKButton.draw(self.screen)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clickEffect.set_volume(self.volume)
                    if self.OKButton.clicked(event.pos):
                        self.clickEffect.play()
                        self.handleOK()
    def handleOK(self):
        self.switchScreen = "start"
