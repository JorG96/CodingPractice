'''Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1'''

def differentSquares(matrix):
    unique = set()
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            unique.add((matrix[row][col], matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1]))
    
    return len(unique)
