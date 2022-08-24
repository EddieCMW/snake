from turtle import back
import random
from xml.etree.ElementTree import TreeBuilder
import pygame

pygame.init()
clock = pygame.time.Clock()

score = 0

def gamewindowupdate():
    screen.fill(color)
    pygame.draw.rect(screen, (128,128,128), (0,0,600,20))
    pygame.draw.rect(screen, (128,128,128), (0,580,600,20))
    pygame.draw.rect(screen, (128,128,128), (0,0,20,600))
    pygame.draw.rect(screen, (128,128,128), (580,0,20,600))
    snakeobj.draw(screen)
    apple.draw(screen)
    
    pygame.display.update()
    


width = 600
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake!")
color = (0,0,0)



class Snake(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.velocity = 4
        self.pressed = True
        self.hitbox = (self.x - 2, self.y + 2, 27, 27)
    def draw(self, screen):
        self.hitbox = (self.x - 2, self.y -2, 27, 27)
        pygame.draw.rect(screen, (0,255,0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

snakeobj = Snake(100,100,25,25)




class Food(object):
    def __init__(self):

        self.randomfood()
    
    def randomfood(self):
        self.x = random.randrange(20,580,1)
        self.y = random.randrange(20,580,1)

    def draw(self, screen):
        self.hitbox = (self.x + 5, self.y + 5, 10)
        pygame.draw.circle(screen, "RED", (self.x, self.y), 10)
        pygame.draw.circle(screen, "YELLOW", (self.x, self.y), 8)



apple = Food()
    

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and snakeobj.x > 20:
        snakeobj.x -= snakeobj.velocity
    if keys[pygame.K_RIGHT] and snakeobj.x < (width-20) - snakeobj.width:
        snakeobj.x += snakeobj.velocity
    if keys[pygame.K_UP] and snakeobj.y > 20:
        snakeobj.y -= snakeobj.velocity
    if keys[pygame.K_DOWN] and snakeobj.y < (height-20) - snakeobj.height:
        snakeobj.y += snakeobj.velocity
    screen.fill((0,0,0))       
    clock.tick(60)

    
    gamewindowupdate()