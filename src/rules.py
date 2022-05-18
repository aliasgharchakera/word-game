import random
from turtle import update 
import pygame 

pygame.init()

rules = pygame.display.set_mode((800,600))
icon = pygame.image.load('Rules.png')
icon = pygame.transform.scale(icon, (800, 600))

pygame.display.set_icon(icon)

while True:
    pygame.display.update()
    rules.fill((0,0,0))
    rules.blit(icon, (0,0))
    pygame.display.update()

    
