from itertools import accumulate

list1 = [1,2,3,4,5]
prefix = list(accumulate(list1))
print(prefix)