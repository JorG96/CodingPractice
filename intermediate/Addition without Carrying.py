'''A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.

Given two integers, your task is to find the result that the child will get.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.'''

def additionWithoutCarrying(param1, param2):
    p1,p2=str(param1),str(param2)
    m=max(len(p1),len(p2))
    if len(p1)<m:
        p1=('0'*(m-len(p1)))+p1
    
    elif len(p2)<m:
        p2=('0'*(m-len(p2)))+p2
    digits=[int(a) + int(b) for a, b in zip(p1, p2)]
    res=int("".join([str(i)[-1] for i in digits]))
    return res
