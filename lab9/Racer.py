#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("materials/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("RacerGame")

#Create Class of Enemies:
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materials/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
#Create Class of Coins:
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materials/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
#Create Class of another Coins with conditions:
class Coin1(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materials/Coin1.jpeg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Coin2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materials/Coin2.jpeg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
#Create Class of Player:
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materials/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin1()
C3 = Coin2()
#Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C1)
coins1 = pygame.sprite.Group()
coins1.add(C2)
coins2 = pygame.sprite.Group()
coins2.add(C3)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coiner = font_small.render(str(COIN), True, 'Green')
    DISPLAYSURF.blit(coiner, (50, 10))
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    #Speed condition:
    COINCH = 0
    if COIN - COINCH >= 30 and (pygame.sprite.spritecollideany(P1, coins) or pygame.sprite.spritecollideany(P1, coins1)):
        SPEED = SPEED + 0.5
        COINCH = COIN
    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COIN += 1
        pygame.mixer.Sound('materials/coin.mp3').play()
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(E1, coins):
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(P1, coins1):
        COIN += 3
        pygame.mixer.Sound('materials/coin.mp3').play()
        C2.rect.top = 0
        C2.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(E1, coins1):
        C2.rect.top = 0
        C2.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(C1, coins1):
        C2.rect.top = 0
        C2.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(P1, coins2):
        COIN += 5
        pygame.mixer.Sound('materials/coin.mp3').play()
        C3.rect.top = 0
        C3.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(E1, coins2):
        C3.rect.top = 0
        C3.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(C1, coins2):
        C3.rect.top = 0
        C3.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    if pygame.sprite.spritecollideany(C2, coins2):
        C3.rect.top = 0
        C3.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('materials/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)