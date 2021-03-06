'''
Tools for day 5 of advent of code 2021
'''

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['Start', 'End'])


def read_text(text):
    '''
    Reads the text file
    '''
    data = text.strip().split('\n')
    # print(data[0].split('->'))
    data = [[map(int,
                 i.strip().split(','))
             for i in x.split('->')]
            for x in data
            if x]
    return data


def load_data(data):
    '''
    Loads the data from the input file
    '''
    for line in data:
        start = Point(*line[0])
        end = Point(*line[1])
        yield Line(start, end)



def generate_points(line,horizantal=False):
    '''
    Generates all points on the line
    '''
    if line.Start == line.End:
        yield line.Start
        return

    dx = abs(line.End.x - line.Start.x)
    dy = abs(line.End.y - line.Start.y)
    minx = min(line.Start.x, line.End.x)
    miny = min(line.Start.y, line.End.y)

    if not (dx != 0 and dy != 0):
        for i in range(minx, minx + dx + 1):
            for j in range(miny, miny + dy + 1):
                yield Point(i, j)
    if horizantal and dx==dy:
        yield line.Start
        x=line.Start.x
        y=line.Start.y
        while x!=line.End.x:
            if line.End.x>line.Start.x:
                x+=1
            else:
                x-=1
            if line.End.y>line.Start.y:
                y+=1
            else:
                y-=1
            yield Point(x,y)




def part1(text,horizantal=False):
    '''
    Part 1 of day 5
    '''
    diagram = {}
    danger_count = 0
    data = read_text(text)
    for line in load_data(data):
        for point in generate_points(line,horizantal):
            if (point.x,point.y) == (2,2):
                print(line)
            diagram.setdefault(point, 0)
            diagram[point] += 1
            if diagram[point] == 2:
                danger_count += 1
    return danger_count

def part2(text):
    return part1(text,horizantal=True)