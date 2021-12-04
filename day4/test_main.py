'''
tests for main.py
'''
from main import *

complete_example_data = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

single_board = [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5],
                                  [19, 8, 7, 25, 23], [20, 11, 10, 24, 4],
                                  [14, 21, 16, 12, 6]]

single_board_2 = [[77, 79, 88, 74, 12], [21, 9, 85, 26, 68],
                                    [11, 62, 64, 4, 5], [47, 33, 76, 63, 87],
                                    [55, 19, 2, 60, 95]]

def test_board_load_board():
    '''
    test board_load_board
    '''
    board = Board(single_board)
    board_2 = Board(single_board_2)
    assert board.element_list == [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5],
                                  [19, 8, 7, 25, 23], [20, 11, 10, 24, 4],
                                  [14, 21, 16, 12, 6]]
    assert board_2.element_list == [[77, 79, 88, 74, 12], [21, 9, 85, 26, 68],
                                    [11, 62, 64, 4, 5], [47, 33, 76, 63, 87],
                                    [55, 19, 2, 60, 95]]
    assert board.values[3].value==3
    assert board.values[3].marked==False
    assert board.values[15].row==0
    assert board.values[15].col==1
    assert board.board_size==5


def test_board_mark_element():

    board = Board(single_board)
    element = Element(0, 0,10)
    element2 = Element(0, 2,100)

    assert board.mark_element(element) == None
    assert element.marked == True
    assert element2.marked == False


def test_board_check_bingo():
    '''
    test board_check_bingo
    '''
    board = Board(single_board)
    assert board.check_bingo(0, 0) == False
    for i in range(5):
        board.mark_element(Element(i, 0,100))
    assert board.check_bingo(0, 0) == True
    assert board.check_bingo(0, 1) == False



def test_find_winning_board():
    '''
    test find_winning_board
    '''
    complete_example = complete_example_data.split('\n')
    complete_example = [line.strip() for line in complete_example]
    bingo_picks,boards=load_boards(complete_example)
    score=find_winning_board(bingo_picks,boards)
    
    assert score==4512


def test_find_loser_board():
    complete_example = complete_example_data.split('\n')
    complete_example = [line.strip() for line in complete_example]
    bingo_picks,boards=load_boards(complete_example)
    score=find_loser_board(bingo_picks,boards)
    assert score==1923
    