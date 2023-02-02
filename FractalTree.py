from manim import *
from math import pi, sin, cos

class FractalTree(Scene):
    def construct(self):
        # fractal tree variables
        angle = (2*pi / 11)/2
        ratio = 0.75
        length = 1.5
        y = -4
        x = 0

        # queue to contain lines (branches)
        queue = [[Line([x,y,0], [x,y+length,0]), x, y+length, length*ratio, angle]]
        for i in range(1000):
            # get branch
            line, x, y, length, angle2 = queue.pop(0)
            # draw branch
            self.add(line)
            #self.wait(1)
                    
            for i in range(2):
                # get branch position
                
                # get inverse x coordinate for second branch
                if i % 2:
                    x2, y2 = self.get_position(length, angle2 - angle*3)
                    queue.append([Line([x, y, 0], [x + x2, y + y2, 0]), x + x2, y + y2, length * ratio, angle2 - angle])
                else:
                    x2, y2 = self.get_position(length, angle2 + angle)
                    queue.append([Line([x, y, 0], [x + x2, y + y2, 0]), x + x2, y + y2, length * ratio, angle2 + angle])

    # get x, y coordinate using angle and length
    def get_position(self, length, angle):
        
        x = length * sin(angle)
        y = length * cos(angle)

        return x, y