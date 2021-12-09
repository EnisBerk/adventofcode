'''
tools for advent code day 8
'''
from collections import Counter

def load_data(text):
    '''
    load data from file
    '''
    data = text.strip().split('\n')
    print(data)
    data = [x.split('|') for x in data]
    data = [[x[0].strip().split(' '),x[1].strip().split(' ')] for x in data]
    return data


def part1(text):
    '''
    find count of unique integers 1,4,7,8
        int:len
        1:2,4:4,7:3,8:7
    '''
    data = load_data(text)
    counter = Counter()
    for _,output_values in data:
        output_values = [len(i) for i in output_values]
        counter+=Counter(output_values)
    return counter[2]+counter[4]+counter[3]+counter[7]


def count_common_elements(x,y):
    '''
    count common elements in two lists
    '''
    return len(set(x)&set(y))

def part2(text):

    data = load_data(text)
    total = 0    
    for signals,output_values in data:
        signatures = {len(s):s for s in signals}
        number_string = ''
        for output_value in output_values:
            length = len(output_value)
            common_4 = count_common_elements(signatures[4],output_value)
            common_2 = count_common_elements(signatures[2],output_value)

            if length == 2:
                number_string+='1'
            elif length == 3:
                number_string+='7'
            elif length == 4:
                number_string+='4'
            elif length == 7:
                number_string+='8'
            elif length == 5:
                if common_4 == 2:
                    number_string+='2'
                else:
                    if common_2 == 1:
                        number_string+='5'
                    else:
                        number_string+='3'
            elif length == 6:
                if common_4==4:
                    number_string+='9'
                else:
                    if common_2 == 2:
                        number_string+='0'
                    else:
                        number_string+='6'
        number_string = int(number_string)
        total+=number_string
    return total
