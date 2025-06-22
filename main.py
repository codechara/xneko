import pygame, buildConfig

pygame.init()

def main():
    print(f"XNeko {buildConfig.VERSION} ({buildConfig.NEKO_ONLINE_VERSION})")

if __name__ == "__main__":
    main()