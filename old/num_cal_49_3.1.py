"""
    Author:Cao Tianhao
    stuNumber:S210231006
    Problem:Page49 3.1
    Date:2021-10-22
    Version:1.0
"""

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7]
y = [72, 108, 140, 150, 174, 196, 208]

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum01 = 0
sum02 = 0

for i in range(0, 7):
    sum1 += 1
for i in range(0, 7):
    sum2 += x[i]
for i in range(0, 7):
    sum3 += x[i]
for i in range(0, 7):
    sum4 += x[i] ** 2
for i in range(0, 7):
    sum01 += y[i]
for i in range(0, 7):
    sum02 += x[i] * y[i]

A = np.array([[sum1, sum2], [sum3, sum4]])
b = np.array([sum01, sum02])
# print(A)
ans = np.linalg.solve(A, b)

print("a =", ans[0])
print(430 / 7)
print("b =", ans[1])
print(309 / 14)

plt.scatter(x, y)
plt.show()
