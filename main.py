import os, pygame, moderngl, numpy as np

pygame.init()

def main():
    path = os.path.split(os.path.abspath(__file__))[0]

    pygame.display.set_mode((640, 480), pygame.OPENGL)
    pygame.display.set_caption("test")
    pygame.display.set_icon(pygame.image.load(path+"/assets/icon.png").convert_alpha())
    ctx = moderngl.create_context()
    for i in ctx.info:
        print("%s : %s" % (i, ctx.info[i]))

    prog = ctx.program(
        vertex_shader="""
            in vec2 in_vert;
            in vec3 in_color;
            
            out vec3 v_color;
            
            void main() {
                v_color = in_color;
                gl_Position = vec4(in_vert, 0.0, 1.0);
            }
        """,
        fragment_shader="""
            in vec3 v_color;
            
            out vec3 f_color;
            
            void main() {
                f_color = v_color;
            }
        """
    )

    verticles = np.array([
        -0.5, -0.5,   1.0, 0.0, 0.0,
         0.5, -0.5,   0.0, 1.0, 0.0,
         0.0,  0.5,   0.0, 0.0, 1.0
    ], dtype="f4")

    vbo = ctx.buffer(verticles)
    vao = ctx.simple_vertex_array(prog, vbo, "in_vert", "in_color")

    while True:
        ctx.clear()
        vao.render(moderngl.TRIANGLES)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()