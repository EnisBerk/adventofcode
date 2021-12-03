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



def test_get_most_common_bits():
    '''
    test get_most_common_bits
    '''
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010', 
        '01010'
    ]
    input_answ = [((data,0),[1,0,0,0,0]),
                  ((data,1),[0,0,0,0,0]),]
    for idex, ans in input_answ:
        assert get_most_common_bits(*idex) == ans


def test_cal_oxygen_and_scrubber_rating():
    '''
    test cal_oxygen_and_scrubber_rating
    '''
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010', 
        '01010'
    ]

    assert cal_rating(data,bit_index_start=0,common=True) == '10111'
    assert cal_rating(data,bit_index_start=0,common=False) == '01010'

def test_get_life_support_rating():
    '''
    test get_life_support_rating
    '''
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010', 
        '01010'
    ]
    assert get_life_support_rating(data) == 230
