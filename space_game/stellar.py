import pygame

width, height = 900, 500
window = pygame.display.set_mode((width, height))

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
