import pygame
from pygame.locals import *
from sys import exit
from random import randint


def bigger_snake(snake_body_growth):
    for position in snake_body_growth:
        pygame.draw.rect(screen, (0, 255, 0), (position[0], position[1], 20, 20))


def restart_game():
    global points, initial_compriment, snake_x, snake_y, snake_body_growth, snake_head_growth, red_apple_x, red_apple_y, game_over
    points = 0
    initial_compriment = 5
    snake_x = int(width/2 - 20)
    snake_y = int(length/2 - 25)
    snake_body_growth = []
    snake_head_growth = []
    red_apple_x = randint(40, 600)
    red_apple_y = randint(50, 430)
    game_over = False


pygame.init()

pygame.mixer.music.set_volume(0.4)
background_music = pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound('sound_effect.wav')

width = 640
length = 480

snake_x = int(width/2 - 20)
snake_y = int(length/2 - 25)

velocity = 10
x_control = velocity
y_control = 0

red_apple_x = randint(40, 600)
red_apple_y = randint(50, 430)

points = 0
font = pygame.font.SysFont('arial', 40, True, True)

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Very nice game')
game_clock = pygame.time.Clock()
snake_body_growth = []
initial_compriment = 5
game_over = False

while True:
    game_clock.tick(30)
    screen.fill((255, 255, 255))

    message = f'Points: {points}'
    text_format = font.render(message, True, (0, 0, 0))

    if snake_y > length:
        snake_y = 0
    if snake_y < 0:
        snake_y = length
    if snake_x >= width:
        snake_x = 0
    if snake_x < 0:
        snake_x = width
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == velocity:
                    pass
                else:
                    x_control = -velocity
                    y_control = 0
            if event.key == K_d:
                if x_control == -velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0
            if event.key == K_w:
                if y_control == velocity:
                    pass
                else:
                    y_control = -velocity
                    x_control = 0
            if event.key == K_s:
                if y_control == -velocity:
                    pass
                else:
                    y_control = velocity
                    x_control = 0
    
    snake_x += x_control
    snake_y += y_control

    snake = pygame.draw.rect(screen, (0, 255, 0), (snake_x, snake_y, 20, 20))
    apple = pygame.draw.circle(screen, (255, 0, 0), (red_apple_x, red_apple_y), 20)

    if snake.colliderect(apple):
        collision_sound.play()
        red_apple_x = randint(40, 600)
        red_apple_y = randint(50, 430)
        points += 1
        initial_compriment += 1

    snake_head_growth = []
    snake_head_growth.append(snake_x)
    snake_head_growth.append(snake_y)

    snake_body_growth.append(snake_head_growth)

    if snake_body_growth.count(snake_head_growth) > 1:
        font2 = pygame.font.SysFont("arial", 20, True)
        message = "Game over! Press 'r' to restart"
        text_format = font2.render(message, True, (0, 0, 0))
        ret_text = text_format.get_rect()

        game_over = True
        while game_over:
            screen.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()

            ret_text.center = (width//2, length//2)
            screen.blit(text_format, ret_text)
            pygame.display.update()

    if len(snake_body_growth) > initial_compriment:
        del snake_body_growth[0]

    bigger_snake(snake_body_growth)

    screen.blit(text_format, (420, 10))
    pygame.display.update()
