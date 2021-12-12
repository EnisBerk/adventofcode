'''
tools for advent code day 11
'''
from collections import deque


def load_data(text):
    '''
    load data from file
    '''
    data = text.strip().split('\n')
    data = [[x for x in line] for line in data]
    return data


class Point(object):

    def __init__(self, x, y,value,grid) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.value = value
        self.last_explode = -1
        self.grid=grid

    def neighbours(self):
        neigbours = [
            self.grid.get_point(self.x + 1, self.y),
            self.grid.get_point(self.x - 1, self.y),
            self.grid.get_point(self.x, self.y + 1),
            self.grid.get_point(self.x, self.y - 1),
            self.grid.get_point(self.x + 1, self.y + 1),
            self.grid.get_point(self.x - 1, self.y - 1),
            self.grid.get_point(self.x - 1, self.y + 1),
            self.grid.get_point(self.x + 1, self.y - 1),
        ]
        for neighbour in neigbours:
            yield neighbour
    
    def energize(self):
        if self.value == 9:
            self.explode(self.grid)
        if self.last_explode == self.grid.step:
            pass
        else:
            self.value += 1


    def explode(self, grid):
        if self.last_explode != grid.step:
            self.value = 0
            self.last_explode = grid.step
            grid.explode_points += 1
            for neighbour in self.neighbours():
                if neighbour:
                    neighbour.energize()


class Grid(object):
    def __init__(self, data):
        super().__init__()
        self.grid = {}
        self.step = 0
        self.explode_points = 0
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                point = Point(int(x), int(y),int(char), self)
                point.value = int(char)
                self.grid[(x, y)] = point
        self.size = len(self.grid)

    def get_point(self, x, y):
        return self.grid.get((x, y), None)
    
    def next_step(self):
        for point in self.grid.values():
            point.energize()
        self.step += 1



def part1(data,steps=10):
    '''
    part 1
    '''
    pass
    data = load_data(data)
    grid = Grid(data)
    for _ in range(steps):
        grid.next_step()

    return grid.explode_points
    


def part2(data):
    '''
    part 2
    '''
    data = load_data(data)
    grid = Grid(data)
    current_explodes = grid.explode_points
    while True:
        grid.next_step()
        if grid.explode_points == current_explodes + grid.size:
            return grid.step
        current_explodes = grid.explode_points
