import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]

data = [(10, 1705),
        (11, 1925),
        (12, 2200),
        (13, 2530),
        (14, 2860),
        (15, 3245),
        (16, 3630),
        (17, 4070),
        (18, 4510),
        (19, 5005),
        (20, 5500),
        (21, 5885),
        (22, 6875),
        (23, 7975),
        (27, 13970),
        (30, 20570),
        (31, 23155),
        (35, 34760),
        ]

# 解压数据
x, y = zip(*data)

# 绘图
plt.plot(x, y, color="blue", linewidth=0.5)

# 添加圆点和从数据点到 x 轴和 y 轴的虚线
for i in range(len(x)):
    plt.plot(x[i], y[i], "o", color="blue")  # 圆点标记
    plt.plot([x[i], x[i]], [0, y[i]], color="grey", linestyle="--", linewidth=0.5)  # 从数据点到 x 轴的虚线
    plt.plot([0, x[i]], [y[i], y[i]], color="grey", linestyle="--", linewidth=0.5)  # 从数据点到 y 轴的虚线

# 设置坐标轴
plt.xticks(x)  # x 轴显示所有的 x 值
plt.yticks(y)  # y 轴显示所有的 y 值

# 标签
plt.xlabel("阶数", fontsize=9)
plt.ylabel("攻击", fontsize=9)
plt.show()

y = [value for _, value in data]

# 计算每两个 y 值的差
y_diff = [y[i] - y[i - 1] for i in range(1, len(y))]

# 打印结果
print("y 值:", y)
print("y 差值:", y_diff)
