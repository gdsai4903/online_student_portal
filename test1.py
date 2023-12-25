from functools import reduce

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add(a, b):
    return a + b

print(reduce(add, ls))