'''Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.'''

from itertools import combinations
def deleteDigit(n):
    N=list(str(n))
    a=[]
    for i in list(combinations(N,len(N)-1)):
        a.append(int("".join(i)))
    return max(a)
        