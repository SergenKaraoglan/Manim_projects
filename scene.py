from manim import *
import numpy as np
import random

class GameOfLife(Scene):
    def construct(self):
        # rectangle grid
        #grid = Rectangle(width=14, height=8, grid_xstep=0.5, grid_ystep=0.5)
        #self.add(grid)

        # table
        #square = Square(side_length=1, color=WHITE)
        #t0 = MobjectTable(
        #    [[square.copy() for _ in range(3)] for _ in range(3)], h_buff=0.1, v_buff=0.1
        #)
        #self.add(t0)

        #square_grid[0].set_fill(WHITE, opacity=1)

        # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        self.create_grid(16, 28)
        self.add(self.grid)

    def create_grid(self, num_row, num_col):
        square_grid = [Square(color=WHITE, side_length=0.5) for _ in range(num_row*num_col)]
        self.grid = VGroup(*square_grid).arrange_in_grid(rows=num_row, cols=num_col, buff=0,)
        self.rules = [[random.randint(0, 1) for _ in range(num_col)] for _ in range(num_row)]


