# 수열
sqe = [1, 2, 3, 4, 5, 6]
print(sqe)


# 등차 수열
def arithmetic_sqe(a, d, n):
    return [a + d * i for i in range(n)]


sqe1 = arithmetic_sqe(1, 1, 10)
sqe2 = arithmetic_sqe(1, 2, 10)
sqe3 = arithmetic_sqe(2, 2, 10)
print(sqe1)
print(sqe2)
print(sqe3)


# 등차 수열의 합
def arithmetic_sum(a, d, n):
    l = a + (n - 1) * d
    return n * (a + l) // 2


sqe_sum1 = arithmetic_sum(1, 1, 10)
sqe_sum2 = arithmetic_sum(1, 2, 6)
sqe_sum3 = arithmetic_sum(2, 2, 10)
print(sqe_sum1)
print(sqe_sum2)
print(sqe_sum3)


# 리턴값으로 합 구하기
def arithmetic_return_sum(sequence):
    return sum(sequence)


return_sum1 = arithmetic_return_sum(sqe1)
return_sum2 = arithmetic_return_sum(sqe2)
return_sum3 = arithmetic_return_sum(sqe3)
print(return_sum1)
print(return_sum2)
print(return_sum3)


# 등비 수열
def geometric_sqe(a, r, n):
    return [a * (r ** i) for i in range(n)]


# 첫 항 a, 공비 r, 항의 개수 n
g_sqe1 = geometric_sqe(1, 1, 10)
g_sqe2 = geometric_sqe(1, 2, 10)
g_sqe3 = geometric_sqe(2, 2, 10)
g_sqe4 = geometric_sqe(2, 3, 10)
print(g_sqe1)
print(g_sqe2)
print(g_sqe3)
print(g_sqe4)