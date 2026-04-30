# coding: utf-8
# 程序设计基础 第八课

import os

# 文件的写入
f=open('example.txt', 'w', encoding='utf-8')    #在根目录中，以只可写模式，以utf-8编码打开文件
f.write("hellow world! \n")                     #写入内容
f.write("你好世界 \n")
f.close()                                       #关闭文件

# 传入相对路径或绝对路径，始终返回标准化的绝对路径
abs_path = os.path.abspath("example.txt")
print(abs_path)

# 文件的读取
f=open('example.txt', 'r', encoding='utf-8')    #在根目录中，以读取模式，以utf-8编码打开文件
data_1 = f.read()                               #读取全部内容
print(data_1)
f.close()

f=open('example.txt', 'r', encoding='utf-8')    #在根目录中，以读取模式，以utf-8编码打开文件
data_2 = f.readline()                           #逐行读取
print(data_2)
data_2 = f.readline()
print(data_2)
f.close()                                       #关闭文件

f=open('example.txt', 'r', encoding='utf-8')    #在根目录中，以读取模式，以utf-8编码打开文件
data_3 = f.readlines()                          #逐行读取将文件的行处理，转换为列表的元素处理
print(data_3)
f.close()                                       #关闭文件



import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体（根据系统可用字体调整，macOS/windows常用）
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "KaiTi"]  # 支持中文
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

import matplotlib.pyplot as plt
import numpy as np
import os

# ========== 1. 设置中文字体（防止图表乱码） ==========
plt.rcParams["font.sans-serif"] = ["SimHei", "KaiTi", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 2. 定义文件路径（请根据实际情况修改） ==========
# 如果文件在脚本同目录，直接用文件名；否则写完整路径
TIME_FILE = "cpu_feb_time.txt"      # 时间数据文件
CLOCK_FILE = "cpu_clock.txt"        # 频率数据文件

# 检查文件是否存在（可选，帮助定位问题）
if not os.path.exists(TIME_FILE):
    print(f"错误：找不到文件 {TIME_FILE}，当前目录是 {os.getcwd()}")
    print("请将文件放到脚本目录，或修改 TIME_FILE 为绝对路径")
    exit()
if not os.path.exists(CLOCK_FILE):
    print(f"错误：找不到文件 {CLOCK_FILE}")
    exit()

# ========== 实验5：创建 CPU → 计算时间列表 的字典 ==========
def read_time_file(filepath):
    """
    读取 cpu_feb_time.txt
    每行格式：时间(秒)，CPU型号   （注意逗号是中文全角"，"）
    返回字典 {CPU型号: [时间1, 时间2, ...]}
    """
    cpu_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 跳过空行和注释行（以#开头）
            if not line or line.startswith('#'):
                continue
            # 按中文逗号分割
            parts = line.split('，')
            if len(parts) < 2:
                continue
            time_str = parts[0].strip()
            cpu_model = parts[1].strip()
            try:
                time_val = float(time_str)
            except ValueError:
                continue   # 忽略无法转换的行
            # 存入字典
            if cpu_model not in cpu_dict:
                cpu_dict[cpu_model] = []
            cpu_dict[cpu_model].append(time_val)
    return cpu_dict

# 读取数据
time_dict = read_time_file(TIME_FILE)
print("=" * 60)
print("实验5结果：CPU型号 → 计算时间列表（仅显示前5个）")
for i, (cpu, times) in enumerate(list(time_dict.items())[:5]):
    print(f"{cpu}: {times}")
print(f"共有 {len(time_dict)} 种不同的CPU型号")
print("=" * 60)

# ========== 实验6：读取频率数据并绘制散点图（误差棒图） ==========
def read_clock_file(filepath):
    """
    读取 cpu_clock.txt
    每行格式：基频，睿频，CPU型号   （中文逗号分隔）
    返回字典 {CPU型号: (基频, 睿频)}
    """
    freq_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('，')
            if len(parts) < 3:
                continue
            base_str = parts[0].strip()
            turbo_str = parts[1].strip()
            # 剩余部分拼接成完整型号（有些型号本身含空格，不需要分割）
            cpu_model = '，'.join(parts[2:]).strip()
            try:
                base_freq = float(base_str)
                turbo_freq = float(turbo_str)
            except ValueError:
                continue
            freq_dict[cpu_model] = (base_freq, turbo_freq)
    return freq_dict

freq_dict = read_clock_file(CLOCK_FILE)

# 准备绘图数据
x_center = []   # 横坐标中心值（基频和睿频的中点）
x_err = []      # 横坐标误差（半宽，即 (睿频-基频)/2）
y_mean = []     # 纵坐标平均值（计算时间的均值）
y_std = []      # 纵坐标标准差
labels = []     # 存CPU型号用于标注

# 只处理同时在两个字典中的CPU
for cpu in time_dict:
    if cpu not in freq_dict:
        print(f"警告：CPU '{cpu}' 在频率文件中未找到，跳过")
        continue
    base, turbo = freq_dict[cpu]
    times = time_dict[cpu]
    mean_val = np.mean(times)
    # 计算样本标准差（如果只有一个数据点，标准差为0）
    if len(times) == 1:
        std_val = 0.0
    else:
        std_val = np.std(times, ddof=1)   # ddof=1 表示样本标准差
    
    center_freq = (base + turbo) / 2
    half_range = (turbo - base) / 2
    
    x_center.append(center_freq)
    x_err.append(half_range)
    y_mean.append(mean_val)
    y_std.append(std_val)
    labels.append(cpu)

print(f"成功匹配 {len(x_center)} 个CPU型号，将绘制散点图")

# 绘制带误差棒的散点图
plt.figure(figsize=(12, 6))
plt.errorbar(x_center, y_mean, 
             xerr=x_err, yerr=y_std,
             fmt='o',                # 圆形点
             capsize=3,              # 误差棒端帽大小
             elinewidth=1,           # 误差棒线宽
             markeredgecolor='black',
             alpha=0.7,
             label='CPU性能数据')

# 添加全局平均时间参考线
global_mean = np.mean(y_mean)
plt.axhline(y=global_mean, color='red', linestyle='--', linewidth=1,
            label=f'全局平均时间 = {global_mean:.2f} 秒')

# 坐标轴标签和标题
plt.xlabel("CPU频率 [GHz] （横轴范围：基频 → 睿频）", fontsize=12)
plt.ylabel("计算斐波那契第36项时间 [秒]", fontsize=12)
plt.title("不同CPU频率与递归计算时间的关系（误差棒表示频率范围和时间波动）", fontsize=14)

# 增加网格
plt.grid(True, linestyle=':', alpha=0.6)

# 可选：为前10个点添加文字标签（避免重叠）
for i in range(min(10, len(labels))):
    plt.annotate(labels[i], (x_center[i], y_mean[i]),
                 fontsize=8, xytext=(5,5), textcoords='offset points')

plt.legend()
plt.tight_layout()
plt.show()