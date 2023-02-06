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

        # current and max depth of tree
        depth = 0
        maxDepth = 10
        # queue to contain lines (branches)
        queue = [[Line([x,y,0], [x,y+length,0]), x, y+length, length*ratio, 0, depth]]
        branches = [[] for _ in range(maxDepth)]
        while True:
            # get branch
            line, x, y, length, angle2, depth = queue.pop(0)
            # break condition
            if depth == maxDepth:
                break
            
            # add branch
            branches[depth].append(line)
                    
            for i in range(2):
                # get branch position
                
                # get inverse x coordinate for second branch
                if i % 2:
                    x2, y2 = self.get_position(length, angle2 - angle)
                    queue.append([Line([x, y, 0], [x + x2, y + y2, 0]), x + x2, y + y2, length * ratio, angle2 - angle, depth+1])
                else:
                    x2, y2 = self.get_position(length, angle2 + angle)
                    queue.append([Line([x, y, 0], [x + x2, y + y2, 0]), x + x2, y + y2, length * ratio, angle2 + angle, depth+1])

        # animate branches per depth
        """ for i in range(len(branches)):
            branchGroup = VGroup(*branches[i])
            self.play(*[Create(branch) for branch in branchGroup], run_time = 1.5) """
        # animate all branches at the same time
        self.play(*[Create(branch) for i in range(maxDepth) for branch in branches[i]], run_time = 3)


    # get x, y coordinate using angle and length
    def get_position(self, length, angle):
        x = length * sin(angle)
        y = length * cos(angle)

        return x, y