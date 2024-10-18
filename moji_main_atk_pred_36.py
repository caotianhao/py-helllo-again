import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'

levels = np.array(range(10, 36))
main_atk = np.array([
    3850, 4510, 5280, 6160, 7260, 8580, 10120, 11935, 14025,
    16445, 19250, 22495, 26180, 30360, 35390, 40370, 46200,
    52580, 59510, 66990, 75020, 83600, 92730, 102410, 112640,
    123420
])

degree = 4
coefficients = np.polyfit(levels, main_atk, degree)
poly_func = np.poly1d(coefficients)

x_fit = np.linspace(10, 35, 100)
y_fit = poly_func(x_fit)

plt.scatter(levels, main_atk, color='red', label='原始数据')
plt.plot(x_fit, y_fit, color='blue', label=f'多项式拟合 (阶数 {degree})')
plt.xlabel('等级')
plt.ylabel('攻击力')
plt.title('攻击力与等级的关系')
plt.legend()
plt.grid()
plt.show()


def print_polynomial(coeffs):
    terms = []
    for i, coeff in enumerate(coeffs):
        power = len(coeffs) - i - 1
        if power > 1:
            terms.append(f"{coeff:.2f}x^{power}")
        elif power == 1:
            terms.append(f"{coeff:.2f}x")
        else:
            terms.append(f"{coeff:.2f}")

    polynomial = " + ".join(terms)
    return polynomial


polynomial_str = print_polynomial(coefficients)
print(f"拟合多项式: {polynomial_str}")

x_value = 36
predicted_value = poly_func(x_value)

print(f"当 x = {x_value} 时，预测的攻击力为: {predicted_value:.2f}")
