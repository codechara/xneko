import os, pygame

pygame.init()

def main():
    path = os.path.split(os.path.abspath(__file__))[0]

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("test")
    pygame.display.set_icon(pygame.image.load(path+"/assets/icon.png").convert_alpha())

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()