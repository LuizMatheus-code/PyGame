import pygame
from pygame.locals import *
from sys import exit
import os


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


main_directory = os.path.dirname(__file__)
image_directory = os.path.join(main_directory, 'images')
sound_directory = os.path.join(main_directory, 'sounds')
width = 640
length = 480

white_color = (255, 255, 255)

screen = pygame.display.set_mode((width, length))

pygame.display.set_caption('Dino game')

all_sprites = pygame.sprite.Group()
dino = Dinosaur()
all_sprites.add(dino)

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    screen.fill(white_color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
