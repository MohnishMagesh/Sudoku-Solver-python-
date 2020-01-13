sudoku_grid = [[0,8,0,3,0,5,4,9,6],
               [4,0,0,0,0,9,1,0,7],
               [6,2,9,4,0,1,0,3,5],
               [0,0,0,0,0,0,6,0,8],
               [0,0,0,5,1,8,7,0,0],
               [0,1,0,0,9,6,0,0,2],
               [1,6,0,0,3,0,0,0,4],
               [5,4,2,1,8,0,9,6,0],
               [0,0,8,0,5,4,2,7,1]]

def sudoku_rules(number, row_no, col_no):
    RULE_1 = True
    RULE_2 = True
    RULE_3 = True

    for i in range(9):
        # check same col_no for similar entry (RULE_1)
        if((sudoku_grid[i][col_no]==number)):
            # Rule is violated
            RULE_1 = False


    for i in range(9):
        # check same row_no for similar entry (RULE_2)
        if((sudoku_grid[row_no][i]==number)):
            # Rule is violated
            RULE_2 = False


    for i in range(3):
        # check same grid for similar entry (RULE_3)
        for j in range(3):
            if(sudoku_grid[i+(row_no-row_no%3)][j+(col_no-col_no%3)]==number):
                RULE_3 = False

    if(RULE_1 and RULE_2 and RULE_3):
        return True

    return False


def emptyPlaceFinder():
    # checks for empty places in the sudoku_grid
    for row in range(9):
        for col in range(9):
            if(sudoku_grid[row][col]==0):
                return True
    return False

def findBlankCell():
    # means there exists no coordinates with
    cell_coordinates = [-1,-1]
    for i in range(9):
        for j in range(9):
            if(sudoku_grid[i][j]==0):
                cell_coordinates[0] = i
                cell_coordinates[1] = j
                return cell_coordinates
    cell_coordinates[0] = -1
    cell_coordinates[1] = -1
    return cell_coordinates

def sudokuSolver(sudoku_grid):
    cell_location = findBlankCell()
    row = cell_location[0]
    col = cell_location[1]
    # grid is full, exit
    if(emptyPlaceFinder()==False):
        return True
    # keep assigning values anywhere between 1 to 9
    for num in range(1,10):
        if(sudoku_rules(num, row, col)==True):
            # assign new number to empty cell_location
            sudoku_grid[row][col] = num
            if(sudokuSolver(sudoku_grid)):
                return True
            # backtrack the changes since it is incorrect
            sudoku_grid[row][col] = 0
    return False

def printSolvedPuzzle():
    for row in range(9):
        print(sudoku_grid[row])

sudokuSolver(sudoku_grid)
printSolvedPuzzle()
