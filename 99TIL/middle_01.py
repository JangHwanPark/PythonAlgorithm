def solution(s):
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    res = ""
    temp = ""
    for i in s:
        if i.isdigit():
            res += i
        else:
            temp += i
            if temp in n:
                res += str(n.index(temp))
                temp = ""
    return int(res)


s = "one4seveneight"    # one / 4 seven / eight = 1478
s1 = "23four5six7"  # 23 four / 5 / six / 7 = 234567
s2 = "123"  # 123
print(solution(s))
