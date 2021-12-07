'''
tools for advent code day 6
'''


def load_data(text):
    '''
    load data from file
    '''
    return map(int,text.strip().split(','))


def accumulate_initial_fish_cycles(data):
    '''
    count the number of fish in the lake
    '''

    initial_state = [0 for i in range(7)]
    for fish in data:
        initial_state[fish] += 1

    return initial_state

def run_cycles(days,initial_state):
    kids=[0,0]
    for i in range(days):
        i = i%7
        growing_kids = kids[0]
        kids[0],kids[1] = kids[1],initial_state[i]
        initial_state[i]+= growing_kids

    return sum(initial_state)+sum(kids)



def part1(text,days):
    '''
    calculate the number of fish in the lake
    '''
    data = load_data(text)
    initial_state = accumulate_initial_fish_cycles(data)
    total_count = run_cycles(days,initial_state)
    return total_count

def part2(text,days):
    return part1(text,days)

