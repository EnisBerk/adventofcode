'''
Solution for Advent of Code 2021 Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3

'''


input_file = 'day3/input'

with open(input_file, encoding='utf-8') as f:
    data = f.readlines()
    data = [line.strip() for line in data]


def cal_eps_gama_rate(common_bit):

    gamma_rate = ''.join(str(x) for x in common_bit)
    epsilon_rate = ''.join([ '0' if x==1 else '1' for x in common_bit ])
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate,epsilon_rate

    
def get_most_common_bits(data):
    '''
    Find most common bits in the data set.
    '''

    counters = [0 for i in range(len(data[0]))]
    for line in data:
        counters = [x + int(y) for x, y in zip(counters, line)]
    
    common_bit=[]
    for counter in counters:
        if counter>(len(data)//2):
            common_bit.append(1)
        elif counter==(len(data)//2):
            print('No common bit?')
        else:
            common_bit.append(0)
    return common_bit


def get_power_consumption(data):
    '''
    Calcuate power cons. from gamma and epsilon rate.
    '''
    common_bit = get_most_common_bits(data)
    gamma_rate, epsilon_rate = cal_eps_gama_rate(common_bit)
    return gamma_rate * epsilon_rate

power_consumption = get_power_consumption(data)
print(f'Power consumption: {power_consumption}')


