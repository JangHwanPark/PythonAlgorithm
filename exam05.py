list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]


def trueandfalse(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True


print(trueandfalse(list1, list2))
