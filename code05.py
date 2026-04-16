import sys
import time

# ================= 实验1：验证元组可作为字典键 =================
print("=== 实验1：元组作为字典键 ===")
# 字典的键必须是不可变类型，元组是不可变的，因此可以作为键
my_dict = {("name", "age"): "张三", ("city", "code"): "北京"}
# 访问字典中的值
print("键 ('name', 'age') 对应的值为:", my_dict[("name", "age")])
print("键 ('city', 'code') 对应的值为:", my_dict[("city", "code")])
# 尝试使用列表作为键会报错（取消注释下方代码可验证）
# my_dict[["name", "age"]] = "李四"  # TypeError: unhashable type: 'list'
print("-" * 40)

# ================= 实验2：遍历速度比较 =================
print("=== 实验2：列表与元组的遍历速度 ===")
# 创建一个较大的列表和元组，包含相同数量的整数
size = 10_000_000  # 1000万个元素
print(f"正在创建包含 {size} 个元素的列表和元组...")
list_data = list(range(size))
tuple_data = tuple(range(size))

# 测试遍历列表的时间
start = time.time()
total_list = 0
for num in list_data:
    total_list += num
end = time.time()
list_time = end - start

# 测试遍历元组的时间
start = time.time()
total_tuple = 0
for num in tuple_data:
    total_tuple += num
end = time.time()
tuple_time = end - start

print(f"列表遍历耗时: {list_time:.4f} 秒，求和结果: {total_list}")
print(f"元组遍历耗时: {tuple_time:.4f} 秒，求和结果: {total_tuple}")
# 速度比较
if list_time < tuple_time:
    print("结论：列表遍历速度更快")
elif list_time > tuple_time:
    print("结论：元组遍历速度更快")
else:
    print("结论：两者速度相近")
print("-" * 40)

# ================= 实验3：存储空间比较 =================
print("=== 实验3：列表与元组的存储空间 ===")
# 创建内容相同但规模不同的列表和元组
small_list = [1, 2, 3]
small_tuple = (1, 2, 3)
large_list = list(range(1000))
large_tuple = tuple(range(1000))

print("小规模数据（3个整数）：")
print(f"列表占用内存: {sys.getsizeof(small_list)} 字节")
print(f"元组占用内存: {sys.getsizeof(small_tuple)} 字节")
print("\n大规模数据（1000个整数）：")
print(f"列表占用内存: {sys.getsizeof(large_list)} 字节")
print(f"元组占用内存: {sys.getsizeof(large_tuple)} 字节")
print("\n结论：元组通常比相同内容的列表占用更少的内存，因为列表需要额外空间来支持动态扩容。")









import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

matplotlib.rcParams["font.family"] = "kaiti"  # 设置中文字体


def sieve_steps(n):
    # 对2~n的数字执行埃拉托色尼筛法
    # 返回数字列表和每一步的状态（颜色列表及描述）
    # 数字范围为2到n
    numbers = list(range(2, n + 1))
    N = len(numbers)
    # 初始状态：所有数字均为蓝色
    colors = ['blue'] * N
    # 标记是否为素数（True 表示未剔除）
    is_prime = [True] * N
    # steps：每一步状态（颜色列表，当前动作描述）
    steps = []

    # 初始状态帧
    steps.append((colors.copy(), "初始状态"))

    # 遍历每个候选数字
    for i, p in enumerate(numbers):
        # 若该数字尚未被剔除，则进行检查
        if is_prime[i]:
            # 第一步：将当前候选数字标为红色（正在检查）
            temp = colors.copy()
            temp[i] = 'red'
            steps.append((temp, f"检查：{p}"))

            # 该数字为素数：确认后标为绿色
            colors[i] = 'green'
            steps.append((colors.copy(), f"确认素数：{p}"))

            # 剔除 p 的倍数，从 p*p 开始
            for multiple in range(p * p, n + 1, p):
                j = multiple - 2  # 数字 multiple 在 numbers 中的索引
                if j < N and is_prime[j]:
                    is_prime[j] = False
                    colors[j] = 'red'  # 被剔除时的指示颜色
                    steps.append((colors.copy(), f"剔除 {multiple}"))
                    colors[j] = 'white'
                    steps.append((colors.copy(), f"剔除 {multiple}"))

    return numbers, steps


# 获取2~300的数字及动画步骤
numbers, steps = sieve_steps(300)

# 初始化图表
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(numbers, [1] * len(numbers), color='blue')
ax.set_xlabel("数字")
ax.set_ylabel("状态")
ax.set_title("埃拉托色尼筛法求300以内的素数")
ax.set_xlim(0, 300)
ax.set_ylim(0, 1.5)


# 更新函数：根据当前帧状态更新每个条形的颜色
def update(frame):
    current_colors, action = steps[frame]
    for bar, c in zip(bars, current_colors):
        bar.set_color(c)
    ax.set_title(action)


# 创建动画对象，帧间隔500毫秒，每秒2帧
ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=100)

# 保存为 GIF 文件
writer = PillowWriter(fps=10)
ani.save("sieve_eratosthenes.gif", writer=writer)

plt.show()



