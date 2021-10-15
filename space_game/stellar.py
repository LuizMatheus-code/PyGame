import pygame
import os

width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spacial')

white_color = (255, 255, 255)
black_color = (0, 0, 0)

border = pygame.Rect(width/2 - 5, 0, 10, height)

fps = 60
vel = 5

spaceship_width, spaceship_height = 55, 40

yellow_spaceship_image = pygame.image.load(os.path.join('space_game/Assets/spaceship_yellow.png'))

yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load('space_game/Assets/spaceship_red.png')

red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)


def yellow_handle_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
            yellow.x -= vel
        if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x:
            yellow.x += vel
        if keys_pressed[pygame.K_w] and yellow.y - vel > 0:
            yellow.y -= vel
        if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < height - 15:
            yellow.y += vel


def red_handle_movement(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.x - vel > border.x + border.width:
            red.x -= vel
        if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < width:
            red.x += vel
        if keys_pressed[pygame.K_UP] and red.y - vel > 0:
            red.y -= vel
        if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < height - 15:
            red.y += vel


def draw_window(red, yellow):
    window.fill(white_color)
    pygame.draw.rect(window, black_color, border)
    window.blit(yellow_spaceship, (yellow.x, yellow.y)) 
    window.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
