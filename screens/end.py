import pygame 
import sys

pygame.init() 

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("TYPING ARMADA")

class Print_Score: 
    def __init__(self, score): 
        self.score = score
    def printscore(self): 
        screen.blit(self.score)  
 

class Button:
    def __init__(self, x, y, image, action):
        self.rect = image.get_rect(topleft=(x, y))  # Lấy rect từ kích thước của hình ảnh
        self.image = image  # Lưu hình ảnh gốc
        self.action = action  # Hành động khi nhấn nút

    def draw(self, screen):
        # Vẽ hình ảnh lên màn hình tại vị trí nút
        screen.blit(self.image, self.rect)

    def click(self, mouse_pos):
        # Kiểm tra nếu nút bị nhấn
        if self.rect.collidepoint(mouse_pos):
            self.action()  # Gọi hành động khi nút được nhấn

# Tạo các nút từ class Button với hình ảnh
def create_button(x, y, image, action):
    return Button(x, y, image, action)

def menu_action():
    print("Menu button clicked")

def restart_action():
    print("Restart button clicked")

color_text = (17, 98, 132)
font = pygame.font.Font("assets/fonts/Montserrat-ExtraBold.ttf", 45) 
score = 10000 # Điểm
#Chữ SCORE 
SCORE = font.render(str(score), True, color_text)


# Ảnh Background
background_image = pygame.image.load("assets/images/end-background.png") 
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

running = True

#Menu Button 
menu_image = pygame.image.load("assets/images/button images/menu-button.png")
#Restart Button
restart_image = pygame.image.load("assets/images/button images/restart-button.png")

button_width = menu_image.get_width()
button_height = menu_image.get_height()

menu_button = create_button(150, 800 - button_height - 220, menu_image, menu_action)
restart_button = create_button(535, 800 - button_height - 220, restart_image, restart_action)

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    
    mouse_pos = pygame.mouse.get_pos() #lấy vị trí chuột

    screen.blit(background_image, (0, 0)) #hiện Background
    screen.blit(SCORE,(525, 373)) #hiện điểm

    menu_button.draw(screen) #hiện nút menu
    restart_button.draw(screen) #hiện nút restart

    pygame.display.flip() 

pygame.quit()