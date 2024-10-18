import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rc("font", family="SimHei")

x = np.arange(1, 21, 1)
y = [
    3475, 6950, 10425, 13900, 17375,
    20850, 24325, 27800, 31275, 34750,
    41700, 48650, 55600, 62550, 69500,
    83400, 97300, 111200, 125100, 139000,
]

plt.plot(x, y)
plt.xticks(np.arange(1, 21, 1.0))
plt.scatter(x, y, color="black", label="Data Points")
for xi, yi in zip(x, y):
    plt.scatter(xi, yi, color="black", marker="o")  # 标记点
    plt.vlines(
        xi, ymin=0, ymax=yi, linestyles="dashed", colors="b", alpha=0.5
    )  # 垂直虚线
    # plt.hlines(yi, xmin=0, xmax=xi, linestyles='dashed', colors='b', alpha=0.5)  # 水平虚线
plt.xlabel("装备阶数")
plt.ylabel("玄铁总数")
plt.show()  # 显示图形
