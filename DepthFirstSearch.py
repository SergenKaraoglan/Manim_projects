from manim import *
import random

class DepthSearch(Scene):
    def construct(self):
        self.finished = False
        self.seen = set()
        # time interval between generations
        self.time = 0.1
        # grid size
        side_length = 0.5
        self.num_row = int(8 * (1//side_length))
        self.num_col = int(14 * (1//side_length))

        # initialise grid
        self.create_grid(self.num_row, self.num_col, side_length)
        self.add(self.grid)
        self.wait(self.time)

        self.depthSearch(0,0)


    def create_grid(self, num_row, num_col, side_length):
        # create cells
        cells = [Square(color=BLUE_E, side_length=side_length) for _ in range(num_row*num_col)]
        # arrange cells into a grid
        self.grid = VGroup(*cells).arrange_in_grid(rows=num_row, cols=num_col, buff=0,)
        # generate rules
        self.rules = [round(random.random()-0.3) for _ in range(num_col) for _ in range(num_row)]
        # print(self.rules)

        self.goal = random.randint(10, len(self.rules)-1)
        # set cell colours based on rules
        for i in range(len(self.rules)):
            if self.rules[i] == 1:
                self.grid[i].set_fill(WHITE, opacity=1)
        
        self.grid[self.goal].set_fill(RED, opacity=1)
        self.rules[self.goal] = 2
    
    def update_grid(self,x, y):
        i = y*self.num_col + x
        self.grid[i].set_fill(BLUE_C, opacity = 1)
        self.add(self.grid)
        self.wait(self.time)
    
    def depthSearch(self, x, y):
        #print(self.seen)
        i = y*self.num_col + x
        if -1 < x < self.num_col and -1 < y < self.num_row and not ((x,y) in self.seen) and self.rules[i] != 1 and not self.finished:
            if self.rules[i] == 2:
                self.finished = True
                return
            #print(x, y)
            self.seen.add((x, y))
            self.update_grid(x, y)
            self.depthSearch(x, y+1)
            self.depthSearch(x-1, y)
            self.depthSearch(x, y-1)
            self.depthSearch(x+1, y)