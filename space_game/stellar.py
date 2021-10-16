import pygame
import os
pygame.font.init()
pygame.mixer.init()

width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spacial')

white_color = (255, 255, 255)
black_color = (0, 0, 0)
red_color = (255, 0, 0)
yellow_color = (255, 255, 0)

border = pygame.Rect(width//2 - 5, 0, 10, height)

bullet_hit_sound = pygame.mixer.Sound('space_game/Assets/Grenade+1.mp3')
bullet_fire_sound = pygame.mixer.Sound('space_game/Assets/Gun+Silencer.mp3')

health_font = pygame.font.SysFont('arial', 40)
winner_font = pygame.font.SysFont('arial', 100)

fps = 60
vel = 5
bullet_velocity = 7
max_bullets = 3
spaceship_width, spaceship_height = 55, 40

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

yellow_spaceship_image = pygame.image.load(os.path.join('space_game/Assets/spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load('space_game/Assets/spaceship_red.png')
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)

space = pygame.image.load('space_game/Assets/space.png')
pygame.transform.scale(space, (width, height))

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


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_velocity
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_velocity
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health,yellow_health):
    window.blit(space, (0, 0))
    pygame.draw.rect(window, black_color, border)

    red_health_text = health_font.render('Health: ' + str(red_health), 1, white_color)
    yellow_health_text = health_font.render('Health: ' + str(yellow_health), 1, white_color)
    window.blit(red_health_text, (width - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))

    window.blit(yellow_spaceship, (yellow.x, yellow.y)) 
    window.blit(red_spaceship, (red.x, red.y))


    for bullet in red_bullets:
        pygame.draw.rect(window, red_color, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(window, yellow_color, bullet)

    pygame.display.update()


def draw_winner(text):
    draw_text = winner_font.render(text, 1, white_color)
    window.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    yellow_bullets = []
    red_bullets = []

    red_health = 4
    yellow_health = 4

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    bullet_fire_sound.play().set_volume(0.08)

                if event.key == pygame.K_l and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    bullet_fire_sound.play().set_volume(0.08)

            if event.type == red_hit:
                red_health -= 1
                bullet_hit_sound.play().set_volume(0.08)

            if event.type == yellow_hit:
                yellow_health -= 1
                bullet_hit_sound.play().set_volume(0.08)
        
        winner_text = ''
        if red_health <= 0:
            winner_text = 'Yellow wins'
        
        if yellow_health <= 0:
            winner_text = 'Red wins'

        if winner_text != '':
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()

if __name__ == "__main__":
    main()
