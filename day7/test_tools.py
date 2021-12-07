from tools import *


input_text = '16,1,2,0,4,2,7,1,2,14'
days = 18

def test_part1():
    assert part1(input_text) == 37
    assert part2(input_text) == 168