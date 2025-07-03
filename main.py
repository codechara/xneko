import os, pygame, moderngl, numpy as np, build

pygame.init()

def main():
    path = os.path.split(os.path.abspath(__file__))[0]

    pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.RESIZABLE)
    pygame.display.set_caption(f"XNeko {build.VERSION}")
    pygame.display.set_icon(pygame.image.load(path+"/assets/icon.png").convert_alpha())
    ctx = moderngl.create_context()

    while True:
        ctx.clear(1.0, 0.0, 0.0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()