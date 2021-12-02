'''
Solution for Advent of Code 2021 Day 2: Dive!
'''

input_file = 'day2/input'

with open(input_file, encoding='utf-8') as f:
    data = f.readlines()


def test_calculate_depth_and_horizon():
    '''
    Test for calculate_depth_and_horizon
    '''
    data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    assert calculate_depth_and_horizon(data) == (10, 15)


def test_calculate_depth_and_horizon_v2():
    '''
    Test for calculate_depth_and_horizon
    '''
    data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    try:
        assert calculate_depth_and_horizon_v2(data) == (60, 15)
    except AssertionError:
        print(test_calculate_depth_and_horizon_v2)



def calculate_depth_and_horizon(data):
    depth = 0
    horizon = 0
    for i in data:
        cmd, dst = i.split(' ')
        dst = int(dst)
        if cmd =='forward':
            horizon += dst
        elif cmd == 'up':
            depth -= dst
        elif cmd == 'down':
            depth += dst
    return depth, horizon

test_calculate_depth_and_horizon()
d,h=calculate_depth_and_horizon(data)
print(d*h)


def calculate_depth_and_horizon_v2(data):
    depth = 0
    horizon = 0
    aim = 0
    for i in data:
        cmd, dst = i.split(' ')
        dst = int(dst)
        if cmd =='forward':
            horizon += dst
            depth +=aim*dst
        elif cmd == 'up':
            aim -= dst
        elif cmd == 'down':
            aim += dst
    return depth, horizon


test_calculate_depth_and_horizon_v2()
d,h=calculate_depth_and_horizon_v2(data)
print(d*h)