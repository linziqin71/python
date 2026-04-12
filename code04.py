import numpy as np
import time
import matplotlib.pyplot as plt
from functools import lru_cache


print("=" * 50)
print("任务1：鸡兔同笼问题（头35，脚94）")

A = np.array([[1, 1], [2, 4]])

b = np.array([35, 94])

solution = np.linalg.solve(A, b)

chickens, rabbits = solution[0], solution[1]
print(f"鸡的数量：{int(chickens)}，兔的数量：{int(rabbits)}")
print("-" * 50)


print("任务2：递归法计算斐波那契数列（0-36项）并记录耗时")

import time
import matplotlib. pylab as plt

def fibonacci_recursive(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


'''n_max_rec = 36
times_rec = []      # 存储每项的计算耗时（秒）
fib_values_rec = [] # 存储每项的斐波那契数值（可选）

for i in range(n_max_rec + 1):
    start = time.perf_counter()  # 高精度计时开始
    fib_val = fibonacci_recursive(i)
    end = time.perf_counter()
    elapsed = end - start
    times_rec.append(elapsed)
    fib_values_rec.append(fib_val)
   #print(f"第{i:2d}项：斐波那契数 = {fib_val:25d}，耗时 = {elapsed:.8f} 秒")

# 绘制耗时折线图（可改为散点图，此处用折线更清晰）
plt.figure(figsize=(8, 5))
plt.plot(fib_values_rec,times_rec,'ro',label="Measurement value")
plt.xlabel("FibnacciNumber of items")
plt.ylabel("Calculation time (s)")
plt.title("fibonacciNumber and calculation time")
plt.legend()
plt.grid(True)
plt.show()
print("-" * 50)'''
import time
import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res = fibonacci(n - 1) + fibonacci(n - 2)
        return res

num_terms = 37                  # 定义计算前n项
results = []                    # 定义空行列
x_list = []                     # 定义空行列

for i in range(0,num_terms):    # 循环计算每项斐波那契数列
    start_time = time.perf_counter()  # 保存计算开始用时
    fib_value = fibonacci(i)    # 计算第i项斐波那契数列
    end_time = time.perf_counter()    # 保存计算结束用时
    elapsed_time = end_time - start_time  # 计算总用时
    results.append(elapsed_time)  # 填充结果值
    x_list.append(i)             # 填充项数值

# 利用matplotlib绘图
plt.figure(figsize=(8, 5))       # 创建画布
plt.plot(x_list, results, 'ro', label="Measurement value")  # 绘制散点图
plt.xlabel("FibonacciNumber of items")  # 绘制横坐标标签
plt.ylabel("Calculation time (s)")        # 绘制纵坐标标签
plt.title("Fibonacci Numbers and Calculation time")  # 绘制图表名称
plt.legend()                     # 设定展示绘画窗口
plt.grid(True)                   # 设定展示网格
plt.show()                       # 开始描绘

# ==================== 任务3：迭代法计算斐波那契数1-300项，绘制散点图（绿色三角，虚线衔接）====================
print("任务3：迭代法计算斐波那契数列（1-300项）并绘图")
'''def fibonacci_iterative(n):
    
    if n == 0:
        return 0   # 根据常见定义：第1项为0，第2项为1；也可自行调整，本题范围1-300无歧义
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 计算 1 到 300 项耗时
n_max_iter = 301
times_iter = []   # 存储每项耗时
n_values = []

for n in range(0,n_max_iter):
    start = time.perf_counter()
    fib_val = fibonacci_iterative(n)  # 计算第n项
    end = time.perf_counter()
    times_iter.append(end - start)
    n_values.append(i)
    

# 绘图：绿色三角散点 + 虚线衔接
plt.figure(figsize=(12, 6))
# 先用 plot 画虚线（连接每个点）
plt.plot(n_values, times_iter, linestyle='--', color='green', linewidth=0.8, alpha=0.7)
# 再用 scatter 绘制绿色三角散点（覆盖在虚线上）
plt.scatter(n_values, times_iter, marker='^', color='green', s=20, label="计算耗时")
plt.xlabel("FibonacciNumber of items (n)")
plt.ylabel("Calculation time (s)")
plt.title("diedai Fibonacci Numbers and Calculation time）")
plt.legend()                     # 设定展示绘画窗口
plt.grid(True)                   # 设定展示网格
plt.show()                       # 开始描绘


print("\n所有任务执行完毕！")'''


import time
import matplotlib.pyplot as plt

def fibonacci_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

num_terms = 300
results = []
x_list = []

for i in range(1, num_terms + 1):
    start_time = time.perf_counter()
    fib_value = fibonacci_iter(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    results.append(elapsed_time)
    x_list.append(i)

plt.figure(figsize=(8, 5))
plt.plot(x_list, results, 'g^--', label="Iterative calculation time")
plt.xlabel("Fibonacci Number of items (1-300)")
plt.ylabel("Calculation time (s)")
plt.title("Fibonacci Numbers (Iterative) and Calculation time")
plt.legend()
plt.grid(True)
plt.show()