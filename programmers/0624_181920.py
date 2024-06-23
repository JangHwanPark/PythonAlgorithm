def solution(sn, en):
    li = []
    for i in range(sn, en + 1):
        li.append(i)
    return li


def solution2(sn, en):
    return list(range(sn, en + 1))


def solution3(sn, en):
    return [i for i in range(sn, en + 1)]


def solution4(sn, en):
    li = []
    while sn <= en:
        li.append(sn)
        sn += 1
    return li


sn = 3
en = 10
print(solution(sn, en))
print(solution2(sn, en))
print(solution3(sn, en))
print(solution4(sn, en))