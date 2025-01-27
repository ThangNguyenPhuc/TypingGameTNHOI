import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Thiết lập cửa sổ hiển thị với kích thước 1000x800
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Class Button với hình ảnh và bo tròn góc
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

# Các hành động của từng nút
def play_action():
    print("Play button clicked")
    # Thêm hành động cho nút Play, ví dụ như bắt đầu game...

def settings_action():
    print("Settings button clicked")
    # Thêm hành động cho nút Settings, ví dụ như mở màn Settings...

def guide_action():
    print("Guide button clicked")
    # Thêm hành động cho nút Guide, ví dụ như hiển thị hướng dẫn...

def quit_action():
    print("Quit button clicked")
    pygame.quit()
    sys.exit()  # Thoát game khi nhấn Quit

# Tải các hình ảnh cho các nút
play_image = pygame.image.load("assets/images/button images/battle-button.png")  # Thay thế đường dẫn thực tế
settings_image = pygame.image.load("assets/images/button images/guide-button.png")  # Thay thế đường dẫn thực tế
guide_image = pygame.image.load("assets/images/button images/settings-button.png")  # Thay thế đường dẫn thực tế
quit_image = pygame.image.load("assets/images/button images/quit-button.png")  # Thay thế đường dẫn thực tế

# Tải hình ảnh nền
background_image = pygame.image.load("assets/images/start-background.jpg")  # Thay thế đường dẫn thực tế
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Tải hình ảnh tên game (thay đường dẫn đúng với hình ảnh của bạn)
game_title_image = pygame.image.load("assets/images/name-game.png")  # Thay thế với tên file hình ảnh tên game của bạn

# Lấy chiều dài và chiều rộng của play_image (hoặc bất kỳ hình ảnh nào bạn muốn sử dụng)
button_width = play_image.get_width()
button_height = play_image.get_height()

# Tính vị trí căn giữa màn hình cho các nút
button_x = (screen_width - button_width) // 2  # Căn giữa theo chiều ngang
button_y_start = 120 + (screen_height - (button_height * 4 + 30 * 3)) // 2  # Căn giữa theo chiều dọc (giữa các nút)

# Tạo các nút với hình ảnh đã bo tròn góc
play_button = create_button(button_x, button_y_start, play_image, play_action)
settings_button = create_button(button_x, button_y_start + button_height + 30, settings_image, settings_action)
guide_button = create_button(button_x, button_y_start + 2 * (button_height + 30), guide_image, guide_action)
quit_button = create_button(button_x, button_y_start + 3 * (button_height + 30), quit_image, quit_action)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Chuột trái được nhấn
                # Kiểm tra và gọi hành động khi nút được nhấn
                play_button.click(event.pos)
                settings_button.click(event.pos)
                guide_button.click(event.pos)
                quit_button.click(event.pos)

    # Lấy vị trí chuột
    mouse_pos = pygame.mouse.get_pos()

    # Vẽ hình ảnh nền lên màn hình (lấp đầy toàn bộ màn hình)
    screen.blit(background_image, (0, 0))  # Vị trí (0, 0) sẽ khiến hình ảnh nền lấp đầy toàn bộ màn hình

    # Vẽ hình ảnh tên game lên màn hình
    screen.blit(game_title_image, ((screen_width - game_title_image.get_width()) // 2, 50))  # Căn giữa tên game

    # Vẽ các nút lên màn hình
    play_button.draw(screen)
    settings_button.draw(screen)
    guide_button.draw(screen)
    quit_button.draw(screen)

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát pygame
pygame.quit()
sys.exit()
