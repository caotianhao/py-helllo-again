import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'

main_atk = [0] * 36

main_atk[10] = 3850
main_atk[11] = 4510
main_atk[12] = 5280
main_atk[13] = 6160
main_atk[14] = 7260
main_atk[15] = 8580
main_atk[16] = 10120
main_atk[17] = 11935
main_atk[18] = 14025
main_atk[19] = 16445
main_atk[20] = 19250
main_atk[21] = 22495
main_atk[22] = 26180
main_atk[23] = 30360
main_atk[24] = 35390
main_atk[25] = 40370
main_atk[26] = 46200
main_atk[27] = 52580
main_atk[28] = 59510
main_atk[29] = 66990
main_atk[30] = 75020
main_atk[31] = 83600
main_atk[32] = 92730
main_atk[33] = 102410
main_atk[34] = 112640
main_atk[35] = 123420

if __name__ == '__main__':
    x = list(range(10, len(main_atk)))
    y = main_atk[10:]

    # 创建图形
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', color='b')

    # 设置标题和轴标签
    plt.xlabel('阶数', fontsize=12)
    plt.ylabel('主攻击', fontsize=12)

    # 添加网格
    plt.grid(True)

    # 显示图形
    plt.show()
