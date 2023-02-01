from manim import *
from math import pi, sin, cos

class FractalTree(Scene):
    def construct(self):
        angle = 2*pi / 11
        ratio = 0.75
        length = 1.5
        y = -4
        x = 0

        queue = [[Line([x,y,0], [x,y+length,0]), x, y+length, length*ratio, angle]]
        for i in range(200):
            line, x, y, length, angle2 = queue.pop(0)
            self.add(line)
            x2, y2 = self.get_position(length, angle2)
                    

            for i in range(2):
                if i % 2:
                    x2 = -x2
                queue.append([Line([x, y, 0], [x + x2, y + y2, 0]), x + x2, y + y2, length*ratio, angle2])


    def get_position(self, length, angle):
        x = length * sin(angle)
        y = length * cos(angle)

        return x, y 