import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.4)
background_music = pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound('sound_effect.wav')

width = 640
length = 480

x_blue = randint(40, 600)
y_blue = randint(50, 430)

points = 0
font = pygame.font.SysFont('arial', 40, True, True)

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Very nice game')
game_clock = pygame.time.Clock()
x = int(width/2 - 20)
y = int(length/2 - 25)

while True:
    game_clock.tick(30)
    screen.fill((0, 0, 0))
    if y > length:
        y = 0
    if y < 0:
        y = length
    if x >= width:
        x = 0
    if x < 0:
        x = width
    message = f'Points: {points}'
    text_format = font.render(message, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    red_rectangle = pygame.draw.rect(screen, (200, 50, 50), (x, y, 40, 50))
    blue_circle = pygame.draw.circle(screen, (0, 0, 200), (x_blue, y_blue), 30)

    if red_rectangle.colliderect(blue_circle):
        collision_sound.play()
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)
        points += 1
    
    screen.blit(text_format, (420, 10))
    pygame.display.update()
