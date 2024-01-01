import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义逻辑斯蒂函数
def logistic_function(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# 假设这些是从拟合得到的参数值
L = 83002.43064644493  # 逻辑斯蒂函数的L值
k = 0.19218195094148813     # 逻辑斯蒂函数的k值
x0 = 20.628743576666185     # 逻辑斯蒂函数的x0值

# 假设的原始数据长度（比如1月20日到2月29日共41天）
current_length = 41

# 预测未来30天的病例数
future_days = 60
future_x = np.array(range(current_length, current_length + future_days))

# 使用逻辑斯蒂模型进行预测
future_cases = logistic_function(future_x, L, k, x0)

# 可视化预测结果
plt.figure(figsize=(12, 6))
plt.plot(future_x, future_cases, label='预测的未来病例数')
plt.xlabel('天数（从1月20日开始）')
plt.ylabel('累计病例数')
plt.title('COVID-19累计确诊病例数未来趋势预测')
plt.legend()
plt.show()
