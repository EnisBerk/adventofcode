'''
tools for advent code day 12
'''


from calendar import c
from numpy import isin


def load_data(text):
    '''
    load data from file
    '''
    data = text.strip().split('\n')
    empty_line = data.index('')

    coordinates = [line.split(',') for line in data[:empty_line]]
    folds = [line.split('=') for line in data[empty_line+1:]]
    return coordinates, folds


def fold(data,y_fold=-1,x_fold=-1):
    '''
    '''
    if y_fold == -1 and x_fold == -1:
        return {}
    if y_fold != -1:
        new_set = set()
        for x,y in data:
            if y>y_fold:
                new_set.add((x,(2*y_fold)-y))
            elif y==y_fold:
                print(x,y,y_fold)
            else:
                new_set.add((x,y))

    if x_fold != -1:
        new_set = set()
        for x,y in data:
            if x>x_fold:
                new_set.add((2*x_fold-x,y))
            else:
                new_set.add((x,y))

    return new_set 

def part1(text):
    '''
    '''
    coordinates,folds = load_data(text)
    coordinates = [tuple(map(int, c)) for c in coordinates]
    folds = [(c[0][-1],int(c[1])) for c in folds]
    matrix = set(coordinates)
    for fold_t in folds[:1]:
        fold_type=fold_t[0]
        fold_value=fold_t[1]
        if fold_type == 'x':
            matrix = fold(matrix,x_fold=fold_value)
        elif fold_type == 'y':
            matrix = fold(matrix,y_fold=fold_value)


    return len(matrix)

def part2(data):
    '''
    '''
    coordinates,folds = load_data(data)
    coordinates = [tuple(map(int, c)) for c in coordinates]
    folds = [(c[0][-1],int(c[1])) for c in folds]
    matrix = set(coordinates)
    for fold_t in folds:
        fold_type=fold_t[0]
        fold_value=fold_t[1]
        if fold_type == 'x':
            matrix = fold(matrix,x_fold=fold_value)
        elif fold_type == 'y':
            matrix = fold(matrix,y_fold=fold_value)
    matrix  = sorted(list(matrix))
    x_max = max([x for x,y in matrix])
    y_max = max([y for x,y in matrix])
    for row in range(y_max+1):
        for col in range(x_max+1):
            if (col,row) in matrix:
                print('#',end='')
            else:
                print('.',end='')
        print('\n',end='')
    