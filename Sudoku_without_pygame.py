# Edit the sudoku_board grid to solve your grid of choice
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
            print('-------------------')            #for visual segregation of squares,horizontal and vertical lines are drawn
        for j in range(len(sudoku_board[0])):
            if j%3==0 and j!=0:
                print('|' , end='')
            if j==len(sudoku_board[0])-1:
                print(sudoku_board[i][j])
            else:
                print(str(sudoku_board[i][j])+" ",end='')

def valid_number(sudoku_board,number,pos):            # A valid number must satisfy row,column and square conditions
    row=pos[0]
    col=pos[1]
    for i in range(len(sudoku_board[0])):               # Checking if the number is not present in its row
        if sudoku_board[row][i]==number and col!=i:
            return False
    
    for i in range(len(sudoku_board)):                  # Checking if the number is not present in its column
        if sudoku_board[i][col]==number and row!=i:
            return False
    
    # row//3 does integer division. So (row//3)*3 makes the total grid into 3 squares 

    for i in range((row//3)*3,(row//3)*3+3):            # Checking if the number is not present in its square
        for j in range((col//3)*3,(col//3)*3+3):
            if sudoku_board[i][j]==number and i!=row and j!=col:
                return False
    
    return True

def locate_empty_spaces(sudoku_board):
    for i in range(len(sudoku_board)):              # Locate if a empty space (0) is present in the grid while traversing from top left to bottom right row by row
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j]==0:
                return (i,j)
    return None

def backtracking_solver(sudoku_board):              
    vacant=locate_empty_spaces(sudoku_board)        # If there is a vacant space, then sudoku is not complete
    if not vacant:
        return True
    else:                                           # for every vacant space put start from smallest valid number for that space.If such a valid number exists, then proceed to next vacant space
        row,col=vacant
    for i in range(1,10):                           # If no valid number exists, then go to previous box and iterate to its next valid number
        if valid_number(sudoku_board,i,(row,col)):
            sudoku_board[row][col]=i
            if backtracking_solver(sudoku_board):
                return True                         #When the whole grid is complete, it returns true and hence solved
            sudoku_board[row][col]=0
    return False

print_board(sudoku_board)
backtracking_solver(sudoku_board)
print('                     ')
print_board(sudoku_board)
