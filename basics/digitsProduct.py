'''Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.'''


def getProduct(n):
    N = 1
    num = str(n)
    for i in num:
        N = N * int(i)
    return N
    
def digitsProduct(product):
    for i in range(1,10000):
        if product==getProduct(i):
            return i
        else: continue
    return -1