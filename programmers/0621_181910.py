def solution(my_string, n):
    res = ""
    temp = len(my_string) - n
    for i in range(temp, n + temp):
        res += my_string[i]
    return res


def solution2(my_str, n):
    return my_str[-n:]


print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))

print(solution2("ProgrammerS123", 11))
print(solution2("He110W0r1d", 5))