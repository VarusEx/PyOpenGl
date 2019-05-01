import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices=(
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (0,0,1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (1,4),
    (1,2),
    (2,4),
    (2,3), # (2,3)
    (3,4)
)


class Render3DObejct(object):
    linewidth = 10
    lines = GL_LINES
    vertices = None
    color = (0, 0, 1)
    edges = None

    def __init__(self, listvertex, listedges):
        self.vertices, self.edges = listvertex, listedges
        self.draw()

    def draw(self):
        glLineWidth(self.linewidth)
        glBegin(self.lines)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(self.color[0], self.color[1], self.color[2])
        glEnd()

    def set_linewidth(self, width):
        self.linewidth = width

    def set_linestyle(self, style=GL_LINES):
        self.lines = style

    def set_color(self, rgb=(0, 0, 1)):
        self.color = rgb

    def set_newobject(self, listvert, listedge):
        if listvert and listedge is (list or []):
            self.vertices = listvert
            self.edges = listedge

    def get_linewidth(self):
        return self.linewidth

    def get_linestyle(self):
        return self.lines

    def get_color(self):
        return self.color

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges


def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)
    obj = Render3DObejct(vertices, edges)
    speed = 0.2
    glTranslatef(0, 0, -5)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            glTranslatef(0, speed, 0)
        elif keys[pygame.K_DOWN]:
            glTranslatef(0, -speed, 0)
        elif keys[pygame.K_RIGHT]:
            glTranslatef(speed, 0, 0)
        elif keys[pygame.K_LEFT]:
            glTranslatef(-speed, 0, 0)
        if keys[pygame.K_t]:
            glTranslatef(0, 0, -speed)
        if keys[pygame.K_g]:
            glTranslatef(0, 0, speed)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        obj.draw()
        pygame.display.flip()


main()
