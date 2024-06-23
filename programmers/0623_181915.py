def solution(my_string, index_list):
    res = []

    # index_list의 각 인덱스를 순회
    for i in index_list:

        # my_string에서 해당 인덱스의 문자를 추출하여 temp에 추가
        res.append(my_string[i])
    return ''.join(res)


my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]

my_string2 = "zpiaz"
index_list2 = [1, 2, 0, 0, 3]
res2 = solution(my_string, index_list)
print(res2)
print(solution(my_string2, index_list2))
print(len(res2))