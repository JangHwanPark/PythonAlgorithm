import random
from itertools import accumulate
from itertools import permutations
from itertools import combinations


# 누적합 (PrefixSum)
def prefix_sum(data):
    prefix = list(accumulate(data))
    return prefix


# 순열 (Permutations)
def permutation(data):
    res = []
    for perm in permutations(data):
        res.append(perm)
    return res


# 조함 (Combinations)
def combination(data2):
    res = []
    for comb in combinations(data2, 2):
        res.append(comb)
    return res


data = [1, 2, 3, 4, 5]
data2 = [1, 2, 3]
print(prefix_sum(data))
print(permutation(data2))
print(combination(data2))