'''Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.'''
import numpy as np
def sudoku(grid):
    arr=np.array(grid)
    res=[]
    #check rows
    for row in range(9):
        if sorted(arr[row])!=sorted(range(1,10)):
            return False

    #check columns
    for column in range(9):
        if sorted(arr[:,column])!=sorted(range(1,10)):
            return False
    #check 3x3 array
    for j in range(0,9,3):
        for i in range(0,9,3):
            tmp=arr[j:j+3,i:i+3]
            if sorted(tmp.flatten())!=sorted(range(1,10)):
                return False
    return True
