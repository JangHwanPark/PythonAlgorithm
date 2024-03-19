# 문자열 입력
a = input("값을 입력하세요.")

# 정수(int) 입력
b = int(input("값을 입력하세요."))

# 여러개의 정수(int) 입력
c = list(map(int, input("값을 입력하세요.").split()))

# 실수 입력
d = float(input("값을 입력하세요."))

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))