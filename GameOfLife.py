from manim import *
import random

class GameOfLife(Scene):
    def construct(self):
        # time interval between generations
        time = 0.1

        # initialise grid
        self.create_grid(16, 28)
        self.add(self.grid)
        self.wait(time)

        # simulate game of life
        num_generations= 10
        for _ in range(num_generations):
            self.update_rules()
            self.update_grid()
            self.add(self.grid)
            self.wait(time)
            #print(self.rules)


    def create_grid(self, num_row, num_col):
        # create cells
        cells = [Square(color=BLUE_E, side_length=0.5) for _ in range(num_row*num_col)]
        # arrange cells into a grid
        self.grid = VGroup(*cells).arrange_in_grid(rows=num_row, cols=num_col, buff=0,)
        # generate rules
        self.rules = [[random.randint(0, 0) for _ in range(num_col)] for _ in range(num_row)]
        self.rules[1][2] = 1
        self.rules[2][3] = 1
        self.rules[3][1] = 1
        self.rules[3][2] = 1
        self.rules[3][3] = 1
        # set cell colours based on rules
        self.update_grid()

    def update_grid(self):
        for i in range(len(self.rules)):
            for j in range(len(self.rules[0])):
                x = i * (len(self.rules[0])) + j
                # change colour according to cell state
                if self.rules[i][j]:
                    self.grid[x].set_fill(WHITE, opacity = 1)
                else:
                    self.grid[x].set_fill(BLACK, opacity = 1)
                
                


    def update_rules(self):
        new_rules = [[self.rules[i][j] for j in range(len(self.rules[0]))] for i in range(len(self.rules))]
        for i in range(len(self.rules)):
            for j in range(len(self.rules[0])):
                # count of live cells
                live = 0
                # check adjacent cells
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k != 0 or l != 0:
                            y = i + k
                            x = j + l
                            if y >= 0 and y < len(self.rules) and x >= 0 and x < len(self.rules[0]):
                                live += self.rules[y][x]
                
                if self.rules[i][j] and live != 2 and live != 3:
                    new_rules[i][j] = 0
                if not self.rules[i][j] and live == 3:
                    new_rules[i][j] = 1
                #print(live)
        # update rules
        self.rules = new_rules