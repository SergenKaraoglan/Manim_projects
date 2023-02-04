from manim import *
from math import sin, cos, pi
import random

class PerlinNoise(Scene):
    def construct(self):
         grid = [random.uniform(-2, 2) for _ in range(10)]
         for i in range(len(grid)):
            self.add(Dot([i-5, grid[i], 0]))
    
    def lerp(alpha, y, y2):
        return (1-alpha) * y + alpha * y2
    def perlinNoise():
        pass