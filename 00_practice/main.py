# # 입력 - n, k
# n = list(map(int, input().split()))
# print(n)
# cnt = 0
#
# # 00시 00분 00초 ~ n시 59분 59초?
# for i in range(n + 1):
#     for j in range(60):
#         for k in range(60):
#             if 3 in str(i) + str(j) + str(k):
#                 cnt += 1
#
# print(cnt)