import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import threading
import time

# 设置固定的工作量
work_load = 100000000000

# 模拟计算任务
def compute_task(work_per_thread):
    work_done = 0
    while work_done < work_per_thread:
        work_done += 1  # 这里模拟的是简单的计数任务

# 获取性能数据
def performance_data(thread_count, total_work_load):
    threads = []
    start_time = time.time()

    work_per_thread = total_work_load // thread_count

    for _ in range(thread_count):
        thread = threading.Thread(target=compute_task, args=(work_per_thread,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time

# 收集不同线程数下的总运行时间数据
thread_counts = np.array(range(1, 11))  # 线程数从1到10
run_times = np.array([performance_data(tc, work_load) for tc in thread_counts])

# 指数拟合函数
def exp_fit(x, a, b):
    return a * np.exp(b * x)

# 执行指数拟合
params, _ = curve_fit(exp_fit, thread_counts, run_times)

# 使用拟合参数创建拟合线
fit_line = exp_fit(thread_counts, *params)

# 绘制原始数据和拟合线
plt.scatter(thread_counts, run_times, label='Original Data')
plt.plot(thread_counts, fit_line, color='red', label=f'Exp Fit: y = {params[0]:.2f} * exp({params[1]:.2f} * x)')
plt.xlabel('Threads')
plt.ylabel('Total Run Time')
plt.title('Exponential Fit to Thread Count vs Run Time')
plt.legend()
plt.show()

# 输出拟合参数
print(f"Fit Parameters: a = {params[0]}, b = {params[1]}")
