'''
Solution for Advent of Code 2021
'''

input_file='day1/input'

with open(input_file,encoding='utf-8') as f:
    data = f.readlines()
    data = [int(x.strip()) for x in data]

def part1(data):
    previous=data[0]
    total=0
    for i in data[1:]:
        if previous<i:
            total+=1
        previous=i
    print('part 1',total)

'''
Part 2
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

'''

def part2(data):
    '''
    difference between the first and second three-measurement windows(3).
    i and i+3 elements are compared.
    '''
    total=0
    for i in range(len(data)):
        if i+3<len(data):
            if data[i]<data[i+3]:
                total+=1
    print('part2',total)

part1(data)
part2(data)


