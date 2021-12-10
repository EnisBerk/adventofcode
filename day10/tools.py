'''
tools for advent code day 10
'''
from collections import deque


def load_data(text):
    '''
    load data from file
    '''
    data = text.strip().split('\n')

    return data


def is_left(char):
    '''
    check if char is left
    '''
    left = {'{', '[', '(', '<'}
    return char in left


def is_right(char):
    '''
    check if char is right
    '''
    right = {'}', ']', ')', '>'}
    return char in right


def other_side(char):
    '''
    get corresponding char
    '''
    left = {
        '{': '}',
        '}': '{',
        '[': ']',
        ']': '[',
        '>': '<',
        '<': '>',
        '(': ')',
        ')': '(',
    }
    return left[char]


def calc_part1_score(illegal_counts):
    '''
    calculate part 1 score
    '''
    score_per_char = {
        ')': 3,
        '}': 1197,
        ']': 57,
        '>': 25137,
    }
    for char, count in illegal_counts.items():
        score_per_char[char] *= count

    return sum(score_per_char.values())


def calc_part2_line_score(completing_chars):
    '''
    calculate part 2 score
    '''
    score_per_char = {
        ')': 1,
        '}': 3,
        ']': 2,
        '>': 4,
    }
    total_score = 0
    for char in completing_chars:
        total_score *= 5
        total_score += score_per_char[char]

    return total_score


def is_valid(line):
    '''
    check if line is valid
    '''
    stack = deque()
    for char in line:
        if is_left(char):
            stack.append(char)
        else:
            if len(stack) == 0:
                return char
            if other_side(stack[-1]) == char:
                stack.pop()
            else:
                return char
    return stack


def part1(data):
    '''
    part 1
    '''
    data = load_data(data)
    illegal_counts = {
        ')': 0,
        '}': 0,
        ']': 0,
        '>': 0,
    }
    for line in data:
        out = is_valid(line)
        if isinstance(out, str):
            illegal_counts[out] += 1

    score = calc_part1_score(illegal_counts)
    return score


def part2(data):
    '''
    part 2
    '''
    data = load_data(data)

    scores = []
    for line in data:
        completing_chars = []
        out = is_valid(line)
        if isinstance(out, deque) and len(out) > 0:
            while len(out) > 0:
                char = out.pop()
                completing_chars.append(other_side(char))
            line_score = calc_part2_line_score(completing_chars)
            scores.append(line_score)
    scores.sort()
    return scores[len(scores) // 2]
