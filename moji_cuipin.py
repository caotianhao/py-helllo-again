import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]

# 数据
x = np.arange(1, 31)
y = [
    3475, 6950, 10425, 13900, 17375,
    20850, 24325, 27800, 31275, 34750,
    41700, 48650, 55600, 62550, 69500,
    83400, 97300, 111200, 125100, 139000,
    152900, 166800, 180700, 194600, 208500,
    222400, 236300, 250200, 264100, 278000,
]

# 绘图
plt.plot(x, y, color="blue", linewidth=0.5)

# 添加圆点和从数据点到 x 轴和 y 轴的虚线
for i in range(len(x)):
    plt.plot(x[i], y[i], "o", color="blue")  # 圆点标记
    plt.plot(
        [x[i], x[i]], [0, y[i]], color="grey", linestyle="--", linewidth=0.5
    )  # 从数据点到 x 轴的虚线
    plt.plot(
        [0, x[i]], [y[i], y[i]], color="grey", linestyle="--", linewidth=0.5
    )  # 从数据点到 y 轴的虚线

# 设置坐标轴
plt.xticks(x)  # x 轴显示所有的 x 值
plt.yticks(y)  # y 轴显示所有的 y 值

# 标签
plt.xlabel("阶数", fontsize=15)
plt.ylabel("玄铁", fontsize=15)
plt.show()
