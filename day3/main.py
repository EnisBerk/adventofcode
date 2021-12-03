'''
Solution for Advent of Code 2021 Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3

'''
from typing import Tuple,List

input_file = 'day3/input'

with open(input_file, encoding='utf-8') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

### Part 1
def cal_eps_gama_rate(common_bit):

    gamma_rate = ''.join(str(x) for x in common_bit)
    epsilon_rate = ''.join([ '0' if x==1 else '1' for x in common_bit ])
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate,epsilon_rate

    
def get_most_common_bits(data,bit_index=-1):
    '''
    Find most common bits in the data set.
    '''
    
    counters = [0 for i in range(len(data[0]))]
    for line in data:
        if bit_index==-1:
            counters = [x + int(y) for x, y in zip(counters, line)]
        else:
            counters[bit_index] = counters[bit_index] + int(line[bit_index])
    
    common_bit=[]
    for counter in counters:
        if counter>(len(data)/2):
            common_bit.append(1)
        elif counter==(len(data)/2):
            common_bit.append(1)
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

#### Part 2 

def cal_rating(data,bit_index_start=0,common=True):
    '''
    Calculate ratings for the data set with common or common bits.

    '''

    reference_bits = get_most_common_bits(data,bit_index_start)

    if not common:
        reference_bits = ''.join([ '0' if x==1 else '1' for x in reference_bits ])
    else:
        reference_bits = ''.join(str(x) for x in reference_bits)

    data = [ x for x in data if x[bit_index_start]==reference_bits[bit_index_start]  ]
    if len(data)>1:
        return cal_rating(data,bit_index_start+1,common)
    else:
        return data[0]



def get_life_support_rating(data):
    '''
    Calcuate life support rating from gamma and epsilon rate.
    '''
    oxygen_generator_rating = cal_rating(data[:],bit_index_start=0,common=True)
    scrubber_rating = cal_rating(data[:],bit_index_start=0,common=False)

    oxygen_generator_rating = int(oxygen_generator_rating,2)
    scrubber_rating = int(scrubber_rating,2)
    return oxygen_generator_rating * scrubber_rating



life_support_rating =  get_life_support_rating(data)
print(f'Life support rating: {life_support_rating}')