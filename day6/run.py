'''
Solution to day 6 of Advent of Code 2021: .
https://adventofcode.com/2021/day/6
'''
from tools import part1, part2

def main():
    '''
    Main function for running the solution.
    '''
    with open('day6/input.txt', 'r') as f:
        data = f.read()
    print(f'Part 1: {part1(data,80)}')
    print(f'Part 2: {part2(data,256)}')

if __name__ == '__main__':
    main()
