# write a function that takes an integer n as an argument
#  and prints the n first lines of a Pascal Triangle

import math
from functools import reduce


def pascal(n):
    for i in range(n) :
        print(" ".join(str(x) for x in pascal_line(i)))
        

def pascal_line(n):
    arr = []
    for i in range(n+1):
        arr.append(pascal_cell(i,n ))   
    return arr


def pascal_cell(i,j):
    return (
        math.floor(factorial(j)/ (factorial(i) * factorial(j -i)))
    )

def factorial(n):
    if n < 2:
        return 1
    items = [x for x  in range(1,n+1)]
    return reduce(lambda x,y: x * y, items)
