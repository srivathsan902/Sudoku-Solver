sudoku_board = [
    [8,0,4,7,0,0,1,0,0],
    [0,6,0,0,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,9],
    [0,0,0,0,0,8,0,1,0],
    [7,0,5,4,0,0,8,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,1,0,6,0,0,0,0,0],
    [5,0,6,0,7,0,0,2,0],
    [0,3,0,0,0,0,5,0,0]
]

def print_board(sudoku_board):
    for i in range(len(sudoku_board)):
        if i%3==0 and i!=0:
            print('-------------------')
        for j in range(len(sudoku_board[0])):
            if j%3==0 and j!=0:
                print('|' , end='')
            if j==len(sudoku_board[0])-1:
                print(sudoku_board[i][j])
            else:
                print(str(sudoku_board[i][j])+" ",end='')

def valid_number(sudoku_board,number,pos):
    row=pos[0]
    col=pos[1]
    for i in range(len(sudoku_board[0])):
        if sudoku_board[row][i]==number and col!=i:
            return False
    
    for i in range(len(sudoku_board)):
        if sudoku_board[i][col]==number and row!=i:
            return False
    
    for i in range((row//3)*3,(row//3)*3+3):
        for j in range((col//3)*3,(col//3)*3+3):
            if sudoku_board[i][j]==number and i!=row and j!=col:
                return False
    
    return True

def locate_empty_spaces(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j]==0:
                return (i,j)
    return None

def backtracking_solver(sudoku_board):
    vacant=locate_empty_spaces(sudoku_board)
    if not vacant:
        return True
    else:
        row,col=vacant
    for i in range(1,10):
        if valid_number(sudoku_board,i,(row,col)):
            sudoku_board[row][col]=i
            if backtracking_solver(sudoku_board):
                return True
            sudoku_board[row][col]=0
    return False

print_board(sudoku_board)
backtracking_solver(sudoku_board)
print('                     ')
print_board(sudoku_board)
