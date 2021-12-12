from tools import *


input_text = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

def test_part1():
    assert part1(input_text,steps=10) == 204
    assert part1(input_text,steps=100) == 1656
    assert part2(input_text) == 195

