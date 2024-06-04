n1 = int(input())
list1 = []

for i in range(0, n1):
    list1.append(int(input()))

print(list1)
for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)