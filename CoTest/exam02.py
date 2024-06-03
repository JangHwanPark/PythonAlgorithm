# 수열
sqe = [1, 2, 3, 4, 5, 6]
print(sqe)


# 등차 수열
def arithmetic_sqe(a,d,n):
    return [a + d * i for i in range(n)]


sqe1 = arithmetic_sqe(1, 1, 10)
sqe2 = arithmetic_sqe(1, 2, 10)
sqe3 = arithmetic_sqe(2, 2, 10)
print(sqe1)
print(sqe2)
print(sqe3)


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