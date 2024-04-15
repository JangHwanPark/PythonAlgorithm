# Beginner
def solution1(n):
    if n < 90:
        return 1
    elif n == 90:
        return 2
    elif 90 < n < 180:
        return 3
    else:
        return 4


def print_solution1(n):
    for i in n:
        print(solution1(i))


n = [70, 91, 180, 90]
print_solution1(n)


# Middle
def solution2():
    return 0


def solution3():
    return 0
