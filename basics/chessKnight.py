'''Given a position of a knight on the standard chessboard,
find the number of different moves the knight can perform.
for cell="a1" the output should be:
    chessKnight(cell)=2
for cell="c2" the output should be:
    chessKnight(cell)=6
'''
from itertools import product
def chessKnight(cell):
    x, y = ord(cell[0])-97,int(cell[1])-1
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return len(moves)
