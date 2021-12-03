'''
tests for main.py
'''

from main import *


def test_get_most_common_bits():
    data = [
        '00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010'
    ]
    assert get_most_common_bits(data) == [1,0,1,1,0]

def test_cal_eps_gama_rate():
    '''
    test cal_eps_gama_rate
    '''
    data = [
        '00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010'
    ]
    common_bit = [1,0,1,1,0]
    assert cal_eps_gama_rate(common_bit) == (22,9)


def test_get_power_consumption():
    '''
    test get_power_consumption
    '''
    data = [
        '00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010'
    ]
    assert get_power_consumption(data) == 198



