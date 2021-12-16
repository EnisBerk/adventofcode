'''
tools for advent code day 12
'''
from collections import defaultdict

from functools import total_ordering
from queue import PriorityQueue
import math


def load_data(text):
    '''
    load data from file
    '''
    data = text.strip().split('\n')
    data = [[int(x) for x in line] for line in data]
    return data

@total_ordering
class Point():
    '''
        single point in the grid
    '''
    def __init__(self, x, y, value,grid=None,):
        self.x = x
        self.y = y
        self.value = value
        self.path_weight = math.inf
        self.previous = None
        if grid:
            self.grid = grid
        else:
            self.grid = None
    def __lt__(self, other):
        return self.path_weight<other.path_weight

    def __eq__(self, other):
        return self.path_weight == other.path_weight

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def neighbors(self,grid=None):
        if self.grid==None:
            self.grid = grid
        for x, y in [[self.x - 1, self.y], [self.x + 1, self.y],
                     [self.x, self.y - 1], [self.x, self.y + 1]]:
            if x > -1 and y > -1 and x < self.grid.x_dim and y < self.grid.y_dim:
                yield self.grid.points[x][y]

class Grid():
    '''
     class for the grid, with methods to find the basins and the lowest points
    '''
    def __init__(self, data):
        self.data = data
        self.points = data
        for x,line in enumerate(data):
            for y,value in enumerate(line):
                self.points[x][y] = Point(x, y, value,grid=self)
                
        self.points[0][0].path_weight = 0
        self.points[0][0].previous = 'start'
        self.x_dim = len(self.points)
        self.y_dim = len(self.points[0])


    def yield_points(self):
        for x, line in enumerate(self.points):
            for y, point in enumerate(line):
                yield x,y,point
    
def dijkstra(graph):

    remaining = PriorityQueue()
    remaining.put(graph.points[0][0])
    visited = set([graph.points[0][0]])
    while not remaining.empty():
        current = remaining.get()
        
        visited.add(current)
        for neighbor in current.neighbors():
            if neighbor not in visited:
                if neighbor.path_weight > (current.path_weight + neighbor.value):
                    neighbor.path_weight = current.path_weight + neighbor.value
                    neighbor.previous = current
                    remaining.put(neighbor)
    return graph
            

def part1(text):

    grid = Grid(load_data(text))
    graph = dijkstra(grid)
    return graph.points[-1][-1].path_weight


def inc(x,count):
    for i in range(0,count):
        if x==9:
            x= 1
        else:
            x= x+1
    return x

def expand_matrix(matrix,x_dim,y_dim):
    matrix_x= []
    print(len(matrix),len(matrix[0]))
    for row in matrix:
        matrix_x_row = []
        for c_x in range(0,x_dim):
            matrix_x_row.extend([inc(value,c_x) for value in row])
        matrix_x.append(matrix_x_row)

    matrix_y = []
    for c_y in range(0,y_dim):
        for row in matrix_x:
            matrix_y.append([inc(value,c_y) for value in row])

    return matrix_y


def part2(text):
    matrix = load_data(text)
    matrix = expand_matrix(matrix,5,5)
    grid = Grid(matrix)
    graph = dijkstra(grid)
    return graph.points[-1][-1].path_weight

