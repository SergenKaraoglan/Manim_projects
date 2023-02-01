from manim import *
from math import pi, sin, cos

class FractalTree(Scene):
    def construct(self):
        angel = 2*pi / 11
        ratio = 0.75
        length = 2
        base = -3

        queue = [[Line([0,base,0], [0,base+length,0]), base+length, length*ratio]]
        for i in range(10):
            line, base, length = queue.pop(0)
            self.add(line)
            if i:
                x = y = 0
                if i % 2:
                    x, y = self.get_position(length, angel, base)
                else:
                    x, y = self.get_position(length, -angel, base)
                
                line.put_start_and_end_on([x,y,0], [x+length,y+length,0])

            for i in range(2):
                queue.append([Line([0, base, 0], [0, base + length, 0]), base+length, length*ratio])

        #self.play(root.animate.put_start_and_end_on([0,base,0], [0, base+length, 0]))

    def get_position(self, length, angel, base):
        x = base + length * sin(angel)
        y = - base -length * cos(angel)

        return x, y