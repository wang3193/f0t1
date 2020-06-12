#map reduce
def f(x):
    return x*2
r = map(f, [2,3,4,5,6])
print(list(r))

from functools import reduce
def add(x, y):
    return x + y
print(reduce(add,[2,3,4,5]))

# filter
def is_odd(n):
    return n%2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7])))

#sorted
print(sorted([2,1,7,6,9,5]))
