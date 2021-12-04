'''
Solution for Advent of Code 2021 Day 4: Giant Squid
https://adventofcode.com/2021/day/4

'''

class Element():
    def __init__(self, row, col,value,marked=False):
        self.value = value
        self.row = row
        self.col = col
        self.marked = marked


class Board():
    def __init__(self,element_list,):
        self.element_list = element_list
        self.board_size = len(self.element_list)
        self.values = {}
        self.rows = {}
        self.cols = {}
        self.bingo=False
        if self.element_list:
            self.load_board()

    def load_board(self,):
        '''
        Load the board values into hashmap'''

        for row_i,row in enumerate(self.element_list):
            for col_i,value in enumerate(row):
                self.values[value]=(Element(row_i,col_i,value))

        for i in range(self.board_size):
            self.cols[i]=self.board_size
            self.rows[i]=self.board_size

    def check_element(self, value):
        element = self.values.get(value,None)
        return element


    def mark_element(self, element):
        '''
        Mark the element as marked and update the rows and cols'''

        element.marked = True
        self.mark_rows_cols(element)
        if self.check_bingo(element.row,element.col):
            return element
        else:
            return None

    def mark_rows_cols(self, element):
        self.rows[element.row] -= 1
        self.cols[element.col] -= 1

    def check_bingo(self, row,col):
        if self.rows[row] == 0:
            return True
        if self.cols[col] == 0:
            return True
        return False

    def calculate_score(self,bingo_element):
        '''
        Calculate the score with winning element after bingo'''
        score=0
        for element in self.values.values():
            if not element.marked:
                score+=element.value
        score*=bingo_element.value
        return score

input_file = 'day4/input'

with open(input_file, encoding='utf-8') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

def load_boards(data):
    bingo_picks = [int(i) for i in data[0].split(",")]
    print(bingo_picks)
    boards=[]
    board=[]
    for line in data[1:]:
        if not line:
            if board:
                # print(board)
                boards.append(Board(board))
            board=[]
        if line:
            row=[int(r.strip()) for r in line.split(" ") if r]
            board.append(row)
    if board:
        print(board)
        boards.append(Board(board))


    return bingo_picks,boards

bingo_picks,boards=load_boards(data)

def find_winning_board(bingo_picks,boards):
    for bingo_pick in bingo_picks:
        for board in boards:
            element=board.check_element(bingo_pick)
            if element:
                if board.mark_element(element):
                    print('BINGO')
                    score=(board.calculate_score(element))
                    return score

score=find_winning_board(bingo_picks,boards)
print(f'The winning score is {score}')

def find_loser_board(bingo_picks,boards):
    last_bingo_board=last_bingo_element=None
    bingo_count=0
    # print(boards)
    for bingo_pick in bingo_picks:
        for i,board in enumerate(boards):
            if board.bingo:
                continue
            # print('index',i)
            element=board.check_element(bingo_pick)
            if element:
                if board.mark_element(element):
                    board.bingo=True
                    last_bingo_board=board
                    last_bingo_element=element
                    bingo_count+=1
                    score=last_bingo_board.calculate_score(last_bingo_element)
                    print('score',score)
        print(bingo_count,len(boards))
        if bingo_count==len(boards) and last_bingo_board:
            print(len(boards))
            score=(last_bingo_board.calculate_score(last_bingo_element))
            print(f'The losing score is {score}')
            return score

bingo_picks,boards=load_boards(data)

find_loser_board(bingo_picks,boards)