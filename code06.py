sentence="Life is short,we need python"
sentence= sentence.lower()

counts={}
for c in sentence:
    counts[c] = counts.get(c,0) +1
print(counts)


# 合并"国家-面积"字典 dicAreas 和"国家-首都"字典 dicCapitals  5-4.py
dicAreas = {'俄罗斯': 1707.5, '加拿大': 997.1, '中国': 960.1, '美国': 936.4, '巴西': 854.7}
dicCapitals = {'俄罗斯': '莫斯科', '加拿大': '渥太华', '中国': '北京', '美国': '华盛顿', '巴西': '巴西利亚'}

dicCountries = {}
for key in dicAreas.keys():
    dicCountries[key] = [dicAreas[key], dicCapitals[key]]

for item in dicCountries.items():
    print(item)


setI={'Python','C++','C','Java','C#'}
setT={'Java','C','Python', 'C++','VB.NET'}

print("IEEE2018排行榜前五的编程语言有:")
print(setI)

print("TIOBE2018排行榜前五的编程语言有:")
print(setT)

print("前五名上榜的所有语言有:")
print(setI | setT)

print("在两个榜单同时进前五的语言有:")
print(setI & setT)

print("只在IEEE榜进前五的语言有:")
print(setI - setT)

print("只在一个榜单进前五的语言:")
print(setI ^ setT)


import matplotlib.pyplot as plt
from collections import Counter

def sieve_steps(n):
    """
    对2~n的数字执行埃拉托色尼筛法，
    返回数字列表和每个数字被标记的素数（最小质因子）
    """
    numbers = list(range(2, n + 1))
    N = len(numbers)
    # 初始状态：所有数字标记为0（未标记）
    colors = [0] * N
    # 标记是否为素数（True 表示尚未被剔除）
    is_prime = [True] * N

    # 遍历每个候选数字
    for i, p in enumerate(numbers):
        if is_prime[i]:                     # p 是素数
            # 将当前素数本身标记为 p
            colors[i] = p
            # 剔除 p 的倍数，从 p*p 开始
            for multiple in range(p * p, n + 1, p):
                j = multiple - 2            # 数字 multiple 在 numbers 中的索引
                if j < N and is_prime[j]:
                    is_prime[j] = False     # 标记为合数
                    colors[j] = p           # 记录该合数是被素数 p 标记的
    return numbers, colors

# 运行筛法，获取2~300的标记结果
numbers, colors = sieve_steps(300)

# 统计每个素数出现的次数
# colors 中每个元素都是某个素数（2~300之间的素数）
# 使用 Counter 自动统计频次
prime_counter = Counter(colors)

# 去除可能残留的0（实际不会出现，但安全起见过滤掉）
if 0 in prime_counter:
    del prime_counter[0]

# 获取所有素数（排序）和对应的频次
primes = sorted(prime_counter.keys())
frequencies = [prime_counter[p] for p in primes]

# 绘制直方图（柱状图）
plt.figure(figsize=(12, 6))
plt.bar(primes, frequencies, width=0.8, color='skyblue', edgecolor='black')

# 添加标签和标题
plt.xlabel("Prime number", fontsize=12)
plt.ylabel("The number of times is called", fontsize=12)
plt.title("Sieve of Eratosthenes (n=300)", fontsize=14)

# 显示网格（可选）
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 展示图形
plt.show()





