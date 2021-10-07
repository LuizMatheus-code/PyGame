import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
length = 480

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Very nice game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen, (100, 50, 50), (200, 300, 40, 50))
    pygame.draw.circle(screen, (0, 0, 100), (220, 250), 30)
    pygame.draw.line(screen, (0, 100, 0), (390, 200), (390, 400), 5)
    pygame.display.update()
