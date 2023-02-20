from manim import *
from math import pi, sin, cos

class FractalTree(Scene):
    def construct(self):
        # fractal tree variables
        angle = (pi/4)
        ratio = 0.8
        length = 1.5
        y = -3
        x = 0
        strokeWidth = 5

        # current and max depth of tree
        depth = 0
        maxDepth = 5
        # queue to contain lines (branches)
        queue = [[Line([x,y,0], [x,y+length,0], stroke_width=strokeWidth), x, y+length, length*ratio, 0, depth, strokeWidth*ratio]]
        branches = [[] for _ in range(maxDepth)]
        while True:
            # get branch
            line, x, y, length, angle2, depth, strokeWidth = queue.pop(0)
            # break condition
            if depth == maxDepth:
                break
            
            # add branch
            branches[depth].append(line)
                    
            for i in range(2):
                # get inverse x coordinate for second branch
                if i % 2:
                    x2, y2 = self.get_position(length, angle2 - angle)
                    queue.append([Line([x, y, 0], [x + x2, y + y2, 0], stroke_width=strokeWidth), 
                                  x + x2, y + y2, length * ratio, angle2 - angle, depth+1, strokeWidth*ratio])
                else:
                    x2, y2 = self.get_position(length, angle2 + angle)
                    queue.append([Line([x, y, 0], [x + x2, y + y2, 0], stroke_width=strokeWidth), 
                                  x + x2, y + y2, length * ratio, angle2 + angle, depth+1, strokeWidth*ratio])

        # animate branches per depth
        self.play(Succession(*[AnimationGroup(*[Create(branch) for branch in branches[i]], run_time=1, rate_func = rate_functions.linear) for i in range(maxDepth)], 
                              lag_ratio = 0.9, rate_func = rate_functions.linear))


    # get x, y coordinate using angle and length
    def get_position(self, length, angle):
        x = length * sin(angle)
        y = length * cos(angle)

        return x, y