'''
test tools
'''
from tools import *

example_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


def test_load_data():
    '''
    test load data
    '''
    short_input = [[(0,9), (5,9)]]
    for data  in load_data(short_input):
        assert (data.Start.x,data.Start.y) == (0, 9)
        assert (data.End.x,data.End.y) == (5, 9)

def test_generate_points():
    '''
    test generate points
    '''
    short_input = [[(0,9), (5,9)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line))
    assert line ==[(0,9), (1,9), (2,9), (3,9), (4,9), (5,9)]
    
    short_input = [[(0,3), (5,9)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line))
    assert line == []

    short_input = [[(1,1), (3,3)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    print('line')
    print(line)
    assert line == [(1,1),(2,2),(3,3)]

    short_input = [[(9,7), (7,9)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    assert line == [(9,7),(8,8),(7,9)]

    short_input = [[(9,7), (9,7)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    assert line == [(9,7)]

    short_input = [[(0,0), (8,8)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    assert line == [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]

    short_input = [[(2,5), (4,6)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    assert line == []


    short_input = [[(6,4), (2,0)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    print('line',line)
    assert line == [(6,4),(5,3),(4,2),(3,1),(2,0)]

    short_input = [[(2,2), (2,1)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    assert line == [(2,1),(2,2)]


    short_input = [[(3,0), (0,3)]]
    a_line = next(load_data(short_input))
    line = list(generate_points(a_line,True))
    assert line == [(3,0),(2,1),(1,2),(0,3)]



def test_part1():
    '''
    '''
    assert 5==part1(example_input)

def test_part2():
    '''
    '''
    assert 12==part2(example_input)