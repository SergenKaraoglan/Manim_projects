from manim import *
from math import floor
import random

class PerlinNoise(Scene):
    def construct(self):
         gradients = [random.uniform(-1, 1) for _ in range(10)]
         
         for i in range((len(gradients)-1)*10):
            print('a')
            x = i /10
            y = self.sample(x, gradients)
            print(y, x)
            self.add(Dot([x - 5, (y+1)**2, 0]))
         
       

    
    def sample(self, x, gradients):
        low = floor(x)
        hi = low + 1
        dist = x - low
        lowSlope = gradients[low]
        hiSlope = gradients[hi]
        lowPos = lowSlope * dist
        hiPos = -hiSlope * (1-dist)
        u = dist * dist * (3.0 - 2.0 * dist)
        return (lowPos*(1-u)) + (hiPos*u)