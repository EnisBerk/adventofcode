'''
Solution to day 11 of Advent of Code 2021:Dumbo Octopus .
https://adventofcode.com/2021/day/11
'''
from tools import part1, part2

def main():
    '''
    Main function for running the solution.
    '''
    with open('day11/input.txt', 'r',encoding='utf-8') as f:
        data = f.read()
    print(f'Part 1: {part1(data,100)}')
    print(f'Part 2: {part2(data)}')

if __name__ == '__main__':
    main()
