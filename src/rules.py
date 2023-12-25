import random
from turtle import update 
import pygame 
import os
import sys

pygame.init()

rules = pygame.display.set_mode((800,600))
icon = pygame.image.load('assets/Rules.png')
icon = pygame.transform.scale(icon, (800, 600))

pygame.display.set_icon(icon)

while True:
    #pygame.display.update()
    window = 1
    rules.fill((0,0,0))
    rules.blit(icon, (0,0))
    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == QUIT:
            exec(open('game_screen.py').read())
    


