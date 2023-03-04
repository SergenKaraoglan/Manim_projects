from manim import *
import random

class GameOfLife(Scene):
    def construct(self):
        # time interval between generations
        time = 0.1
        side_length = 0.5
        num_row = int(8 * (1//side_length))
        num_col = int(14 * (1//side_length))
        print(num_row, num_col)

        # initialise grid
        self.create_grid(num_row, num_col, side_length)
        self.add(self.grid)
        self.wait(time)

        # simulate game of life
        num_generations= 50
        for _ in range(num_generations):
            self.update_rules()
            self.update_grid()
            self.add(self.grid)
            self.wait(time)
            #print(self.rules)


    def create_grid(self, num_row, num_col, side_length):
        # create cells
        cells = [Square(color=BLUE_E, side_length=side_length) for _ in range(num_row*num_col)]
        # arrange cells into a grid
        self.grid = VGroup(*cells).arrange_in_grid(rows=num_row, cols=num_col, buff=0,)
        # generate rules
        self.rules = [[random.randint(0, 0) for _ in range(num_col)] for _ in range(num_row)]
        
        # create gliders that create a pattern within index range 0-15
        self.createGlider(5, 5)
        self.createGlider2(5, 10)
        self.createGlider(5, 15)
        self.createGlider2(5, 20)
        self.createGlider(5, 25)

        # set cell colours based on rules
        self.update_grid()

    def update_grid(self):
        for i in range(len(self.rules)):
            for j in range(len(self.rules[0])):
                x = i * (len(self.rules[0])) + j
                # change colour according to cell state
                if self.rules[i][j]:
                    self.grid[x].set_fill(BLUE_C, opacity = 1)
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
                            # wrap around
                            if y < 0:
                                y = len(self.rules) - 1
                            if y >= len(self.rules):
                                y = 0
                            if x < 0:
                                x = len(self.rules[0]) - 1
                            if x >= len(self.rules[0]):
                                x = 0
                            
                            live += self.rules[y][x]
                
                if self.rules[i][j] and live != 2 and live != 3:
                    new_rules[i][j] = 0
                if not self.rules[i][j] and live == 3:
                    new_rules[i][j] = 1
                #print(live)
        # update rules
        self.rules = new_rules

    def createGlider(self, x, y):
        self.rules[x][y] = 1
        self.rules[x+1][y+1] = 1
        self.rules[x+2][y+1] = 1
        self.rules[x+2][y] = 1
        self.rules[x+2][y-1] = 1
    
    # reverse glider
    def createGlider2(self, x, y):
        self.rules[x][y] = 1
        self.rules[x-1][y-1] = 1
        self.rules[x-2][y-1] = 1
        self.rules[x-2][y] = 1
        self.rules[x-2][y+1] = 1
