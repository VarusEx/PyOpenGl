import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy

vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [0, 0, 1]
    ]

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 4),
    (1, 2),
    (2, 4),
    (2, 3),
    (3, 4)
)


class Render3DObejct(object):
    linewidth = 10
    lines = GL_QUADS
    vertices = None
    color = (0, 0, 1)
    edges = None

    def __init__(self, listvertex, listedges, mul=1):
        self.edges = listedges
        self.vertices = list(numpy.multiply(numpy.array(listvertex), mul))
        self.draw()

    def draw(self):
        glLineWidth(self.linewidth)
        glBegin(self.lines)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(self.color[0], self.color[1], self.color[2])
        glEnd()

    def move(self, x, y, z):
        self.vertices = list(map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.vertices))

    def set_linewidth(self, width):
        self.linewidth = width

    def set_linestyle(self, style=GL_LINES):
        self.lines = style

    def set_color(self, rgb=(0, 0, 1)):
        self.color = rgb

    def set_newobject(self, listvert, listedge):
        if listvert and listedge:
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
            obj.move(0, speed, 0)
        elif keys[pygame.K_DOWN]:
            obj.move(0, -speed, 0)
        elif keys[pygame.K_RIGHT]:
            obj.move(speed, 0, 0)
        elif keys[pygame.K_LEFT]:
            obj.move(-speed, 0, 0)
        if keys[pygame.K_t]:
            obj.move(0, 0, -speed)
        if keys[pygame.K_g]:
            obj.move(0, 0, speed)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        obj.draw()
        pygame.display.flip()


main()
