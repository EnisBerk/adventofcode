from tools import *


initial_state= '3,4,3,1,2'
days = 18

def test_part1():
    assert part1(initial_state, days) == 26
    assert part1(initial_state, 80) == 5934
    assert part1(initial_state, 256) == 26984457539