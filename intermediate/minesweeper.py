'''In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]'''

import numpy as np
import scipy.signal
def minesweeper(matrix):
    Array=np.array(matrix).astype(int)
    Output=scipy.signal.convolve2d(Array,np.ones((3,3)),mode='same')-Array
    return Output
    