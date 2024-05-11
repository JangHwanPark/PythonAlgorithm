import matplotlib.pyplot as plt
import numpy as np

# x 값의 범위를 설정
x = np.linspace(-10, 10, 400)
# 함수 정의
y = x**3 + 3*x**2 + 4*x + 2

# 그래프를 그리는 부분
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x^3 + 3x^2 + 4x + 2')
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()