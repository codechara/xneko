import pygame

pygame.init()

import buildConfig
from Window import Window

def main():
    print(f"XNeko {buildConfig.VERSION} ({buildConfig.NEKO_ONLINE_VERSION})")

    window = Window()
    screen = window.screen
    clock = pygame.time.Clock()
    window.set_mode(Window.Modes.MINIMIZED)

    delta = 0
    while True:
        screen.fill((255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                window.set_mode(Window.Modes.HIDDEN)

        pygame.display.flip()
        delta = clock.tick(buildConfig.FPS)

if __name__ == "__main__":
    main()