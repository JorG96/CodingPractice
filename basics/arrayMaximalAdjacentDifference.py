'''Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.'''

def arrayMaximalAdjacentDifference(inputArray):
    lst=[]
    for i in range(len(inputArray)-1):
        a,b=inputArray[i],inputArray[i+1]
        lst.append(abs(a-b))
    return max(lst)
