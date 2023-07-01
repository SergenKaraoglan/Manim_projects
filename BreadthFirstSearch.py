from manim import *
import random

class breadthSearch(Scene):
    def construct(self):
        self.finished = False
        self.seen = set((0,0))
        self.queue = [(0,0,0)]
        self.dirs = [(0,1), (-1,0), (0,-1), (1,0)]
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

        self.cells = []
        self.breadthSearch()
        
        self.cells.sort()
        cur = 0
        for i in range(len(self.cells)):
            depth = self.cells[i][0]
            i = self.cells[i][1]
            if depth != cur:
                cur += 1
                self.add(self.grid)
                self.wait(self.time)
            self.grid[i].set_fill(BLUE_C, opacity = 1)
        
        self.add(self.grid)

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
    
    def breadthSearch(self):
        #print(self.seen)
        if self.queue and not self.finished:
            curCell = self.queue.pop(0)
            x = curCell[0]
            y = curCell[1]
            depth = curCell[2]
            i = y*self.num_col + x
            if self.rules[i] == 2:
                self.finished = True
                return
            self.cells.append((depth, i))

            for dir in self.dirs:
                x2 = x+dir[0]
                y2 = y+dir[1]
                i = y2*self.num_col + x2
                if -1 < x2 < self.num_col and -1 < y2 < self.num_row and not ((x2,y2) in self.seen) and self.rules[i] != 1:
                    self.queue.append((x2, y2, depth+1))
                    self.seen.add((x2, y2))
            self.breadthSearch()