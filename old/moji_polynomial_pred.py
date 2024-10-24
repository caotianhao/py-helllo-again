import numpy as np

begin_degree = 2
end_degree = 3
begin_pred_level = 36
end_pred_level = 40

levels = np.array(range(10, 36))
main_atk = np.array([
    3850, 4510, 5280, 6160, 7260, 8580, 10120, 11935, 14025,
    16445, 19250, 22495, 26180, 30360, 35390, 40370, 46200,
    52580, 59510, 66990, 75020, 83600, 92730, 102410, 112640,
    123420
])


def main():
    for pred_level in range(begin_pred_level, end_pred_level + 1):
        total_predicted_value = 0
        for degree in range(begin_degree, end_degree + 1):
            coefficients = np.polyfit(levels, main_atk, degree)
            poly_func = np.poly1d(coefficients)
            predicted_value = poly_func(pred_level)
            total_predicted_value += predicted_value
            print(f"pred_level: {pred_level} degree: {degree}, Predicted value: {predicted_value:.2f}")

        print(f"avg: {total_predicted_value / (end_degree - begin_degree + 1):.2f}")
        print("--------------------------------------------------------------------")


if __name__ == "__main__":
    main()
