



import math

res = math.sqrt(27)
print(res)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res = fib(n-1)+fib(n-2)
        return res
    
n_terms = 20
for i in range(n_terms):
    print(fib(i))

runnian = lambda year:year % 400 == 0 or(year %4 ==0 and year %100 != 0)
for i in range(1800,2051):
    if runnian(i):
       print(i)


while True:
    b = int(input("请输入整数"))

    if b == 0:
        break
    else:
        pass
    print(b**2)
print("OVER")


a = 3.14
print(type(a))
print(int(a))


'''n = int(input("请输入n"))


def digui(n):
    if n == 0 or n ==1 :
        return 1
        
    else :
         result = 1
         
         result = n * digui(n - 1)
         return result
digui(n)
        
print(f"{n}!返回 {result}")'''

'''n = int(input("请输入n"))

def digui(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * digui(n - 1)   # 直接返回，无需中间变量

result = digui(n)                 # 接收递归结果
print(f"{n}! 返回 {result}")'''

n = int(input("请输入n"))

def digui(n):
    if n == 0 or n == 1:
        print(f"{n}! = 1")      # 打印基础情况
        return 1
    else:
        result = n * digui(n - 1)
        print(f"{n}! = {result}")  # 打印当前n的阶乘结果
        return result

result = digui(n)
print(f"最终 {n}! = {result}")




'''def factorial(n):
   
    print(f"递归调用: n = {n}")  # 输出当前递归的循环
    if n == 0:
        print("到达终止条件: 0! = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"{n}! = {n} * {n-1}! = {result}")
        return result

def main():
    while True:
        try:
            num = int(input("请输入一个非负整数（输入0退出程序）: "))
            if num == 0:
                print("程序结束")
                break
            elif num < 0:
                print("阶乘只适用于非负整数，请重新输入。")
                continue
            else:
                print(f"计算 {num}! 的结果为: {factorial(num)}")
                print("-" * 30)
        except ValueError:
            print("输入无效，请输入整数。")

if __name__ == "__main__":
    main()
'''
 