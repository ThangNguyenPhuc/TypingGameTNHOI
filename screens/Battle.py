import pygame
import sys

from assets.components.TypingMechanics import TypingArea

class BattleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.backgroundImage = pygame.image.load("assets/images/battle-bg.jpg")
        self.backgroundImage = pygame.transform.smoothscale(self.backgroundImage, (1000, 600))
        self.font = pygame.font.Font(None, 50)
        self.typedText = ""
        self.keyPressed = None
        

    def draw(self):
        # screen.blit(self.backgroundImage, (0, 0))
        self.screen.fill((255, 255, 255))

        
        inputBox = pygame.Surface((600, 70), pygame.SRCALPHA)
        inputBox.fill((0, 0, 0, 1))
        self.screen.blit(inputBox, (200, 400))


    def handleKeyType(self):
        pass