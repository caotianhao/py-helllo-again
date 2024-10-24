import numpy as np
import matplotlib.pyplot as plt

# x,y为题目给定数据
x = [0, 3, 5, 7, 9, 11, 12, 13, 14, 15]
y = [0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6]

# n+1为最终画图点的个数
n = 999

# 将x，y转化为array格式，并求长度
data_x = np.array(x)
sx = len(data_x)
data_y = np.array(y)

# x_为n+1个点的横坐标，y_为对应的值
x_ = np.linspace(x[0], x[sx - 1], n)
y_ = np.zeros(shape=(1, n))

# 最终的拉格朗日函数有sx个基函数
# 对每个基函数分别求对应的y值，存储在tmp中
# 最后求和得到最终的函数的y值
for i in range(sx):
    tmp = np.zeros(shape=(1, n))
    tmp += data_y[i]
    for j in range(sx):
        if j == i:
            continue
        else:
            tmp = tmp * (x_ - data_x[j]) / (data_x[i] - data_x[j])
    y_ += tmp

# 画图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x_, y_)
plt.show()
