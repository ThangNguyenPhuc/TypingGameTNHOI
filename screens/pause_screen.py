import pygame
import sys
pygame.init()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TYPING ARMADA")
# khoi tao man hinh

class Frame:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft =(x, y))
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, self.rect)



class Button:
    def __init__(self, x, y, image, action):
        self.rect = image.get_rect(topleft =(x, y))
        self.image = image
        self.action = action
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.action()

def restart_action():
    print("do something")

def resume_action():
    print("do something")

def quit_action():
    pygame.quit()
    sys.exit()

def pause_action():
    print("do something")


background_image = pygame.image.load("assets/images/start-background.jpg")
background_image = pygame.transform.scale(background_image,(screen_width, screen_height))
pause_frame_image = pygame.image.load("assets/images/pause-frame.png")
resume_image = pygame.image.load("assets/images/button images/resume-button.png")
restart_imamge = pygame.image.load("assets/images/button images/restart-button.png")
quit_image = pygame.image.load("assets/images/button images/quit-button.png")
pause_image = pygame.image.load("assets/images/button images/pause-button.png")
# tai hinh xuong

button_width, button_height = resume_image.get_width(), resume_image.get_height() 
button_x, button_y = (screen_width - button_width) // 2  , (screen_height - button_height) // 2 - 60

# tap cac doi tuong
pause_x, pause_y = (screen_width - pause_frame_image.get_width()) // 2, (screen_height - pause_frame_image.get_height()) // 2
pause_frame = Frame(pause_x, pause_y, pause_frame_image)
delta = 100
resume_button = Button(button_x, button_y, resume_image, resume_action)
restart_button = Button(button_x, (button_y) + delta, restart_imamge, restart_action)
quit_button = Button(button_x, button_y + 2*delta, quit_image, quit_action)
pause_button = Button(screen_width - 75, 10, pause_image, pause_action)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                resume_button.click(event.pos)
                restart_button.click(event.pos)
                quit_button.click(event.pos)
                #  pause_button.click(event.pos) tam thoi khong dung nut pause 



    # ve background
    screen.blit(background_image, (0,0))

    # ve khung pause
    pause_frame.draw(screen)

    # ve 4 nut resume, restart, quit cp, pause
    resume_button.draw(screen)
    restart_button.draw(screen)
    quit_button.draw(screen)
    # pause_button.draw(screen) khong ve nut pause




    pygame.display.flip()



pygame.quit()
sys.exit()