'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.
'''
import numpy as np
def sudoku2(grid):
    arr=np.array(grid)
    for i in range(9):
        if isRow_Valid(arr[i,:]) and isCol_Valid(arr[:,i]):
            continue
        else: return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if checkSub(arr[i:i+3,j:j+3]):
               continue
            else: return False
    return True
        
     

def isRow_Valid(row):
    rowSet=set()
    for i in row:
        if i in rowSet:
            return False
        elif i!='.':
            rowSet.add(i)

    return True

def isCol_Valid(col):
    colSet=set()
    for i in col:
        if i in colSet:
            return False

        elif i!='.':
            colSet.add(i)
    return True
    
def checkSub(sub):
    _sub=sub.flatten()
    subSet=set()
    for i in _sub:
        if i in subSet:
            return False
        elif i!='.':
            subSet.add(i)

    return True
    

