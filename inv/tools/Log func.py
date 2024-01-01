import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义逻辑斯蒂函数
def logistic_function(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# 定义指数函数
def exponential_function(x, a, b, c):
    return a * np.exp(b * x) + c

# 示例数据（1月20日到2月29日的累计确诊病例数）
y_data_combined = np.array([278, 309, 571, 830, 1297, 1985, 2761, 4537, 5997, 7736, 9720, 14380, 17205, 20438, 24324, 28018, 31161, 34546, 37198, 40171, 42638, 44653, 46472, 48467, 49970, 51091, 70548, 72436, 74185, 75002, 75891,76288, 76936, 77150, 77658, 78064, 78497, 78824, 79251, 79824])
x_data_combined = np.array(range(1, 41))  # 从1月20日到2月29日共41天

# 拟合逻辑斯蒂函数
popt_log, pcov_log = curve_fit(logistic_function, x_data_combined, y_data_combined, p0=[100000, 0.01, 20], maxfev=10000)
L, k, x0 = popt_log

# 拟合指数函数
popt_exp, pcov_exp = curve_fit(exponential_function, x_data_combined, y_data_combined, p0=[1, 0.1, y_data_combined[0]], maxfev=10000)
a, b, c = popt_exp

# 打印函数参数
print(f"逻辑斯蒂函数参数: L={L}, k={k}, x0={x0}")
print(f"指数函数参数: a={a}, b={b}, c={c}")

# 可视化
plt.figure(figsize=(12, 6))
plt.scatter(x_data_combined, y_data_combined, label='实际数据')
plt.plot(x_data_combined, logistic_function(x_data_combined, *popt_log), label='逻辑斯蒂拟合')
plt.plot(x_data_combined, exponential_function(x_data_combined, *popt_exp), label='指数拟合', linestyle='--')
plt.xlabel('天（从1月20日开始）')
plt.ylabel('累计病例数')
plt.title('COVID-19累计确诊病例数拟合（2020年1月和2月）')
plt.legend()
plt.show()
