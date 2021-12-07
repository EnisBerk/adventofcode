'''
tools for advent code day 7
'''


def load_data(text):
    '''
    load data from file
    '''
    return map(int,text.strip().split(','))



def part1(text):
    '''
    calculate the number of fish in the lake
    '''
    data = load_data(text)
    locations = sorted(data)
    # print(locations)
    meeting_point = locations[len(locations)//2]
    fuel_amount =  calc_fuel(locations,meeting_point)
    return fuel_amount

def  calc_fuel(locations,meeting_point):
    return sum([abs(meeting_point-x) for x in locations])

def calc_fuel_part2(locations,meeting_point):
    fuel_amount = 0
    for x in locations:
        n = abs(meeting_point-x)
        cost = (n*(n+1))/2
        fuel_amount += cost
    return fuel_amount


def part2(text):
    data = load_data(text)
    locations = sorted(data)
    meeting_point = locations[len(locations)//2]
    initial_fuel = calc_fuel_part2(locations,meeting_point)
    lowest=initial_fuel
    for i in range(0,locations[-1]):
        fuel = calc_fuel_part2(locations,i)
        if fuel < lowest:
            lowest = fuel
    return lowest
