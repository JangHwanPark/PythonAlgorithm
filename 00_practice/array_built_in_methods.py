import random


def random_list(range_num, start_num, end_num):
    arr = []
    for i in range(range_num):
        arr.append(random.randint(start_num, end_num))
    return arr


print('random_list:', random_list(10, 1, 25))