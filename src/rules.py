import random 
import pygame 

pygame.init()
rules = pygame.display.set_mode((800,600))
icon = pygame.image.load('Rules.png')
pygame.display.set_icon(icon)

while True:
    rules.fill((0,0,0))
    rules.blit(icon, (0,0))