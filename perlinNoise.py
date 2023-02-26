from manim import *
from math import floor
import random

class PerlinNoise(Scene):
    def construct(self):
         gradients = [random.uniform(-1, 1) for _ in range(10)]
         
         for i in range((len(gradients)-1)*10):
            x = i /10
            y = self.sample(x, gradients)
            print(y, x)
            self.add(Dot([x - 5, (y+1)**2, 0]))

    
    def sample(self, x, gradients):
        # find the unit interval
        interval = floor(x)
        # find the distance between the unit interval and the sample
        distance = x - interval
        # find the unit interval gradients
        g1 = gradients[interval % len(gradients)]
        g2 = gradients[(interval + 1) % len(gradients)]
        # interpolate between the gradients
        return self.interpolate(g1, g2, distance)
    
    # octave noise
    def octave(self, x, gradients, octaves):
        sum = 0
        for i in range(octaves):
            sum += self.sample(x, gradients) / (2**i)
        return sum