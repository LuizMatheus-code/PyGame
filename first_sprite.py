import pygame
from pygame.locals import *
from sys import exit


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frog_sprite = []
        for count in range(1, 11):
            self.frog_sprite.append(pygame.image.load(f'sprites/attack_{count}.png'))
        self.current = 0
        self.image = self.frog_sprite[self.current]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 200, 210

        self.animation = False


    def attack_now(self):
        self.animation = True


    def update(self):
        if self.animation:
            if self.current == 0:
                pygame.mixer.Sound('sound_effect.wav').play()
            self.current += 0.5
            if self.current >= len(self.frog_sprite):
                self.current = 0
                self.animation = False
            self.image = self.frog_sprite[int(self.current)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))

all_sprites = pygame.sprite.Group()
animated_frog = Frog()
all_sprites.add(animated_frog)

pygame.init()

width = 640
length = 480

black_color = (0, 0, 0)

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Frog sprite')

clock = pygame.time.Clock()

background_image = pygame.image.load('pixel_city_background.png').convert()
background_image = pygame.transform.scale(background_image, (width, length))

while True:
    clock.tick(30)
    screen.fill(black_color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            animated_frog.attack_now()
    
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
