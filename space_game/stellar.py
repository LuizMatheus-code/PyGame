import pygame
import os

width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spacial')

white_color = (255, 255, 255)

fps = 60

spaceship_width, spaceship_height = 55, 40

yellow_spaceship_image = pygame.image.load(os.path.join('space_game/Assets/spaceship_yellow.png'))

yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load('space_game/Assets/spaceship_red.png')

red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)


def draw_window():
    window.fill(white_color)
    window.blit(yellow_spaceship, (300, 100)) 
    window.blit(red_spaceship, (700, 100))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
