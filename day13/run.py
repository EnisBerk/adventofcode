'''
Solution to day 13 of Advent of Code 2021: Transparent Origami.
https://adventofcode.com/2021/day/13
'''
from tools import part1, part2

def main():
    '''
    Main function for running the solution.
    '''
    with open('day13/input.txt', 'r',encoding='utf-8') as f:
        data = f.read()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == '__main__':
    main()
