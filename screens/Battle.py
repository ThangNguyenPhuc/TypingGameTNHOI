import pygame
import sys
import random


class Enemy:
    def __init__(self, type, x, y, word):
        self.type = type
        self.x = x
        self.y = y    
        self.word = word
        self.speed = None
        if (type == "plane"):
            self.speed = 1
        else:
            self.speed = 0.5

        

class BattleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.backgroundImage = pygame.image.load("assets/images/battle-background.jpg")
        self.backgroundImage = pygame.transform.smoothscale(self.backgroundImage, (1000, 800))
        self.font = pygame.font.SysFont("Arial", 50)    
        self.typedText = ""

        self.sprites = []
        self.enemies = []
        
        

    def draw(self):
        self.screen.blit(self.backgroundImage, (0, 0))

        inputBox = pygame.Surface((600, 70), pygame.SRCALPHA)
        inputBox.fill((0, 0, 0, 180))
        self.screen.blit(inputBox, (200, 600))

        for enemy in self.enemies:
            enemyImage = None
            if enemy.type == "plane":
                enemyImage = pygame.image.load("assets/images/battle resources/aircraft.png")
                enemyImage = pygame.transform.smoothscale(enemyImage, (100, 100))
            else:
                enemyImage = pygame.image.load("assets/images/battle resources/ship.png")
                enemyImage = pygame.transform.smoothscale(enemyImage, (100, 50))

            self.screen.blit(enemyImage, (enemy.x, enemy.y))
        
            enemy.x -= enemy.speed
            
            

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.typedText = self.typedText[:-1]
                elif 'a' <= event.unicode <= 'z' or event.unicode == ' ':
                    self.typedText += event.unicode

        textShow = self.font.render(self.typedText, True, (255, 255, 255))
        self.screen.blit(textShow, (210, 605))


    def spawnEnemy(self):
        enemyType = random.randint(0, 1)
        rand_y = None
        
        if enemyType:
            rand_y = random.randint(0, 300)
            newEnemy = Enemy("plane", 900, rand_y, "something")
            self.enemies.append(newEnemy)
        else:
            rand_y = random.randint(420, 600)
            newEnemy = Enemy("ship", 900, rand_y, "something")
            self.enemies.append(newEnemy)

    