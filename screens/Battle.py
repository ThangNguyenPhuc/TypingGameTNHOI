import pygame
import sys
import random
import math

#Open glossaries
easyFile = open("assets/glossary/EASY.txt")
# mediumFile = open("assets/glossary/MEDIUM.txt")
# hardFile = open("assets/glossary/HARD.txt")
# insaneFile = open("assets/glossary/INSANE.txt")


class Player:
    def __init__(self):
        self.health = 500
        self.position = (150, 450)

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

        self.state = 'moving'


class Torpedo:
    def __init__(self, start, end, targetWord):
        self.startPos = pygame.Vector2(start[0], start[1])
        self.endPos = pygame.Vector2(end[0], end[1])
        self.interpolate = 0.0
        self.speed = 0.03
        self.target = targetWord
        
class Explosion:
    def __init__(self, pos, type, timeStart):
        self.startTime = timeStart  
        self.type = type
        self.position = pos  

class BattleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.backgroundImage = pygame.image.load("assets/images/battle-background.jpg")
        self.backgroundImage = pygame.transform.smoothscale(self.backgroundImage, (1000, 800))
        self.font = pygame.font.SysFont("Arial", 50)    
        self.typedText = ""

        self.player = Player()

        self.sprites = []
        self.enemies = []
        self.torpedoes = []
        self.explosions = []

        self.glossaries = []

        self.glossaries.append(easyFile.readlines())

        for idx in range(len(self.glossaries[0])):
            self.glossaries[0][idx] = self.glossaries[0][idx][:-1]


    def draw(self):
        self.screen.blit(self.backgroundImage, (0, 0))

        inputBox = pygame.Surface((600, 70), pygame.SRCALPHA)
        inputBox.fill((0, 0, 0, 180))
        self.screen.blit(inputBox, (200, 600))

        #Draw player character
        player = pygame.image.load("assets/images/battle resources/player-character.png")
        player = pygame.transform.smoothscale(player, (100, 100))
        self.screen.blit(player, self.player.position)

        #Draw enemies
        for enemy in self.enemies:
            enemyImage = None
            if enemy.type == "plane":
                enemyImage = pygame.image.load("assets/images/battle resources/aircraft.png")
                enemyImage = pygame.transform.smoothscale(enemyImage, (100, 100))
            else:
                enemyImage = pygame.image.load("assets/images/battle resources/ship.png")
                enemyImage = pygame.transform.smoothscale(enemyImage, (100, 50))

            #Create word on screen
            enemyFont = pygame.font.SysFont("Arial", 30)
            enemyWord = enemyFont.render(enemy.word, True, (255, 0, 0))

            #Define word postition
            wordPos = (enemy.x + 50 - (enemyWord.get_width()) // 2, enemy.y - (40 if enemy.type == "ship" else 20))
            
            #Draw objects
            self.screen.blit(enemyWord, wordPos)
            self.screen.blit(enemyImage, (enemy.x, enemy.y))
            
        #Draw health bar
        barLength = self.player.health * 6 // 5
        healthBar = pygame.Surface((barLength, 20))
        healthBar.fill((255, 0, 0))
        self.screen.blit(healthBar, (200, 50))

        #Draw torpedoes
        for idx in range(len(self.torpedoes)):
            torpedoImage = pygame.image.load("assets/images/battle resources/torpedo.png")
            torpedoImage = pygame.transform.smoothscale(torpedoImage, (50, 50))


            torpedo = self.torpedoes[idx]

            itpl = torpedo.interpolate
            speed = torpedo.speed
            A = torpedo.startPos; B = torpedo.endPos

            self.torpedoes[idx].interpolate = min(itpl + speed, 1.0)

            curPos = A.lerp(B, torpedo.interpolate)

            #Rotate 45 degrees
            torpedoImage = pygame.transform.rotate(torpedoImage, 40.0)
            rectBox = torpedoImage.get_rect(center=(curPos.x, curPos.y))

            #Point direction to enemy
            tanRatio = (A.y - B.y) / (A.x - B.x)
            angle = 0 - math.degrees(math.atan(tanRatio))

            torpedoImage = pygame.transform.rotate(torpedoImage, angle)
            rectBox = torpedoImage.get_rect(center=(curPos.x, curPos.y))

            #Draw
            self.screen.blit(torpedoImage, rectBox.topleft)

        #Draw explosions
        idxx = 0
        while idxx < len(self.explosions): 
            if (idxx >= len(self.explosions)):
                break
            explosion = self.explosions[idxx]
            explosionImageURL = None
            if explosion.type == "plane":
                explosionImageURL = "assets/images/battle resources/plane-explode.jpg"
            else:
                explosionImageURL = "assets/images/battle resources/ship-explode.jpg"
            explosionImage = pygame.image.load(explosionImageURL)
            explosionImage = pygame.transform.smoothscale(explosionImage, (100, 100))

            #Explosion time exceeded 1s
            if pygame.time.get_ticks() - explosion.startTime > 1000:
                self.explosions.pop(idxx)
                continue

            self.screen.blit(explosionImage, explosion.position)
            idxx += 1

        #Handle enemy events
        idx = 0
        while idx < len(self.enemies):
            enemy = self.enemies[idx]
            #Word match with enemy words
            if self.typedText == enemy.word:
                self.typedText = ""
                self.enemies[idx].speed = 0   
                newTorpedo = Torpedo((250, 550), (enemy.x + 50, enemy.y + (50 if enemy.type == "plane" else 25)), enemy.word)     
                self.torpedoes.append(newTorpedo) 


            #Enemy reach border check
            if enemy.x >= 250:
                self.enemies[idx].x -= enemy.speed
                idx += 1
            else:
                self.enemies.pop(idx)
                self.player.health -= 20
            
        #Handle torpedo touch enemy
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(self.torpedoes):
            popped = False
            while idx2 < len(self.enemies):
        
                if idx1 >= len(self.torpedoes) or idx2 >= len(self.enemies):
                    break
                
                torpedo = self.torpedoes[idx1]
                enemy = self.enemies[idx2]

                if torpedo.target == enemy.word and torpedo.interpolate == 1.0:
                    #Explode animation
                    newExplosion = Explosion((enemy.x, enemy.y - (50 if enemy.type == 'ship' else 0)), enemy.type, pygame.time.get_ticks())
                    self.explosions.append(newExplosion)
                    self.torpedoes.pop(idx1)
                    self.enemies.pop(idx2)
                    popped = True
                
                if not popped:
                    idx2 += 1
            if not popped:
                idx1 += 1


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
        
        newWord = self.glossaries[0][random.randint(0, len(self.glossaries[0]) - 1)]

        if enemyType:
            rand_y = random.randint(70, 300)
            newEnemy = Enemy("plane", 900, rand_y, newWord)
            self.enemies.append(newEnemy)
        else:
            rand_y = random.randint(420, 600)
            newEnemy = Enemy("ship", 900, rand_y, newWord)
            self.enemies.append(newEnemy)