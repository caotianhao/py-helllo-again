import numpy as np
import matplotlib.pyplot as plt

# 已知数据点
x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 27, 30, 31, 35])
y = np.array([1705, 1925, 2200, 2530, 2860, 3245, 3630,
              4070, 4510, 5005, 5500, 5885, 6875, 7975,
              13970, 20570, 23155, 34760])

total = 0
for i in range(2, 10):
    coeffs = np.polyfit(x, y, i)
    poly = np.poly1d(coeffs)

    # 打印拟合的多项式表达式
    # print(poly)

    x_value = 24
    predicted_value = poly(x_value)
    total += predicted_value
    print(f"The predicted value when x = {x_value} is {predicted_value} when i = {i}")

print(total / 8)
# 可视化
# plt.scatter(x, y, label='Data Points')
# plt.plot(x, poly(x), label='Fitted Polynomial', color='red')
# plt.scatter(x_value, predicted_value, color='green', label='Predicted Value at x=33')
# plt.legend()
# plt.show()
